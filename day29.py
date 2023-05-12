def outer(father):
    def inner(son):
        nonlocal father
        father = "father变成了孙笑川"
        print(f"爸爸是{father},儿子是{son}")
    return inner

fn = outer("丁真")
fn("鸡哥")
