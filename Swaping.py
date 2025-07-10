{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMod4MfqO44xagP4+JmXt+M",
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
        "<a href=\"https://colab.research.google.com/github/ThivaharBalasubramaniam/My-works/blob/main/Swaping.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "y8Yom1lSEYv4",
        "outputId": "8fdea7f6-f8b1-47b5-b526-21b533df7668"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Before swaping a=5b=10\n",
            "after swaping a=10b=5\n"
          ]
        }
      ],
      "source": [
        "a=5\n",
        "b=10\n",
        "print(f\"Before swaping a={a}b={b}\")\n",
        "a=a+b\n",
        "b=a-b\n",
        "a=a-b\n",
        "print(f\"after swaping a={a}b={b}\")"
      ]
    }
  ]
}