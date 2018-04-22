import pandas as pd
import read

df = read.load_data()

def remove_subdomains(domain):
    segments = domain.split('.')
    return '.'.join(segments[len(segments) - 2:])

def top_domains():
    domains = df['url'].dropna()
    domains = domains.apply(func=remove_subdomains)
    for name, row in domains.items():
        print('{0}: {1}'.format(name, row))
    
if __name__ == '__main__':
    top_domains()