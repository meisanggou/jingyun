#! /usr/bin/env python
# coding: utf-8

import os
import sys
import yaml
from compose.cli.main import main as compose_main
from jingyun_cli import logger
from jingyun_cli.util.cli_args import args_man, parse_args
try:
    from .help import g_help, error_and_exit
except ValueError:
    from help import g_help, error_and_exit


__author__ = '鹛桑够'


def get_file(compose_dir):
    if compose_dir is None:
        compose_dir = os.environ.get("JINGD_CONF_DIR", ".")
    file_path = os.path.join(compose_dir, "docker-compose.yml")
    return file_path


def write_conf(args):
    if len(sys.argv) <= 1:
        sys.argv.append("-h")
    service_name = args.name
    service_item = dict(image=args.image)
    if args.volumes is not None:
        service_item["volumes"] = args.volumes
    if args.ports is not None:
        service_item["ports"] = args.ports
    if args.restart is not None:
        service_item["restart"] = args.restart
    if args.command is not None:
        service_item["command"] = " ".join(args.command)
    if args.environments is not None:
        service_item["environment"] = args.environments
    if args.working_dir is not None:
        service_item["working_dir"] = args.working_dir
    file_path = get_file(args.compose_dir)
    if os.path.exists(file_path) is False:
        logger.debug(g_help("create", file_path))
        o_y = dict(version='2', services={service_name: service_item})
    else:
        f = open(file_path)
        o_y = yaml.load(f)
        if service_name in o_y["services"]:
            logger.debug(g_help("exist_service"))
        o_y["services"][service_name] = service_item
    w_f = open(file_path, "w")
    yaml.dump(o_y, stream=w_f, default_flow_style=False)


def main():
    commands_man = args_man.add_subparsers(title="Commands", description=None, metavar="COMMAND", dest="sub_cmd")

    config_man = commands_man.add_parser("config", help=g_help("action_config"))
    config_man.add_argument("command", nargs="*", help=g_help("command"))
    config_man.add_argument("-d", dest="compose_dir", help=g_help("compose_dir"))
    config_man.add_argument("-e", "--environment", dest="environments", help=g_help("env"), action="append")
    config_man.add_argument("-f", "--file", dest="file_path", help=g_help("file"))
    config_man.add_argument("-n", "--name", dest="name", help=g_help("name"), required=True)
    config_man.add_argument("-i", "--image", dest="image", help=g_help("image"), required=True)
    config_man.add_argument("-v", "--volumes", dest="volumes", help=g_help("volumes"), action="append")
    config_man.add_argument("-p", "--ports", help=g_help("ports"), action="append")
    config_man.add_argument("--restart", help=g_help("restart"))
    config_man.add_argument("-w", "--working-dir", dest="working_dir", help=g_help("working_dir"))

    # commands_man.add_parser("kill", help="")

    # up_man = commands_man.add_parser("up", help="execute docker-compose up")
    # up_man.add_argument("args", nargs="*")
    if len(sys.argv) <= 1:
        sys.argv.append("-h")
    args = parse_args()
    if args.sub_cmd == "config":
        write_conf(args)
    else:
        file_path = get_file(None)
        sys.argv.insert(1, "-f")
        sys.argv.insert(2, file_path)
        compose_main()


if __name__ == "__main__":
    sys.argv.extend(["--debug", "config", "-n", "qc", "-i", "meisanggou/qc", "-v", "${JINGD_DATA_ROOT}:${JINGD_DATA_ROOT}",
                     "-v", "${JINGD_CONF_DIR}:${JINGD_CONF_DIR}", "-v", "${GATCAPI_DIR}/Worker:/opt/worker", "-w", "/opt/worker", "python", "SampleSequencingLocalWorker.py"])
    main()
