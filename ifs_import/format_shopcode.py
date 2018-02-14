
def main():
    with open('store_code.txt') as f, open('format_store_code.txt', 'w') as g:
        for l in f.readlines():
            g.write("'{}',\n".format(l.strip()))


if __name__ == '__main__':
    main()
