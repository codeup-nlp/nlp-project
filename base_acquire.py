"""
A module for obtaining repo readme and language data from the github API.

Before using this module, read through it, and follow the instructions marked
TODO.

After doing so, run it like this:

    python acquire.py

To create the `data.json` file that contains the data.
"""
import os
import json
from typing import Dict, List, Optional, Union, cast
import requests

from env import github_token, github_username

# TODO: Make a github personal access token.
#     1. Go here and generate a personal access token: https://github.com/settings/tokens
#        You do _not_ need select any scopes, i.e. leave all the checkboxes unchecked
#     2. Save it in your env.py file under the variable `github_token`
# TODO: Add your github username to your env.py file under the variable `github_username`
# TODO: Add more repositories to the `REPOS` list below.

REPOS = [ 
"ccxt/ccxt",
"openssl/openssl",
"HelloZeroNet/ZeroNet",
"freqtrade/freqtrade",
"amark/gun",
"brix/crypto-js",
"google/tink",
"jedisct1/libsodium",
"krzyzanowskim/CryptoSwift",
"cryptomator/cryptomator",
"bitwiseshiftleft/sjcl",
"ctf-wiki/ctf-wiki",
"StockSharp/StockSharp",
"pyca/cryptography",
"digitalbazaar/forge",
"aws/s2n-tls",
"hummingbot/hummingbot",
"google/end-to-end",
"PrivateBin/PrivateBin",
"CryptoSignal/Crypto-Signal",
"jesse-ai/jesse",
"trustwallet/assets",
"Mbed-TLS/mbedtls",
"bitpay/wallet",
"Haehnchen/crypto-trading-bot",

"NASAWorldWind/WebWorldWind", 
"r-spacex/SpaceX-API", 
"nasa/fprime", 
"NASAWorldWind/WorldWindJava", 
"nasa-gibs/worldview", 
"nasa/apod-api", 
"chrislgarry/Apollo-11", 
"nasa/NASA-3D-Resources", 
"nasa/astrobee", 
"bloominstituteoftechnology/nasa-photo-of-the-day", 
"nasa/Open-Source-Catalog", 
"nasa/CrisisMappingToolkit",
"nasa/code-nasa-gov", 
"nasa/earthdata-search",
"NASAWorldWind/WorldWindAndroid", 
"spaceship-prompt/spaceship-prompt",
"rt-bishop/Look4Sat", 
"nasa-jpl/COVID-19-respirators",
"jakiestfu/himawari.js", 
"orbitalindex/awesome-space", 
"CelestiaProject/Celestia", 
"trehn/termtrack", 
"barrosfilipe/Rocket-Lab-API", 
"Trinitui/Rocket-Lab-API-Reborn", 
"Onnamission/SpaceX-Analytics", 

"NeuromatchAcademy/course-content",
"cnrl/cns-project-template",
"translationalneuromodeling/tapas",
"ContextLab/computational-neuroscience",
"computational-neuroscience/Computational-Neuroscience-UW",
"neurolib-dev/neurolib",
"simetenn/uncertainpy",
"CompCogNeuro/sims",
"compmem/compsy",
"conorhoughton/COMS30127",
"ashumeow/Computational-NeuroScience",
"kuz/Computational-Neuroscience-Course",
"INCF/neuroshapes",
"CompCogNeuro/ed4",
"alisharifi2000/CS-SBU-ComputationalNeuroScience2021-projects",
"karnigili/Computational-Neuroscience",
"robclewley/compneuro",
"btel/python-in-neuroscience-tutorials",
"neurodebian/neurodebian",
"alfredcai/Coursera-Computational-NeuroScience",
"neurodata/brainlit",
"patrickmineault/xcorr-notebooks",
"ITNG/ModelingNeuralDynamics",
"CNS-OIST/a310_cns_2018",
"rougier/Neurosciences",


"hyperledger-archives/education-cryptomoji",
"DataONEorg/Education",
"data-edu/data-science-in-education",

"bitcoin/bitcoin",
"hyperledger-archives/education-cryptomoji",
"DataONEorg/Education",
"data-edu/data-science-in-education",
"tesseract-ocr/tesseract", 

"AgoraIO-Usecase/eEducation",
"WikiEducationFoundation/WikiEduDashboard",
"puppetlabs/education-builds",
"sugarlabs/musicblocks",
"microsoft/Web-Dev-For-Beginners",
"jakemdrew/EducationDataNC",
"shama/letswritecode",

"netdata/netdata",

"CTFd/CTFd",
"anton-liauchuk/educational-platform",
"Akshima-Ghai/OneEducationalWebsiteForAll",
"llSourcell/Watch-Me-Build-an-Education-Startup",
"tecladocode/rest-apis-flask-python",
"psi4/psi4numpy",
"unstructuredstudio/zubhub",
"zero-to-mastery/start-here-guidelines",
"getify/Functional-Light-JS",
"arschles/go-in-5-minutes",

"microsoft/CyberBattleSim",
"mitre-attack/car",
"eth0izzle/bucket-stream", 
"cybercommons/cybercom-cookiecutter",
"state-hiu/cybergis-scripts",

"microsoft/PowerToys",
"ReactiveX/RxJava",
"kdn251/interviews",
"web-sys1/ActionData",
"rvaughan/coronavirus-data",
"weareblahs/covidcases",
"covid19-eu-zh/covid19-eu-data",
"ercbk/Indiana-COVIDcast-Dashboard",
"ercbk/Indiana-COVID-19-Website",
"RamiKrispin/coronavirus",
"covidatlas/coronadatascraper",
"minvws/nl-covid19-notification-app-website",
"BustByte/coronastatus",
"tomwhite/covid-19-uk-data",
"vinitshahdeo/Water-Monitoring-System",
"labnol/covid19-vaccine-tracker",

"google/googletest",
"apache/incubator-doris",
"fmtlib/fmt",
"opencv/opencv",
"microsoft/calculator",
"microsoft/winget-cli",
"IntelLabs/control-flag",
"onnx/onnx",
"catchorg/Catch2",
"facebook/folly"

]

