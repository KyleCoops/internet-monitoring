FROM ubuntu:20.04
RUN apt update && apt -y install apt-transport-https gnupg1 dirmngr curl
RUN curl -s https://install.speedtest.net/app/cli/install.deb.sh | bash
RUN apt -y install speedtest
ENTRYPOINT [ "sleep", "1000" ]