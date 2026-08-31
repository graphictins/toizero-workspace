

mod msgbox; // Link the msgbox.rs file

use std::fs;
use serde::{Deserialize, Serialize};
use toml;

#[derive(Serialize, Deserialize, Default)]
struct Stats { task_left: usize }

#[derive(Serialize, Deserialize)]
struct Popup {
    #[serde(default = "fallback_msg")]
    message: String,
}

fn fallback_msg() -> String {
    "$ Taskleft, Keep it up champ!".to_string()
}

impl Default for Popup {
    fn default() -> Self {
        Self { message: fallback_msg() }
    }
}

#[derive(Serialize, Deserialize, Default)]
struct Data {
    stats: Stats,
    popup: Popup,
}

fn main() {
    let exe_dir = std::env::current_exe().expect("Failed path").parent().unwrap().to_path_buf();
    let toml_path = exe_dir.join("data.toml");
    let note_path = exe_dir.parent().expect("No parent").join("note.md");

    if let Ok(content) = fs::read_to_string(&note_path) {
        let current: usize = content.lines()
            .filter(|l| l.contains("⚛️") || l.contains("🆘"))
            .count();

        let mut data: Data = fs::read_to_string(&toml_path)
            .ok()
            .and_then(|s| toml::from_str(&s).ok())
            .unwrap_or_default();

        if current != data.stats.task_left {
            let new_content: Vec<String> = content.lines()
                .map(|l| if l.contains("### TaskLeft ==") { 
                    format!("### TaskLeft == {}", current) 
                } else { 
                    l.to_string() 
                })
                .collect();
            
            let _ = fs::write(&note_path, new_content.join("\n"));

            data.stats.task_left = current;
            let _ = fs::write(&toml_path, toml::to_string(&data).unwrap());

            let template = if data.popup.message.is_empty() {
                fallback_msg()
            } else {
                data.popup.message.clone()
            };
            
            let display_msg = template.replace("$ Taskleft", &current.to_string());
            
            // Call the function in msgbox.rs
            msgbox::show("TOIZero Progress", &display_msg);
        }
    }
}