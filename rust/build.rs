

fn main() {
    // Passing std::iter::empty::<&str>() satisfies the second argument requirement
    embed_resource::compile("manifest.rc", std::iter::empty::<&str>());
}