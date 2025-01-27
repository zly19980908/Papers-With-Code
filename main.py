'''
This repository is builded and maintained by Mengxu(mengxu98@qq.com).
If you interested it, please add items as follow rules, and PR:
You can choose one of the following ways:

1) Refer to the 'README' file and manually fill in the following information:
    Add "| Journal | Date | Title | Code | Data | Citation |";
        For Journal and Title, please sort by A-Z;
        For Date, please sort by published date;
        For Code and Data, please reference: https://img.shields.io/;
        For Citation, the data of Citation could obtain from: https://www.semanticscholar.org/.

2) Automatically fill in information using 'extract_paper_infor' function:
    Parameter: 'url_paper', need to provide a link to the paper from https://www.semanticscholar.org/;
    Parameter: 'code_language', the main programming languages used in the paper;
    Parameter: 'url_code', code storage address in the paper;
    Parameter: 'data_database', database for storing data in the paper;
    Parameter: 'url_data', data storage address in the paper.

    Note: please shut down the proxy service when using this script!
    
Note: now this script only supports some open access journals correctly, such as "Nature communications", 
      and some journals will not allow extract information.
      So, you should use semanticscholar APIs as much as possible to obtain information,
      and manually fill in other parameters, such as 'code_language', 'url_code', 'data_database' and 'url_data'.

If you encounter any problems when using this script, please issue on GitHub or contact me.
'''

# Import function
from extract_paper_information import extract_paper_infor

######################
# ***--- Here ---*** #
######################

# The URL of paper obtain from: https://www.semanticscholar.org/
url_paper = "https://www.semanticscholar.org/paper/Single-cell-analysis-reveals-prognostic-fibroblast-Hanley-Waise/a5b158dbafff3ade8a9779c134441e5f3db18e2d"
url_paper = "https://api.semanticscholar.org/v1/paper/a5b158dbafff3ade8a9779c134441e5f3db18e2d"  # test
code_language = ""
url_code = ""
data_database = ""
url_data = ""

extract_paper_infor(url_paper,
                    code_language,
                    url_code,
                    data_database,
                    url_data,
                    file="test.md")  # "README.md"
