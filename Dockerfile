FROM alpine:latest

LABEL maintainer="Nick [linickx.com]"
LABEL version="0.1"

# Install
RUN apk update \
    && apk add bash tzdata \
    && rm -rf /var/cache/apk/*

RUN echo "Hello World!"
ENTRYPOINT ["/bin/bash"]