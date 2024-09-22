// Written by Juan Pablo Gutiérrez
// 22 09 2024
// Represents a specific system which will contain actions

struct System {
    name: String,
}

impl System {
    fn new(name: &str) -> Self {
        Self {
            name: name.to_string(),
        }
    }

    fn init(&self) {
        println!("{} initialized", self.name);
    }

    fn execute_periodic(&self) {
        println!("{} executed", self.name);
    }
}
