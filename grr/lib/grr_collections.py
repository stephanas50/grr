#!/usr/bin/env python
"""Some collections used in multiple places."""

from grr.lib import output_plugin
from grr.lib import rdfvalue
from grr.lib import sequential_collection
from grr.lib.rdfvalues import anomaly
from grr.lib.rdfvalues import client as rdf_client
from grr.lib.rdfvalues import crypto as rdf_crypto
from grr.lib.rdfvalues import flows as rdf_flows
from grr.lib.rdfvalues import hunts as rdf_hunts


class LogCollection(sequential_collection.IndexedSequentialCollection):
  RDF_TYPE = rdf_flows.FlowLog


class CrashCollection(sequential_collection.IndexedSequentialCollection):
  RDF_TYPE = rdf_client.ClientCrash


class AnomalyCollection(sequential_collection.IndexedSequentialCollection):
  RDF_TYPE = anomaly.Anomaly


class ClientUrnCollection(sequential_collection.IndexedSequentialCollection):
  RDF_TYPE = rdf_client.ClientURN


class RDFUrnCollection(sequential_collection.IndexedSequentialCollection):
  RDF_TYPE = rdfvalue.RDFURN


class HuntErrorCollection(sequential_collection.IndexedSequentialCollection):
  RDF_TYPE = rdf_hunts.HuntError


class PluginStatusCollection(sequential_collection.IndexedSequentialCollection):
  RDF_TYPE = output_plugin.OutputPluginBatchProcessingStatus


class SignedBlobCollection(sequential_collection.IndexedSequentialCollection):
  RDF_TYPE = rdf_crypto.SignedBlob
