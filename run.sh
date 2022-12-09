#!/bin/bash -ex

flask createdb

flask --debug run
