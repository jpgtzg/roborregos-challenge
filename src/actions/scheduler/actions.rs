// Written by Juan Pablo Gutiérrez
// 20 09 2024

struct Action {
    name: String,
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

    fn finalize(&self) {
        println!("{} finalized", self.name);
    }

    fn is_finished(&self) -> bool {
        true
    }
}