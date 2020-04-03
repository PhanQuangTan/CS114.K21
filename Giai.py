{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled3.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyP53z14uJnIOfeLTR6RFoIX",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/PhanQuangTan/CS114.K21/blob/master/Giai.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Pq2c8uj_QOeG",
        "colab_type": "code",
        "outputId": "c2979512-fb06-48a2-813f-e348487add2a",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        }
      },
      "source": [
        "n = int(input(\"Nhập số cần tính giai thừa: \"))\n",
        " \n",
        "def giaiThua(n):\n",
        "    if n == 0:\n",
        "        return 1\n",
        "    return n * giaiThua(n - 1)\n",
        " \n",
        "print (giaiThua(n))"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Nhập số cần tính giai thừa: 4\n",
            "24\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}