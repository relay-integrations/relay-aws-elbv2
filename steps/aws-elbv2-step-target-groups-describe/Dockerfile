FROM relaysh/core:latest-python
RUN pip install --upgrade boto3
COPY "./step.py" "/entrypoint.py"
ENTRYPOINT []
CMD ["python3", "/entrypoint.py"]

LABEL "org.opencontainers.image.title"="Describe AWS ELB v2 target groups"
LABEL "org.opencontainers.image.description"="This task describes the ELB v2 target groups given a list of load balancers."
LABEL "com.puppet.nebula.sdk.version"="v1"
