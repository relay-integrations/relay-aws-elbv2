FROM relaysh/core:latest-python
RUN pip install --upgrade boto3
COPY "./step.py" "/entrypoint.py"
ENTRYPOINT []
CMD ["python3", "/entrypoint.py"]

LABEL "org.opencontainers.image.title"="Describe AWS ELB v2 targets"
LABEL "org.opencontainers.image.description"="This task describes targets given a list of target groups."
LABEL "com.puppet.nebula.sdk.version"="v1"
