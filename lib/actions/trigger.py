from typing import Callable, Optional
from wpilib.command import Command
from wpilib.event import EventLoop
from wpilib.util import requireNonNullParam
from wpilib.math.filter import Debouncer

class Trigger:
    def __init__(self, loop: EventLoop, condition: Callable[[], bool]):
        self._loop = requireNonNullParam(loop, "loop", "Trigger")
        self._condition = requireNonNullParam(condition, "condition", "Trigger")
        self._pressed_last = self._condition()

    def on_true(self, command: Command) -> 'Trigger':
        requireNonNullParam(command, "command", "onTrue")
        self._loop.bind(self._create_runnable(command, True))
        return self

    def on_false(self, command: Command) -> 'Trigger':
        requireNonNullParam(command, "command", "onFalse")
        self._loop.bind(self._create_runnable(command, False))
        return self

    def while_true(self, command: Command) -> 'Trigger':
        requireNonNullParam(command, "command", "whileTrue")
        self._loop.bind(self._create_while_runnable(command, True))
        return self

    def while_false(self, command: Command) -> 'Trigger':
        requireNonNullParam(command, "command", "whileFalse")
        self._loop.bind(self._create_while_runnable(command, False))
        return self

    def toggle_on_true(self, command: Command) -> 'Trigger':
        requireNonNullParam(command, "command", "toggleOnTrue")
        self._loop.bind(self._create_toggle_runnable(command, True))
        return self

    def toggle_on_false(self, command: Command) -> 'Trigger':
        requireNonNullParam(command, "command", "toggleOnFalse")
        self._loop.bind(self._create_toggle_runnable(command, False))
        return self

    def _create_runnable(self, command: Command, is_true: bool) -> Callable[[], None]:
        return lambda: self._check_and_run(command, is_true)

    def _check_and_run(self, command: Command, is_true: bool) -> None:
        current_pressed = self._condition()
        if (is_true and not self._pressed_last and current_pressed) or \
           (not is_true and self._pressed_last and not current_pressed):
            command.schedule()
        self._pressed_last = current_pressed

    def _create_while_runnable(self, command: Command, is_true: bool) -> Callable[[], None]:
        return lambda: self._check_while(command, is_true)

    def _check_while(self, command: Command, is_true: bool) -> None:
        current_pressed = self._condition()
        if is_true:
            if not self._pressed_last and current_pressed:
                command.schedule()
            elif self._pressed_last and not current_pressed:
                command.cancel()
        else:
            if self._pressed_last and not current_pressed:
                command.schedule()
            elif not self._pressed_last and current_pressed:
                command.cancel()
        self._pressed_last = current_pressed

    def _create_toggle_runnable(self, command: Command, is_true: bool) -> Callable[[], None]:
        return lambda: self._check_toggle(command, is_true)

    def _check_toggle(self, command: Command, is_true: bool) -> None:
        current_pressed = self._condition()
        if (is_true and not self._pressed_last and current_pressed) or \
           (not is_true and self._pressed_last and not current_pressed):
            if command.is_scheduled():
                command.cancel()
            else:
                command.schedule()
        self._pressed_last = current_pressed

    def get_as_boolean(self) -> bool:
        return self._condition()

    def and_condition(self, trigger: Callable[[], bool]) -> 'Trigger':
        return Trigger(self._loop, lambda: self.get_as_boolean() and trigger())

    def or_condition(self, trigger: Callable[[], bool]) -> 'Trigger':
        return Trigger(self._loop, lambda: self.get_as_boolean() or trigger())

    def negate(self) -> 'Trigger':
        return Trigger(self._loop, lambda: not self.get_as_boolean())

    def debounce(self, seconds: float, type: Optional[str] = None) -> 'Trigger':
        return Trigger(
            self._loop,
            Debouncer(seconds, type).calculate(self._condition)
        )
