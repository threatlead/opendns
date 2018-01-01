import requests
import zipfile
import io


class OpenDns:
    """
    OpenDNS website scraper
    """
    base_url = 'http://s3-us-west-1.amazonaws.com'
    base_static = '{0}/umbrella-static'.format(base_url)
    top_domains = '{0}/top-1m.csv.zip'.format(base_static)
    top_tlds = '{0}/top-1m-TLD.csv.zip'.format(base_static)

    @classmethod
    def _download_zip_file(cls, zip_url, zip_file):
        r = requests.get(zip_url)
        r.raise_for_status()
        z = zipfile.ZipFile(io.BytesIO(r.content))
        return z.read(zip_file)

    @classmethod
    def tld_list(cls, ):
        contents = cls._download_zip_file(OpenDns.top_tlds, 'top-1m-TLD.csv')
        data = []
        for line in contents.splitlines():
            rank, suffix = line.split(b',')
            data.append((int(rank), suffix.decode('idna')))
        return data

    @classmethod
    def domain_list(cls, ):
        contents = cls._download_zip_file(OpenDns.top_domains, 'top-1m.csv')
        data = []
        for line in contents.splitlines():
            rank, domain = line.split(b',')
            try:
                domain = domain.decode('idna')
            except:
                continue
            else:
                data.append((int(rank), domain))
        return data
