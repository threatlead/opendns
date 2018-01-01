# ![Domains](https://s13.postimg.org/bdlsdeyhj/domain_1.png) OpenDNS Scraper

## Usage

### TLD list

```python
import opendns
print(opendns.OpenDns.tld_list()[:10])
```

```javascript
[
    (1, 'com'),
    (2, 'net'),
    (3, 'org'),
    (4, 'googleapis.com'),
    (5, 'io'),
    (6, 'tv'),
    (7, 'co'),
    (8, 's3.amazonaws.com'),
    (9, 'elb.amazonaws.com'),
    (10, 'ru')
]
>>>
```

### Domain List

```python
print(opendns.OpenDns.domain_list()[:10])
```

```javacript
[
    (1, 'netflix.com'),
    (2, 'api-global.netflix.com'),
    (3, 'google.com'),
    (4, 'ichnaea.netflix.com'),
    (5, 'microsoft.com'),
    (6, 'www.google.com'),
    (7, 'facebook.com'),
    (8, 'doubleclick.net'),
    (9, 'g.doubleclick.net'),
    (10, 'googleads.g.doubleclick.net')
]
```