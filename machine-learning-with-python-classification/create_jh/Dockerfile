FROM us.gcr.io/jupyterhub-170614/0636920156154:v1.0

USER root
# notebook and ipykernel should already be installed. now just need jupyterhub
RUN pip install --upgrade --no-cache-dir jupyterhub==0.7.2

USER jovyan

WORKDIR /home/jovyan

# adding oneliner for css stuff
RUN echo "@import url(\"https://cdn.oreillystatic.com/jupyterhub/jupyterhub-theme/custom/custom.css\")" | tee \
/opt/conda/lib/python3.6/site-packages/notebook/static/custom/custom.css \
/opt/conda/pkgs/jupyter_core-4.3.0-py36_0/lib/python3.6/site-packages/jupyter_core/tests/dotipython/profile_default/static/custom/custom.css 

CMD jupyterhub-singleuser \
  --port=8888 \
  --ip=0.0.0.0 \
  --user="$JPY_USER" \
  --cookie-name=$JPY_COOKIE_NAME \
  --base-url=$JPY_BASE_URL \
  --hub-prefix=$JPY_HUB_PREFIX \
  --hub-api-url=$JPY_HUB_API_URL \
