{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNjUcl/kW2dIHIE+EYpi4tc",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/meharaliaftab/steamlit/blob/main/webscraper_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VBlXGRFrM_Un",
        "outputId": "e7f34276-ca64-46ff-f981-46781e79b26c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting streamlit\n",
            "  Downloading streamlit-1.22.0-py2.py3-none-any.whl (8.9 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m8.9/8.9 MB\u001b[0m \u001b[31m79.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: altair<5,>=3.2.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.2.2)\n",
            "Collecting blinker>=1.0.0 (from streamlit)\n",
            "  Downloading blinker-1.6.2-py3-none-any.whl (13 kB)\n",
            "Requirement already satisfied: cachetools>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (5.3.0)\n",
            "Requirement already satisfied: click>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.1.3)\n",
            "Collecting importlib-metadata>=1.4 (from streamlit)\n",
            "  Downloading importlib_metadata-6.6.0-py3-none-any.whl (22 kB)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.10/dist-packages (from streamlit) (1.22.4)\n",
            "Requirement already satisfied: packaging>=14.1 in /usr/local/lib/python3.10/dist-packages (from streamlit) (23.1)\n",
            "Requirement already satisfied: pandas<3,>=0.25 in /usr/local/lib/python3.10/dist-packages (from streamlit) (1.5.3)\n",
            "Requirement already satisfied: pillow>=6.2.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.4.0)\n",
            "Requirement already satisfied: protobuf<4,>=3.12 in /usr/local/lib/python3.10/dist-packages (from streamlit) (3.20.3)\n",
            "Requirement already satisfied: pyarrow>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (9.0.0)\n",
            "Collecting pympler>=0.9 (from streamlit)\n",
            "  Downloading Pympler-1.0.1-py3-none-any.whl (164 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m164.8/164.8 kB\u001b[0m \u001b[31m17.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: python-dateutil in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.8.2)\n",
            "Requirement already satisfied: requests>=2.4 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.27.1)\n",
            "Requirement already satisfied: rich>=10.11.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (13.3.4)\n",
            "Requirement already satisfied: tenacity<9,>=8.0.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.2.2)\n",
            "Requirement already satisfied: toml in /usr/local/lib/python3.10/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions>=3.10.0.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.5.0)\n",
            "Requirement already satisfied: tzlocal>=1.1 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.3)\n",
            "Collecting validators>=0.2 (from streamlit)\n",
            "  Downloading validators-0.20.0.tar.gz (30 kB)\n",
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "Collecting gitpython!=3.1.19 (from streamlit)\n",
            "  Downloading GitPython-3.1.31-py3-none-any.whl (184 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m184.3/184.3 kB\u001b[0m \u001b[31m20.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting pydeck>=0.1.dev5 (from streamlit)\n",
            "  Downloading pydeck-0.8.1b0-py2.py3-none-any.whl (4.8 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m4.8/4.8 MB\u001b[0m \u001b[31m102.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: tornado>=6.0.3 in /usr/local/lib/python3.10/dist-packages (from streamlit) (6.3.1)\n",
            "Collecting watchdog (from streamlit)\n",
            "  Downloading watchdog-3.0.0-py3-none-manylinux2014_x86_64.whl (82 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m82.1/82.1 kB\u001b[0m \u001b[31m9.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: entrypoints in /usr/local/lib/python3.10/dist-packages (from altair<5,>=3.2.0->streamlit) (0.4)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from altair<5,>=3.2.0->streamlit) (3.1.2)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.10/dist-packages (from altair<5,>=3.2.0->streamlit) (4.3.3)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.10/dist-packages (from altair<5,>=3.2.0->streamlit) (0.12.0)\n",
            "Collecting gitdb<5,>=4.0.1 (from gitpython!=3.1.19->streamlit)\n",
            "  Downloading gitdb-4.0.10-py3-none-any.whl (62 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m62.7/62.7 kB\u001b[0m \u001b[31m8.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.10/dist-packages (from importlib-metadata>=1.4->streamlit) (3.15.0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=0.25->streamlit) (2022.7.1)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil->streamlit) (1.16.0)\n",
            "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.4->streamlit) (1.26.15)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.4->streamlit) (2022.12.7)\n",
            "Requirement already satisfied: charset-normalizer~=2.0.0 in /usr/local/lib/python3.10/dist-packages (from requests>=2.4->streamlit) (2.0.12)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.4->streamlit) (3.4)\n",
            "Requirement already satisfied: markdown-it-py<3.0.0,>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich>=10.11.0->streamlit) (2.2.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich>=10.11.0->streamlit) (2.14.0)\n",
            "Requirement already satisfied: pytz-deprecation-shim in /usr/local/lib/python3.10/dist-packages (from tzlocal>=1.1->streamlit) (0.1.0.post0)\n",
            "Requirement already satisfied: decorator>=3.4.0 in /usr/local/lib/python3.10/dist-packages (from validators>=0.2->streamlit) (4.4.2)\n",
            "Collecting smmap<6,>=3.0.1 (from gitdb<5,>=4.0.1->gitpython!=3.1.19->streamlit)\n",
            "  Downloading smmap-5.0.0-py3-none-any.whl (24 kB)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->altair<5,>=3.2.0->streamlit) (2.1.2)\n",
            "Requirement already satisfied: attrs>=17.4.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<5,>=3.2.0->streamlit) (23.1.0)\n",
            "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<5,>=3.2.0->streamlit) (0.19.3)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py<3.0.0,>=2.2.0->rich>=10.11.0->streamlit) (0.1.2)\n",
            "Requirement already satisfied: tzdata in /usr/local/lib/python3.10/dist-packages (from pytz-deprecation-shim->tzlocal>=1.1->streamlit) (2023.3)\n",
            "Building wheels for collected packages: validators\n",
            "  Building wheel for validators (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for validators: filename=validators-0.20.0-py3-none-any.whl size=19579 sha256=44fbd86eb8882334dcfc9659e398a716974b415889d84862d7c63f5a41c71676\n",
            "  Stored in directory: /root/.cache/pip/wheels/f2/ed/dd/d3a556ad245ef9dc570c6bcd2f22886d17b0b408dd3bbb9ac3\n",
            "Successfully built validators\n",
            "Installing collected packages: watchdog, validators, smmap, pympler, importlib-metadata, blinker, pydeck, gitdb, gitpython, streamlit\n",
            "Successfully installed blinker-1.6.2 gitdb-4.0.10 gitpython-3.1.31 importlib-metadata-6.6.0 pydeck-0.8.1b0 pympler-1.0.1 smmap-5.0.0 streamlit-1.22.0 validators-0.20.0 watchdog-3.0.0\n"
          ]
        }
      ],
      "source": [
        "!pip install streamlit"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install beautifulsoup4"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KOVec6cCNJz5",
        "outputId": "53d329c5-4b30-46f9-d9a9-3cf6cf3417f7"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.10/dist-packages (4.11.2)\n",
            "Requirement already satisfied: soupsieve>1.2 in /usr/local/lib/python3.10/dist-packages (from beautifulsoup4) (2.4.1)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install requests"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1paQd3h-NXfU",
        "outputId": "dcd0f15b-8bfc-4ecd-9b87-8bfbe2de5cd5"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (2.27.1)\n",
            "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests) (1.26.15)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests) (2022.12.7)\n",
            "Requirement already satisfied: charset-normalizer~=2.0.0 in /usr/local/lib/python3.10/dist-packages (from requests) (2.0.12)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests) (3.4)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile app.py\n",
        "import streamlit as st\n",
        "import requests\n",
        "from bs4 import BeautifulSoup\n",
        "\n",
        "def main():\n",
        "    # Create a title for your app\n",
        "    st.title(\"Pixabay Web Scraper\")\n",
        "\n",
        "    # Add an input field to enter the search term\n",
        "    search_term = st.text_input(\"Enter search term\", \"nature\")\n",
        "\n",
        "    # Create a button to initiate the scraping process\n",
        "    if st.button(\"Scrape\"):\n",
        "        # Make a GET request to Pixabay website\n",
        "        response = requests.get(f\"https://pixabay.com/images/search/{search_term}/\")\n",
        "        soup = BeautifulSoup(response.content, \"html.parser\")\n",
        "\n",
        "        # Find and display the images on the page\n",
        "        images = soup.find_all(\"img\", {\"src\": True})\n",
        "        for image in images:\n",
        "            st.image(image[\"src\"])\n",
        "\n",
        "    # Add a footer or any additional information\n",
        "    st.text(\"Web Scraper by Your Name\")\n",
        "\n",
        "# Call the main function directly\n",
        "main()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9t1NWgi-NblN",
        "outputId": "b900c064-6ea3-4029-b08a-9dcf75dfb259"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing app.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!streamlit run app.py"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3UgFiWzKNrIR",
        "outputId": "d38b5b22-c45f-48b9-9039-6a571e912845"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Collecting usage statistics. To deactivate, set browser.gatherUsageStats to False.\n",
            "\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m\u001b[1m  You can now view your Streamlit app in your browser.\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Network URL: \u001b[0m\u001b[1mhttp://172.28.0.12:8501\u001b[0m\n",
            "\u001b[34m  External URL: \u001b[0m\u001b[1mhttp://34.91.168.5:8501\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Stopping...\u001b[0m\n",
            "\u001b[34m  Stopping...\u001b[0m\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install beautifulsoup4"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uKQqHNZ7OBNq",
        "outputId": "02acf720-cbcf-4de0-e245-5230ab9c52f1"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.10/dist-packages (4.11.2)\n",
            "Requirement already satisfied: soupsieve>1.2 in /usr/local/lib/python3.10/dist-packages (from beautifulsoup4) (2.4.1)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!npm install localtunnel"
      ],
      "metadata": {
        "id": "AesCBi6qTsDC",
        "outputId": "879e0044-8a2f-47a5-e4c4-88b362d7dda5",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[K\u001b[?25h\u001b[37;40mnpm\u001b[0m \u001b[0m\u001b[30;43mWARN\u001b[0m \u001b[0m\u001b[35msaveError\u001b[0m ENOENT: no such file or directory, open '/content/package.json'\n",
            "\u001b[K\u001b[?25h\u001b[37;40mnpm\u001b[0m \u001b[0m\u001b[34;40mnotice\u001b[0m\u001b[35m\u001b[0m created a lockfile as package-lock.json. You should commit this file.\n",
            "\u001b[0m\u001b[37;40mnpm\u001b[0m \u001b[0m\u001b[30;43mWARN\u001b[0m \u001b[0m\u001b[35menoent\u001b[0m ENOENT: no such file or directory, open '/content/package.json'\n",
            "\u001b[0m\u001b[37;40mnpm\u001b[0m \u001b[0m\u001b[30;43mWARN\u001b[0m\u001b[35m\u001b[0m content No description\n",
            "\u001b[0m\u001b[37;40mnpm\u001b[0m \u001b[0m\u001b[30;43mWARN\u001b[0m\u001b[35m\u001b[0m content No repository field.\n",
            "\u001b[0m\u001b[37;40mnpm\u001b[0m \u001b[0m\u001b[30;43mWARN\u001b[0m\u001b[35m\u001b[0m content No README data\n",
            "\u001b[0m\u001b[37;40mnpm\u001b[0m \u001b[0m\u001b[30;43mWARN\u001b[0m\u001b[35m\u001b[0m content No license field.\n",
            "\u001b[0m\n",
            "+ localtunnel@2.0.2\n",
            "added 22 packages from 22 contributors and audited 22 packages in 2.098s\n",
            "\n",
            "3 packages are looking for funding\n",
            "  run `npm fund` for details\n",
            "\n",
            "found \u001b[92m0\u001b[0m vulnerabilities\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!streamlit run app.py &>/content/logs.txt &"
      ],
      "metadata": {
        "id": "FDX9k4oTUaqB"
      },
      "execution_count": 12,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!npx localtunnel --port 8501"
      ],
      "metadata": {
        "id": "RQNo2dPbUjHi",
        "outputId": "4dbdb68c-5d0d-4bdb-dced-4d5c5d93b874",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[K\u001b[?25hnpx: installed 22 in 1.87s\n",
            "your url is: https://whole-shirts-drive.loca.lt\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "5xJWhYOxUmre"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}