def domain_name(domain):
    """Domain name extractor.

    Function that, when given a URL as a string, returns only the domain name as a string.
    """
    domain = domain[8:]
    if domain[2] == "w":
        result = domain.split(".")
        return result[1]
    else:
        result = domain.split(".")
        return result[0]
if __name__ == "__main__":
    print(domain_name("https://github.com/"))