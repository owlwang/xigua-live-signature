import execjs

with open('xigua.js', 'r') as f:
    jscode = f.read()
ctx = execjs.compile(jscode)


def get_signature(path):
    return ctx.call("get_signature", path)


if __name__ == '__main__':
    sig = get_signature('/api/feed/category/more/1/1602314750624/113')
    print(sig)
