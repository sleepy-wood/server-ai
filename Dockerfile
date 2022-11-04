FROM public.ecr.aws/docker/library/python:3.10

WORKDIR /app

COPY pyproject.toml ./
RUN mkdir app && touch app/__init__.py \
    && python -c 'from setuptools import setup; setup()' egg_info \
    && pkgs=$(sed '/^\[/,//d' *.egg-info/requires.txt) \
    && pip install --no-cache-dir $pkgs

COPY . ./
RUN pip install --no-cache-dir  --no-deps -e .

CMD ["app"]
