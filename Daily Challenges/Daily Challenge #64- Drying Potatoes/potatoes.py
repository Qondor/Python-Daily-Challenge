def potatoes_dryer(p0, w0, p1):
    return w0 * (100-p0) / (100-p1)

if __name__ == "__main__":
    print(potatoes_dryer(99, 100, 98))