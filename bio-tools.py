{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPJ4n/e+pgXfX3cM5k+vW1p",
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
        "<a href=\"https://colab.research.google.com/github/arcPrayagscibio/learning-biotechnology-/blob/main/string%20reverse.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dna = \"TAGCGATCGAATGCATGCATGCATAGCGATCGAATGCATGCATGCA\"\n",
        "s = dna\n",
        "s = s[::-1]\n",
        "print(\"the reverse sequence for this string\",s)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "--WmSF9coPSR",
        "outputId": "25e3014c-b206-48a0-d255-7605e819304d"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "the reverse sequence for this string ACGTACGTACGTAAGCTAGCGATACGTACGTACGTAAGCTAGCGAT\n"
          ]
        }
      ]
    }
  ]
}
