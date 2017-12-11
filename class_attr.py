# -*- coding:utf8 -*-


class HD(object):
    user = 'jerry'

    def __init__(self, user):
        self.user = user


if __name__ == '__main__':
    a = HD('tom')
    print a.user
    print a.__class__.user
