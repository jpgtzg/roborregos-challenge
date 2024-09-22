// Written by Juan Pablo Gutiérrez
// 20 09 2024

use std::collections::HashMap;

struct Action {
    name: String,
    requirements: HashMap<System>,
}

impl Action {
    fn new(name: &str) -> Self {
        Self {
            name: name.to_string(),
        }
    }

    fn init(&self) {
        println!("{} initialized", self.name);
    }

    fn execute(&self) {
        println!("{} executed", self.name);
    }

    fn finalize(&self, interrupted : bool) {
        println!("{} finalized", self.name);
    }

    fn is_finished(&self) -> bool {
        true
    }

    fn add_requirements(&self, requirements: Vec<System>) {
        requirements.iter().for_each(|system| {
            self.requirements.insert(system);
        });
    }
}