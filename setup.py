from setuptools import setup

setup(
    name="st7789vw",
    version="1.0.0",
    description="Python-Treiber 1.3 ST7789VW TFT-Display (Joy-IT kompatibel)",
    author="Joy-IT",
    author_email="service@joy-it.net",
    license="MIT",
    packages=["st7789vw"],
    install_requires=[
        "gpiozero",
        "spidev",
        "numpy",
        "Pillow"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
