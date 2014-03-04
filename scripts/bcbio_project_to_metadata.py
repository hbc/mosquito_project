import os
from argparse import ArgumentParser
from collections import OrderedDict
import yaml


if __name__ == "__main__":
    description = ("Convert the metadata from bcbio-nextgen project.yaml "
                   "file to a CSV file.")
    parser = ArgumentParser(description)

    parser.add_argument("config",
                        help="bcbio-nextgen project YAML file")
    args = parser.parse_args()

    with open(args.config) as in_handle:
        config = yaml.load(in_handle)["details"]

    metadata_keys = sorted(config[0]["metadata"].keys())
    print ",".join(["samplename", "description"] + metadata_keys)
    for sample in config:
        samplename = os.path.basename(os.path.splitext(sample["files"][0])[0])
        description = sample["description"]
        metadata_values = OrderedDict(sorted(sample["metadata"].items())).values()
        print ",".join([samplename, description] + metadata_values)
