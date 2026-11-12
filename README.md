# VulnTrack Enterprise

VulnTrack Enterprise is an advanced vulnerability and asset compliance tracking platform engineered to secure modern organizational infrastructure. By bridging the gap between hardware asset inventory and real-time Common Vulnerabilities and Exposures (CVE) intelligence, VulnTrack Enterprise empowers security analysts to instantly quantify enterprise risk, prioritize patch deployments, and maintain continuous compliance verification through an intuitive, containerized architecture.

## Installation

To set up and configure the local development environment using Docker and Django, execute the following commands in your terminal:

```bash
docker-compose build
docker-compose run django python manage.py migrate
docker-compose run django python manage.py createsuperuser
