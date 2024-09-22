// Written by Juan Pablo Gutiérrez
// 20 09 2024

use crate::actions::actions::Action;
use std::collections::Vec;

struct ActionScheduler {}

impl ActionScheduler {
    fn new() -> Self {
        Self {}
    }

    fn schedule(&self, actions: Vec<Action>) {
        actions.iter().for_each(|action| {
            action.init();
        });
    }
}