headers = {"Authorization": f"token {github_token}", "User-Agent": github_username}

if headers["Authorization"] == "token " or headers["User-Agent"] == "":
    raise Exception(
        "You need to follow the instructions marked TODO in this script before trying to use it"
    )


def github_api_request(url: str) -> Union[List, Dict]:
    response = requests.get(url, headers=headers)
    response_data = response.json()
    if response.status_code != 200:
        print(url)
        raise Exception(
            f"Error response from github api! status code: {response.status_code}, "
            f"response: {json.dumps(response_data)}"
        )
    return response_data


def get_repo_language(repo: str) -> str:
    url = f"https://api.github.com/repos/{repo}"
    repo_info = github_api_request(url)
    if type(repo_info) is dict:
        repo_info = cast(Dict, repo_info)
        if "language" not in repo_info:
            raise Exception(
                "'language' key not round in response\n{}".format(json.dumps(repo_info))
            )
        return repo_info["language"]
    raise Exception(
        f"Expecting a dictionary response from {url}, instead got {json.dumps(repo_info)}"
    )


def get_repo_contents(repo: str) -> List[Dict[str, str]]:
    url = f"https://api.github.com/repos/{repo}/contents/"
    contents = github_api_request(url)
    if type(contents) is list:
        contents = cast(List, contents)
        return contents
    raise Exception(
        f"Expecting a list response from {url}, instead got {json.dumps(contents)}"
    )


def get_readme_download_url(files: List[Dict[str, str]]) -> str:
    """
    Takes in a response from the github api that lists the files in a repo and
    returns the url that can be used to download the repo's README file.
    """
    for file in files:
        if file["name"].lower().startswith("readme"):
            return file["download_url"]
    return ""


def process_repo(repo: str) -> Dict[str, str]:
    """
    Takes a repo name like "gocodeup/codeup-setup-script" and returns a
    dictionary with the language of the repo and the readme contents.
    """
    contents = get_repo_contents(repo)
    readme_download_url = get_readme_download_url(contents)
    if readme_download_url == "":
        readme_contents = ""
    else:
        readme_contents = requests.get(readme_download_url).text
    return {
        "repo": repo,
        "language": get_repo_language(repo),
        "readme_contents": readme_contents,
    }


def scrape_github_data() -> List[Dict[str, str]]:
    """
    Loop through all of the repos and process them. Returns the processed data.
    """
    return [process_repo(repo) for repo in REPOS]


if __name__ == "__main__":
    data = scrape_github_data()
    json.dump(data, open("data.json", "w"), indent=1)
