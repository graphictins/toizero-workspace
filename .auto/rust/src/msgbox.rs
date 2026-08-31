

use rfd::{MessageDialog, MessageLevel};

pub fn show(title: &str, message: &str) {
    MessageDialog::new()
        .set_title(title)
        .set_description(message)
        .set_level(MessageLevel::Info)
        .show();
}