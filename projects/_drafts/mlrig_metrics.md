---
layout: post
title: Machine Learning Rig: Metrics
---

# Adding Monitoring and Metrics to my ML rig with Grafana and Prometheus

TODO: Links for Grafana and Prometheus

* Wanted monitoring/Metrics for the ML rig
* Decided to go with Prometheus+Grafana instead of more "out of the box" solutions (like WandBs) because:
  * Have several other machines I want to monitor (RPi's, other servers)
  * Eventually want to make a Grafana dashboard for my partner's fish tank (heat/salinity/pH/etc)
  * Wanted to learn about Grafana and Prometheus
* Added [node-exporter](TODO: Link) to all my machines
  * 3 RPis, 2 servers (including the ML rig), 2 PCs, and two laptops
  * Set up [Ansible](TODO: link to ansible) to install node-exporter
    * Ansible was a bit of a learning detour
    * Eventually set up a [repo I was happy with](TODO: Link to ansible-jerome)
      * Inventory with all my devices
      * All sensitive data in a vault
      * Prometheus package installed via ansible-galaxy
      * Playbook setup for node-exporter
* Set up prometheus + grafana on another server with [docker-compose](TODO: link to my compose file somehow?)
* Set up [prometheus.yml](TODO: link to prometheus.yml somehow) and some grafana dashboard
* This was good - had CPU, RAM, Network, storage metrics for all my machines
* Still missing GPU Metrics!
  * Couldn't find any easy out of the box prometheus clients for AMD GPUs (link to random golang one)
  * TODO: google around for pure CUDA prometheus clients! they will probably work
  * Ended up writing a quick n dirty [rocm prom client](TODO: link to rocm-prom-metrics)
    * Had to make a few patches to rocm-smi
    * Deployed on ml rig manually with systemd units so it starts on boot
* All done! had a play around in JupyterLab to see everything was wired up properly 

TODO: Image of dashboard

