# Auto generated from alskg_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-06-01T15:34:47
# Schema: alskg_schema
#
# id: https://w3id.org/alskg/schema/alskg-schema
# description: A LinkML schema for ALSKG that extends the OptimusKG semantic model while preserving Neo4j-compatible node classes, relationship classes, and graph semantics. It adds ALS-focused classes and relationships for subtypes, variants, pathogenesis, gene expression, cohorts, samples, assays, evidence, biomarkers, model systems, therapy, and drug repurposing.
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Float, Integer, String
from linkml_runtime.utils.metamodelcore import Bool

metamodel_version = "1.7.0"
version = "0.2.0-alskg-neo4j-extension"

# Namespaces
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
CHEMBL = CurieNamespace('CHEMBL', 'https://www.ebi.ac.uk/chembl/compound_report_card/')
CL = CurieNamespace('CL', 'http://purl.obolibrary.org/obo/CL_')
DOI = CurieNamespace('DOI', 'https://doi.org/')
DOID = CurieNamespace('DOID', 'http://purl.obolibrary.org/obo/DOID_')
DRUGBANK = CurieNamespace('DRUGBANK', 'https://go.drugbank.com/drugs/')
ECO = CurieNamespace('ECO', 'http://purl.obolibrary.org/obo/ECO_')
EFO = CurieNamespace('EFO', 'http://www.ebi.ac.uk/efo/EFO_')
ENSG = CurieNamespace('ENSG', 'https://ensembl.org/id/')
GO = CurieNamespace('GO', 'http://purl.obolibrary.org/obo/GO_')
HGNC = CurieNamespace('HGNC', 'https://identifiers.org/hgnc/')
HP = CurieNamespace('HP', 'http://purl.obolibrary.org/obo/HP_')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
MESH = CurieNamespace('MESH', 'http://id.nlm.nih.gov/mesh/')
MONDO = CurieNamespace('MONDO', 'http://purl.obolibrary.org/obo/MONDO_')
NCBIGENE = CurieNamespace('NCBIGene', 'https://identifiers.org/ncbigene/')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
ORPHANET = CurieNamespace('ORPHANET', 'http://www.orpha.net/ORDO/Orphanet_')
PMID = CurieNamespace('PMID', 'https://pubmed.ncbi.nlm.nih.gov/')
PR = CurieNamespace('PR', 'http://purl.obolibrary.org/obo/PR_')
REACT = CurieNamespace('REACT', 'https://reactome.org/content/detail/')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
RXNORM = CurieNamespace('RXNORM', 'https://www.nlm.nih.gov/research/umls/rxnorm/')
SIO = CurieNamespace('SIO', 'http://semanticscience.org/resource/')
SO = CurieNamespace('SO', 'http://purl.obolibrary.org/obo/SO_')
UBERON = CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_')
UNIPROTKB = CurieNamespace('UniProtKB', 'https://identifiers.org/uniprot/')
ALSKG = CurieNamespace('alskg', 'https://w3id.org/alskg/schema/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
ENSEMBL = CurieNamespace('ensembl', 'https://identifiers.org/ensembl/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OBO = CurieNamespace('obo', 'http://purl.obolibrary.org/obo/')
OKG = CurieNamespace('okg', 'https://w3id.org/optimuskg/schema/')
OPTIMUSKG = CurieNamespace('optimuskg', 'https://optimuskg.ai/schema/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PAV = CurieNamespace('pav', 'http://purl.org/pav/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
UNIPROT = CurieNamespace('uniprot', 'https://purl.uniprot.org/uniprot/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = ALSKG


# Types
class CURIEType(str):
    """ A Compact URI (CURIE) identifier in the form {namespace}[:_]{local_id}. Examples: ENSG00000139618, GO:0000001, HP:0001250, MONDO:0005148. All namespace prefixes are validated against the Biolink Model namespace registry. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "CURIEType"
    type_model_uri = ALSKG.CURIEType


class URIType(str):
    """ A URI or URL stored as a string. """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "URIType"
    type_model_uri = ALSKG.URIType


class Base64StringType(str):
    """ A base64-encoded binary payload stored as a string. Used for mol_file_base64 and mol_image_base64 on Drug nodes. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Base64StringType"
    type_model_uri = ALSKG.Base64StringType


class Probability(Float):
    """ A probability-like score between 0 and 1. """
    type_class_uri = XSD["float"]
    type_class_curie = "xsd:float"
    type_name = "Probability"
    type_model_uri = ALSKG.Probability


# Class references
class NamedEntityId(extended_str):
    pass


class OntologyClassId(NamedEntityId):
    pass


class ClinicalEntityId(NamedEntityId):
    pass


class PhysicalEntityId(NamedEntityId):
    pass


class AnalyticalEntityId(NamedEntityId):
    pass


class AnatomyId(AnalyticalEntityId):
    pass


class BiologicalProcessId(OntologyClassId):
    pass


class CellularComponentId(OntologyClassId):
    pass


class DiseaseId(ClinicalEntityId):
    pass


class DrugId(PhysicalEntityId):
    pass


class ExposureId(PhysicalEntityId):
    pass


class GeneId(PhysicalEntityId):
    pass


class MolecularFunctionId(OntologyClassId):
    pass


class PhenotypeId(ClinicalEntityId):
    pass


class PathwayId(OntologyClassId):
    pass


class OntologyMetadataId(extended_str):
    pass


class ProteinId(PhysicalEntityId):
    pass


class ProteinIsoformId(ProteinId):
    pass


class DatabaseAccessionId(extended_str):
    pass


class DataSourceId(extended_str):
    pass


class PublicationId(extended_str):
    pass


class EvidenceRecordId(extended_str):
    pass


class SynonymId(extended_str):
    pass


class CrossReferenceId(DatabaseAccessionId):
    pass


class AmyotrophicLateralSclerosisId(DiseaseId):
    pass


class DiseaseSubtypeId(ClinicalEntityId):
    pass


class ALSSubtypeId(DiseaseSubtypeId):
    pass


class MolecularSubtypeId(ALSSubtypeId):
    pass


class ClinicalSubtypeId(ALSSubtypeId):
    pass


class GeneticSubtypeId(ALSSubtypeId):
    pass


class PathologySubtypeId(ALSSubtypeId):
    pass


class ProgressionSubtypeId(ALSSubtypeId):
    pass


class SubtypeSchemeId(AnalyticalEntityId):
    pass


class SubtypeCriterionId(AnalyticalEntityId):
    pass


class SequenceVariantId(PhysicalEntityId):
    pass


class RepeatExpansionId(SequenceVariantId):
    pass


class CellTypeId(OntologyClassId):
    pass


class PathogenicMechanismId(AnalyticalEntityId):
    pass


class MolecularEventId(AnalyticalEntityId):
    pass


class ProteinAggregateId(PhysicalEntityId):
    pass


class EvidenceStatementId(AnalyticalEntityId):
    pass


class PathogenesisStatementId(EvidenceStatementId):
    pass


class DifferentialExpressionStatementId(EvidenceStatementId):
    pass


class GeneExpressionContextId(DifferentialExpressionStatementId):
    pass


class ProteinAbundanceResultId(EvidenceStatementId):
    pass


class PhenotypeObservationId(EvidenceStatementId):
    pass


class DiseaseStageId(ClinicalEntityId):
    pass


class ProgressionPatternId(ClinicalEntityId):
    pass


class BiomarkerId(ClinicalEntityId):
    pass


class StudyId(extended_str):
    pass


class DatasetId(extended_str):
    pass


class CohortId(extended_str):
    pass


class ComparatorGroupId(CohortId):
    pass


class SampleId(extended_str):
    pass


class AssayId(extended_str):
    pass


class ModelSystemId(AnalyticalEntityId):
    pass


class TherapeuticInterventionId(ClinicalEntityId):
    pass


class ClinicalTrialId(StudyId):
    pass


class DrugRepurposingHypothesisId(EvidenceStatementId):
    pass


class BiologicalAgentId(ExposureId):
    pass


class ALSKGExtensionGraphId(AnalyticalEntityId):
    pass


class ExternalKnowledgeReferenceId(extended_str):
    pass


@dataclass(repr=False)
class NamedEntity(YAMLRoot):
    """
    Root abstract class for all named entities in OptimusKG. Replaces the former BiomedicalEntity root (v0.3.0).
    Provides core identity slots shared across all four mid-tier branches: OntologyClass, ClinicalEntity,
    PhysicalEntity, and AnalyticalEntity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["NamedThing"]
    class_class_curie: ClassVar[str] = "biolink:NamedThing"
    class_name: ClassVar[str] = "NamedEntity"
    class_model_uri: ClassVar[URIRef] = ALSKG.NamedEntity

    id: Union[str, NamedEntityId] = None
    name: Optional[str] = None
    original_optimus_label: Optional[str] = None
    direct_sources: Optional[Union[str, list[str]]] = empty_list()
    indirect_sources: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedEntityId):
            self.id = NamedEntityId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.original_optimus_label is not None and not isinstance(self.original_optimus_label, str):
            self.original_optimus_label = str(self.original_optimus_label)

        if not isinstance(self.direct_sources, list):
            self.direct_sources = [self.direct_sources] if self.direct_sources is not None else []
        self.direct_sources = [v if isinstance(v, str) else str(v) for v in self.direct_sources]

        if not isinstance(self.indirect_sources, list):
            self.indirect_sources = [self.indirect_sources] if self.indirect_sources is not None else []
        self.indirect_sources = [v if isinstance(v, str) else str(v) for v in self.indirect_sources]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OntologyClass(NamedEntity):
    """
    Abstract mid-tier for entity types grounded in an OBO/OWL ontology or curated pathway database. All subclasses
    carry ontology header metadata (title, version, license, definition) and cross-references. Covers: Anatomy
    (Uberon), BiologicalProcess (GO), CellularComponent (GO), MolecularFunction (GO), Pathway (Reactome).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL["Class"]
    class_class_curie: ClassVar[str] = "owl:Class"
    class_name: ClassVar[str] = "OntologyClass"
    class_model_uri: ClassVar[URIRef] = ALSKG.OntologyClass

    id: Union[str, OntologyClassId] = None
    name: Optional[str] = None
    original_optimus_label: Optional[str] = None
    direct_sources: Optional[Union[str, list[str]]] = empty_list()
    indirect_sources: Optional[Union[str, list[str]]] = empty_list()
    has_synonym: Optional[Union[Union[str, SynonymId], list[Union[str, SynonymId]]]] = empty_list()
    has_cross_reference: Optional[Union[Union[str, DatabaseAccessionId], list[Union[str, DatabaseAccessionId]]]] = empty_list()
    definition: Optional[str] = None
    synonyms: Optional[Union[str, list[str]]] = empty_list()
    xrefs: Optional[Union[str, list[str]]] = empty_list()
    ontology: Optional[Union[str, OntologyMetadataId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.original_optimus_label is not None and not isinstance(self.original_optimus_label, str):
            self.original_optimus_label = str(self.original_optimus_label)

        if not isinstance(self.direct_sources, list):
            self.direct_sources = [self.direct_sources] if self.direct_sources is not None else []
        self.direct_sources = [v if isinstance(v, str) else str(v) for v in self.direct_sources]

        if not isinstance(self.indirect_sources, list):
            self.indirect_sources = [self.indirect_sources] if self.indirect_sources is not None else []
        self.indirect_sources = [v if isinstance(v, str) else str(v) for v in self.indirect_sources]

        if not isinstance(self.has_synonym, list):
            self.has_synonym = [self.has_synonym] if self.has_synonym is not None else []
        self.has_synonym = [v if isinstance(v, SynonymId) else SynonymId(v) for v in self.has_synonym]

        if not isinstance(self.has_cross_reference, list):
            self.has_cross_reference = [self.has_cross_reference] if self.has_cross_reference is not None else []
        self.has_cross_reference = [v if isinstance(v, DatabaseAccessionId) else DatabaseAccessionId(v) for v in self.has_cross_reference]

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        if not isinstance(self.xrefs, list):
            self.xrefs = [self.xrefs] if self.xrefs is not None else []
        self.xrefs = [v if isinstance(v, str) else str(v) for v in self.xrefs]

        if self.ontology is not None and not isinstance(self.ontology, OntologyMetadataId):
            self.ontology = OntologyMetadataId(self.ontology)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ClinicalEntity(NamedEntity):
    """
    Abstract mid-tier for clinical observation categories grounded in disease and phenotype ontologies. Both
    subclasses carry UMLS CUIs, SNOMED CT mappings, and full ontological hierarchy (parents, ancestors, is_leaf).
    Covers: Disease (MONDO, DOID, EFO, Orphanet, NCIT), Phenotype (HPO, MedDRA).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["DiseaseOrPhenotypicFeature"]
    class_class_curie: ClassVar[str] = "biolink:DiseaseOrPhenotypicFeature"
    class_name: ClassVar[str] = "ClinicalEntity"
    class_model_uri: ClassVar[URIRef] = ALSKG.ClinicalEntity

    id: Union[str, ClinicalEntityId] = None
    name: Optional[str] = None
    original_optimus_label: Optional[str] = None
    direct_sources: Optional[Union[str, list[str]]] = empty_list()
    indirect_sources: Optional[Union[str, list[str]]] = empty_list()
    has_synonym: Optional[Union[Union[str, SynonymId], list[Union[str, SynonymId]]]] = empty_list()
    has_cross_reference: Optional[Union[Union[str, DatabaseAccessionId], list[Union[str, DatabaseAccessionId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ClinicalEntityId):
            self.id = ClinicalEntityId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.original_optimus_label is not None and not isinstance(self.original_optimus_label, str):
            self.original_optimus_label = str(self.original_optimus_label)

        if not isinstance(self.direct_sources, list):
            self.direct_sources = [self.direct_sources] if self.direct_sources is not None else []
        self.direct_sources = [v if isinstance(v, str) else str(v) for v in self.direct_sources]

        if not isinstance(self.indirect_sources, list):
            self.indirect_sources = [self.indirect_sources] if self.indirect_sources is not None else []
        self.indirect_sources = [v if isinstance(v, str) else str(v) for v in self.indirect_sources]

        if not isinstance(self.has_synonym, list):
            self.has_synonym = [self.has_synonym] if self.has_synonym is not None else []
        self.has_synonym = [v if isinstance(v, SynonymId) else SynonymId(v) for v in self.has_synonym]

        if not isinstance(self.has_cross_reference, list):
            self.has_cross_reference = [self.has_cross_reference] if self.has_cross_reference is not None else []
        self.has_cross_reference = [v if isinstance(v, DatabaseAccessionId) else DatabaseAccessionId(v) for v in self.has_cross_reference]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhysicalEntity(NamedEntity):
    """
    Abstract mid-tier for physically real, structurally defined entities whose identity is established by a structure
    or sequence database (not by an ontology concept hierarchy). Merges the former MolecularEntity (Gene, Protein) and
    ChemicalEntity (Drug, Exposure) branches into one family. Biolink alignment:
    biolink:ChemicalEntityOrGeneOrGeneProduct covers this combined family. Covers: Gene (ENSG), Protein (UniProt),
    Drug (ChEMBL/DrugBank/RxNorm), Exposure (MeSH/CTD).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ChemicalEntityOrGeneOrGeneProduct"]
    class_class_curie: ClassVar[str] = "biolink:ChemicalEntityOrGeneOrGeneProduct"
    class_name: ClassVar[str] = "PhysicalEntity"
    class_model_uri: ClassVar[URIRef] = ALSKG.PhysicalEntity

    id: Union[str, PhysicalEntityId] = None
    name: Optional[str] = None
    original_optimus_label: Optional[str] = None
    direct_sources: Optional[Union[str, list[str]]] = empty_list()
    indirect_sources: Optional[Union[str, list[str]]] = empty_list()
    has_synonym: Optional[Union[Union[str, SynonymId], list[Union[str, SynonymId]]]] = empty_list()
    has_cross_reference: Optional[Union[Union[str, DatabaseAccessionId], list[Union[str, DatabaseAccessionId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhysicalEntityId):
            self.id = PhysicalEntityId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.original_optimus_label is not None and not isinstance(self.original_optimus_label, str):
            self.original_optimus_label = str(self.original_optimus_label)

        if not isinstance(self.direct_sources, list):
            self.direct_sources = [self.direct_sources] if self.direct_sources is not None else []
        self.direct_sources = [v if isinstance(v, str) else str(v) for v in self.direct_sources]

        if not isinstance(self.indirect_sources, list):
            self.indirect_sources = [self.indirect_sources] if self.indirect_sources is not None else []
        self.indirect_sources = [v if isinstance(v, str) else str(v) for v in self.indirect_sources]

        if not isinstance(self.has_synonym, list):
            self.has_synonym = [self.has_synonym] if self.has_synonym is not None else []
        self.has_synonym = [v if isinstance(v, SynonymId) else SynonymId(v) for v in self.has_synonym]

        if not isinstance(self.has_cross_reference, list):
            self.has_cross_reference = [self.has_cross_reference] if self.has_cross_reference is not None else []
        self.has_cross_reference = [v if isinstance(v, DatabaseAccessionId) else DatabaseAccessionId(v) for v in self.has_cross_reference]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AnalyticalEntity(NamedEntity):
    """
    Abstract mid-tier for entities whose identity is established by a computational analysis rather than an ontology
    or physical database. These are reified analytical findings promoted to named nodes because they accumulate enough
    properties and relationships to warrant first-class graph identity. Covers: MolecularSubtype (transcriptomic
    patient strata, MST label), GeneExpressionContext (reified differential expression findings, ECX label).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["StudyResult"]
    class_class_curie: ClassVar[str] = "biolink:StudyResult"
    class_name: ClassVar[str] = "AnalyticalEntity"
    class_model_uri: ClassVar[URIRef] = ALSKG.AnalyticalEntity

    id: Union[str, AnalyticalEntityId] = None

@dataclass(repr=False)
class Anatomy(AnalyticalEntity):
    """
    An anatomical entity or anatomical region represented in OptimusKG. Current Neo4j label: `ANA`.

    Property detail from OptimusKG source schema: An anatomical structure or tissue node. Represents 13,120 anatomical
    entities (6.9% of nodes) from the Uberon cross-species anatomy ontology. Covers organs, tissues, cell types,
    developmental structures, and systems. Source: Uberon. Node file: nodes/anatomy.parquet
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["AnatomicalEntity"]
    class_class_curie: ClassVar[str] = "biolink:AnatomicalEntity"
    class_name: ClassVar[str] = "Anatomy"
    class_model_uri: ClassVar[URIRef] = ALSKG.Anatomy

    id: Union[str, AnatomyId] = None
    name: Optional[str] = None
    original_optimus_label: Optional[str] = None
    direct_sources: Optional[Union[str, list[str]]] = empty_list()
    indirect_sources: Optional[Union[str, list[str]]] = empty_list()
    has_synonym: Optional[Union[Union[str, SynonymId], list[Union[str, SynonymId]]]] = empty_list()
    has_cross_reference: Optional[Union[Union[str, DatabaseAccessionId], list[Union[str, DatabaseAccessionId]]]] = empty_list()
    definition: Optional[str] = None
    synonyms: Optional[Union[str, list[str]]] = empty_list()
    xrefs: Optional[Union[str, list[str]]] = empty_list()
    ontology: Optional[Union[str, OntologyMetadataId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnatomyId):
            self.id = AnatomyId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.original_optimus_label is not None and not isinstance(self.original_optimus_label, str):
            self.original_optimus_label = str(self.original_optimus_label)

        if not isinstance(self.direct_sources, list):
            self.direct_sources = [self.direct_sources] if self.direct_sources is not None else []
        self.direct_sources = [v if isinstance(v, str) else str(v) for v in self.direct_sources]

        if not isinstance(self.indirect_sources, list):
            self.indirect_sources = [self.indirect_sources] if self.indirect_sources is not None else []
        self.indirect_sources = [v if isinstance(v, str) else str(v) for v in self.indirect_sources]

        if not isinstance(self.has_synonym, list):
            self.has_synonym = [self.has_synonym] if self.has_synonym is not None else []
        self.has_synonym = [v if isinstance(v, SynonymId) else SynonymId(v) for v in self.has_synonym]

        if not isinstance(self.has_cross_reference, list):
            self.has_cross_reference = [self.has_cross_reference] if self.has_cross_reference is not None else []
        self.has_cross_reference = [v if isinstance(v, DatabaseAccessionId) else DatabaseAccessionId(v) for v in self.has_cross_reference]

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        if not isinstance(self.xrefs, list):
            self.xrefs = [self.xrefs] if self.xrefs is not None else []
        self.xrefs = [v if isinstance(v, str) else str(v) for v in self.xrefs]

        if self.ontology is not None and not isinstance(self.ontology, OntologyMetadataId):
            self.ontology = OntologyMetadataId(self.ontology)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiologicalProcess(OntologyClass):
    """
    A Gene Ontology biological process term represented in OptimusKG. Current Neo4j label: `BPO`.

    Property detail from OptimusKG source schema: A Gene Ontology (GO) biological process node. Represents 25,754
    biological processes (13.5% of nodes) describing coordinated programs of molecular activities with a defined
    beginning and end (e.g. "apoptotic process", "DNA repair", "cell division"). Source: Gene Ontology (GO). Node
    file: nodes/biological_process.parquet
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["BiologicalProcess"]
    class_class_curie: ClassVar[str] = "biolink:BiologicalProcess"
    class_name: ClassVar[str] = "BiologicalProcess"
    class_model_uri: ClassVar[URIRef] = ALSKG.BiologicalProcess

    id: Union[str, BiologicalProcessId] = None
    name: Optional[str] = None
    original_optimus_label: Optional[str] = None
    direct_sources: Optional[Union[str, list[str]]] = empty_list()
    indirect_sources: Optional[Union[str, list[str]]] = empty_list()
    has_synonym: Optional[Union[Union[str, SynonymId], list[Union[str, SynonymId]]]] = empty_list()
    has_cross_reference: Optional[Union[Union[str, DatabaseAccessionId], list[Union[str, DatabaseAccessionId]]]] = empty_list()
    definition: Optional[str] = None
    synonyms: Optional[Union[str, list[str]]] = empty_list()
    xrefs: Optional[Union[str, list[str]]] = empty_list()
    ontology: Optional[Union[str, OntologyMetadataId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiologicalProcessId):
            self.id = BiologicalProcessId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.original_optimus_label is not None and not isinstance(self.original_optimus_label, str):
            self.original_optimus_label = str(self.original_optimus_label)

        if not isinstance(self.direct_sources, list):
            self.direct_sources = [self.direct_sources] if self.direct_sources is not None else []
        self.direct_sources = [v if isinstance(v, str) else str(v) for v in self.direct_sources]

        if not isinstance(self.indirect_sources, list):
            self.indirect_sources = [self.indirect_sources] if self.indirect_sources is not None else []
        self.indirect_sources = [v if isinstance(v, str) else str(v) for v in self.indirect_sources]

        if not isinstance(self.has_synonym, list):
            self.has_synonym = [self.has_synonym] if self.has_synonym is not None else []
        self.has_synonym = [v if isinstance(v, SynonymId) else SynonymId(v) for v in self.has_synonym]

        if not isinstance(self.has_cross_reference, list):
            self.has_cross_reference = [self.has_cross_reference] if self.has_cross_reference is not None else []
        self.has_cross_reference = [v if isinstance(v, DatabaseAccessionId) else DatabaseAccessionId(v) for v in self.has_cross_reference]

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        if not isinstance(self.xrefs, list):
            self.xrefs = [self.xrefs] if self.xrefs is not None else []
        self.xrefs = [v if isinstance(v, str) else str(v) for v in self.xrefs]

        if self.ontology is not None and not isinstance(self.ontology, OntologyMetadataId):
            self.ontology = OntologyMetadataId(self.ontology)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CellularComponent(OntologyClass):
    """
    A Gene Ontology cellular component term represented in OptimusKG. Current Neo4j label: `CCO`.

    Property detail from OptimusKG source schema: A Gene Ontology (GO) cellular component node. Represents 4,052
    subcellular structures and compartments (2.1% of nodes) where gene products are active or located (e.g. "nucleus",
    "mitochondria", "plasma membrane", "ribosome"). Source: Gene Ontology (GO). Node file:
    nodes/cellular_component.parquet
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["CellularComponent"]
    class_class_curie: ClassVar[str] = "biolink:CellularComponent"
    class_name: ClassVar[str] = "CellularComponent"
    class_model_uri: ClassVar[URIRef] = ALSKG.CellularComponent

    id: Union[str, CellularComponentId] = None
    name: Optional[str] = None
    original_optimus_label: Optional[str] = None
    direct_sources: Optional[Union[str, list[str]]] = empty_list()
    indirect_sources: Optional[Union[str, list[str]]] = empty_list()
    has_synonym: Optional[Union[Union[str, SynonymId], list[Union[str, SynonymId]]]] = empty_list()
    has_cross_reference: Optional[Union[Union[str, DatabaseAccessionId], list[Union[str, DatabaseAccessionId]]]] = empty_list()
    definition: Optional[str] = None
    synonyms: Optional[Union[str, list[str]]] = empty_list()
    xrefs: Optional[Union[str, list[str]]] = empty_list()
    ontology: Optional[Union[str, OntologyMetadataId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellularComponentId):
            self.id = CellularComponentId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.original_optimus_label is not None and not isinstance(self.original_optimus_label, str):
            self.original_optimus_label = str(self.original_optimus_label)

        if not isinstance(self.direct_sources, list):
            self.direct_sources = [self.direct_sources] if self.direct_sources is not None else []
        self.direct_sources = [v if isinstance(v, str) else str(v) for v in self.direct_sources]

        if not isinstance(self.indirect_sources, list):
            self.indirect_sources = [self.indirect_sources] if self.indirect_sources is not None else []
        self.indirect_sources = [v if isinstance(v, str) else str(v) for v in self.indirect_sources]

        if not isinstance(self.has_synonym, list):
            self.has_synonym = [self.has_synonym] if self.has_synonym is not None else []
        self.has_synonym = [v if isinstance(v, SynonymId) else SynonymId(v) for v in self.has_synonym]

        if not isinstance(self.has_cross_reference, list):
            self.has_cross_reference = [self.has_cross_reference] if self.has_cross_reference is not None else []
        self.has_cross_reference = [v if isinstance(v, DatabaseAccessionId) else DatabaseAccessionId(v) for v in self.has_cross_reference]

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        if not isinstance(self.xrefs, list):
            self.xrefs = [self.xrefs] if self.xrefs is not None else []
        self.xrefs = [v if isinstance(v, str) else str(v) for v in self.xrefs]

        if self.ontology is not None and not isinstance(self.ontology, OntologyMetadataId):
            self.ontology = OntologyMetadataId(self.ontology)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Disease(ClinicalEntity):
    """
    A disease, disorder, or clinical condition represented in OptimusKG. Current Neo4j label: `DIS`.

    Property detail from OptimusKG source schema: A human disease node. Represents 36,345 diseases (19.1% of nodes)
    spanning genetic, infectious, cancer, environmental, complex, rare, and common human diseases. Harmonized across
    MONDO, DOID, EFO, Orphanet, NCIT, and other ontologies with full hierarchical structure. Sources: DrugCentral,
    Mondo, Open Targets. Node file: nodes/disease.parquet
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Disease"]
    class_class_curie: ClassVar[str] = "biolink:Disease"
    class_name: ClassVar[str] = "Disease"
    class_model_uri: ClassVar[URIRef] = ALSKG.Disease

    id: Union[str, DiseaseId] = None
    name: Optional[str] = None
    original_optimus_label: Optional[str] = None
    direct_sources: Optional[Union[str, list[str]]] = empty_list()
    indirect_sources: Optional[Union[str, list[str]]] = empty_list()
    has_synonym: Optional[Union[Union[str, SynonymId], list[Union[str, SynonymId]]]] = empty_list()
    has_cross_reference: Optional[Union[Union[str, DatabaseAccessionId], list[Union[str, DatabaseAccessionId]]]] = empty_list()
    disease_has_molecular_subtype: Optional[Union[str, MolecularSubtypeId]] = None
    has_als_subtype: Optional[Union[Union[str, ALSSubtypeId], list[Union[str, ALSSubtypeId]]]] = empty_list()
    has_pathogenic_mechanism: Optional[Union[Union[str, PathogenicMechanismId], list[Union[str, PathogenicMechanismId]]]] = empty_list()
    has_phenotype_observation: Optional[Union[Union[str, PhenotypeObservationId], list[Union[str, PhenotypeObservationId]]]] = empty_list()
    affects_anatomy: Optional[Union[Union[str, AnatomyId], list[Union[str, AnatomyId]]]] = empty_list()
    involves_cell_type: Optional[Union[Union[str, CellTypeId], list[Union[str, CellTypeId]]]] = empty_list()
    disease_has_als_subtype: Optional[Union[str, ALSSubtypeId]] = None
    description: Optional[str] = None
    code: Optional[str] = None
    parents: Optional[Union[str, list[str]]] = empty_list()
    children: Optional[Union[str, list[str]]] = empty_list()
    ancestors: Optional[Union[str, list[str]]] = empty_list()
    descendants: Optional[Union[str, list[str]]] = empty_list()
    is_leaf: Optional[Union[bool, Bool]] = None
    exact_synonyms: Optional[Union[str, list[str]]] = empty_list()
    related_synonyms: Optional[Union[str, list[str]]] = empty_list()
    narrow_synonyms: Optional[Union[str, list[str]]] = empty_list()
    broad_synonyms: Optional[Union[str, list[str]]] = empty_list()
    obsolete_terms: Optional[Union[str, list[str]]] = empty_list()
    obsolete_xrefs: Optional[Union[str, list[str]]] = empty_list()
    xrefs: Optional[Union[str, list[str]]] = empty_list()
    concept_ids: Optional[Union[str, list[str]]] = empty_list()
    concept_names: Optional[Union[str, list[str]]] = empty_list()
    umls_cui: Optional[str] = None
    snomed_full_names: Optional[Union[str, list[str]]] = empty_list()
    snomed_concept_ids: Optional[Union[str, list[str]]] = empty_list()
    cui_semantic_type: Optional[str] = None
    therapeutic_areas: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiseaseId):
            self.id = DiseaseId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.original_optimus_label is not None and not isinstance(self.original_optimus_label, str):
            self.original_optimus_label = str(self.original_optimus_label)

        if not isinstance(self.direct_sources, list):
            self.direct_sources = [self.direct_sources] if self.direct_sources is not None else []
        self.direct_sources = [v if isinstance(v, str) else str(v) for v in self.direct_sources]

        if not isinstance(self.indirect_sources, list):
            self.indirect_sources = [self.indirect_sources] if self.indirect_sources is not None else []
        self.indirect_sources = [v if isinstance(v, str) else str(v) for v in self.indirect_sources]

        if not isinstance(self.has_synonym, list):
            self.has_synonym = [self.has_synonym] if self.has_synonym is not None else []
        self.has_synonym = [v if isinstance(v, SynonymId) else SynonymId(v) for v in self.has_synonym]

        if not isinstance(self.has_cross_reference, list):
            self.has_cross_reference = [self.has_cross_reference] if self.has_cross_reference is not None else []
        self.has_cross_reference = [v if isinstance(v, DatabaseAccessionId) else DatabaseAccessionId(v) for v in self.has_cross_reference]

        if self.disease_has_molecular_subtype is not None and not isinstance(self.disease_has_molecular_subtype, MolecularSubtypeId):
            self.disease_has_molecular_subtype = MolecularSubtypeId(self.disease_has_molecular_subtype)

        if not isinstance(self.has_als_subtype, list):
            self.has_als_subtype = [self.has_als_subtype] if self.has_als_subtype is not None else []
        self.has_als_subtype = [v if isinstance(v, ALSSubtypeId) else ALSSubtypeId(v) for v in self.has_als_subtype]

        if not isinstance(self.has_pathogenic_mechanism, list):
            self.has_pathogenic_mechanism = [self.has_pathogenic_mechanism] if self.has_pathogenic_mechanism is not None else []
        self.has_pathogenic_mechanism = [v if isinstance(v, PathogenicMechanismId) else PathogenicMechanismId(v) for v in self.has_pathogenic_mechanism]

        if not isinstance(self.has_phenotype_observation, list):
            self.has_phenotype_observation = [self.has_phenotype_observation] if self.has_phenotype_observation is not None else []
        self.has_phenotype_observation = [v if isinstance(v, PhenotypeObservationId) else PhenotypeObservationId(v) for v in self.has_phenotype_observation]

        if not isinstance(self.affects_anatomy, list):
            self.affects_anatomy = [self.affects_anatomy] if self.affects_anatomy is not None else []
        self.affects_anatomy = [v if isinstance(v, AnatomyId) else AnatomyId(v) for v in self.affects_anatomy]

        if not isinstance(self.involves_cell_type, list):
            self.involves_cell_type = [self.involves_cell_type] if self.involves_cell_type is not None else []
        self.involves_cell_type = [v if isinstance(v, CellTypeId) else CellTypeId(v) for v in self.involves_cell_type]

        if self.disease_has_als_subtype is not None and not isinstance(self.disease_has_als_subtype, ALSSubtypeId):
            self.disease_has_als_subtype = ALSSubtypeId(self.disease_has_als_subtype)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.code is not None and not isinstance(self.code, str):
            self.code = str(self.code)

        if not isinstance(self.parents, list):
            self.parents = [self.parents] if self.parents is not None else []
        self.parents = [v if isinstance(v, str) else str(v) for v in self.parents]

        if not isinstance(self.children, list):
            self.children = [self.children] if self.children is not None else []
        self.children = [v if isinstance(v, str) else str(v) for v in self.children]

        if not isinstance(self.ancestors, list):
            self.ancestors = [self.ancestors] if self.ancestors is not None else []
        self.ancestors = [v if isinstance(v, str) else str(v) for v in self.ancestors]

        if not isinstance(self.descendants, list):
            self.descendants = [self.descendants] if self.descendants is not None else []
        self.descendants = [v if isinstance(v, str) else str(v) for v in self.descendants]

        if self.is_leaf is not None and not isinstance(self.is_leaf, Bool):
            self.is_leaf = Bool(self.is_leaf)

        if not isinstance(self.exact_synonyms, list):
            self.exact_synonyms = [self.exact_synonyms] if self.exact_synonyms is not None else []
        self.exact_synonyms = [v if isinstance(v, str) else str(v) for v in self.exact_synonyms]

        if not isinstance(self.related_synonyms, list):
            self.related_synonyms = [self.related_synonyms] if self.related_synonyms is not None else []
        self.related_synonyms = [v if isinstance(v, str) else str(v) for v in self.related_synonyms]

        if not isinstance(self.narrow_synonyms, list):
            self.narrow_synonyms = [self.narrow_synonyms] if self.narrow_synonyms is not None else []
        self.narrow_synonyms = [v if isinstance(v, str) else str(v) for v in self.narrow_synonyms]

        if not isinstance(self.broad_synonyms, list):
            self.broad_synonyms = [self.broad_synonyms] if self.broad_synonyms is not None else []
        self.broad_synonyms = [v if isinstance(v, str) else str(v) for v in self.broad_synonyms]

        if not isinstance(self.obsolete_terms, list):
            self.obsolete_terms = [self.obsolete_terms] if self.obsolete_terms is not None else []
        self.obsolete_terms = [v if isinstance(v, str) else str(v) for v in self.obsolete_terms]

        if not isinstance(self.obsolete_xrefs, list):
            self.obsolete_xrefs = [self.obsolete_xrefs] if self.obsolete_xrefs is not None else []
        self.obsolete_xrefs = [v if isinstance(v, str) else str(v) for v in self.obsolete_xrefs]

        if not isinstance(self.xrefs, list):
            self.xrefs = [self.xrefs] if self.xrefs is not None else []
        self.xrefs = [v if isinstance(v, str) else str(v) for v in self.xrefs]

        if not isinstance(self.concept_ids, list):
            self.concept_ids = [self.concept_ids] if self.concept_ids is not None else []
        self.concept_ids = [v if isinstance(v, str) else str(v) for v in self.concept_ids]

        if not isinstance(self.concept_names, list):
            self.concept_names = [self.concept_names] if self.concept_names is not None else []
        self.concept_names = [v if isinstance(v, str) else str(v) for v in self.concept_names]

        if self.umls_cui is not None and not isinstance(self.umls_cui, str):
            self.umls_cui = str(self.umls_cui)

        if not isinstance(self.snomed_full_names, list):
            self.snomed_full_names = [self.snomed_full_names] if self.snomed_full_names is not None else []
        self.snomed_full_names = [v if isinstance(v, str) else str(v) for v in self.snomed_full_names]

        if not isinstance(self.snomed_concept_ids, list):
            self.snomed_concept_ids = [self.snomed_concept_ids] if self.snomed_concept_ids is not None else []
        self.snomed_concept_ids = [v if isinstance(v, str) else str(v) for v in self.snomed_concept_ids]

        if self.cui_semantic_type is not None and not isinstance(self.cui_semantic_type, str):
            self.cui_semantic_type = str(self.cui_semantic_type)

        if not isinstance(self.therapeutic_areas, list):
            self.therapeutic_areas = [self.therapeutic_areas] if self.therapeutic_areas is not None else []
        self.therapeutic_areas = [v if isinstance(v, str) else str(v) for v in self.therapeutic_areas]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Drug(PhysicalEntity):
    """
    A drug, compound, or therapeutic agent represented in OptimusKG. Current Neo4j label: `DRG`.

    Property detail from OptimusKG source schema: A pharmacological compound node. Represents 16,766 drugs (8.8% of
    nodes) including approved drugs, investigational compounds, and biologics. Integrates chemical, regulatory, and
    clinical metadata from DrugBank, DrugCentral, OnSIDES, and Open Targets. Primary ontologies: ChEMBL, DrugBank,
    RxNorm. Node file: nodes/drug.parquet
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Drug"]
    class_class_curie: ClassVar[str] = "biolink:Drug"
    class_name: ClassVar[str] = "Drug"
    class_model_uri: ClassVar[URIRef] = ALSKG.Drug

    id: Union[str, DrugId] = None
    name: Optional[str] = None
    original_optimus_label: Optional[str] = None
    direct_sources: Optional[Union[str, list[str]]] = empty_list()
    indirect_sources: Optional[Union[str, list[str]]] = empty_list()
    has_synonym: Optional[Union[Union[str, SynonymId], list[Union[str, SynonymId]]]] = empty_list()
    has_cross_reference: Optional[Union[Union[str, DatabaseAccessionId], list[Union[str, DatabaseAccessionId]]]] = empty_list()
    modulates_pathogenic_mechanism: Optional[Union[Union[str, PathogenicMechanismId], list[Union[str, PathogenicMechanismId]]]] = empty_list()
    targets_gene: Optional[Union[Union[str, GeneId], list[Union[str, GeneId]]]] = empty_list()
    targets_protein: Optional[Union[Union[str, ProteinId], list[Union[str, ProteinId]]]] = empty_list()
    type: Optional[str] = None
    description: Optional[str] = None
    synonyms: Optional[Union[str, list[str]]] = empty_list()
    source_ids: Optional[Union[str, list[str]]] = empty_list()
    trade_names: Optional[Union[str, list[str]]] = empty_list()
    accession_numbers: Optional[Union[str, list[str]]] = empty_list()
    inchi_key: Optional[str] = None
    cd_formula: Optional[str] = None
    is_approved: Optional[Union[bool, Bool]] = None
    has_been_withdrawn: Optional[Union[bool, Bool]] = None
    black_box_warning: Optional[Union[bool, Bool]] = None
    year_of_first_approval: Optional[int] = None
    maximum_clinical_trial_phase: Optional[float] = None
    status: Optional[str] = None
    chemical_abstracts_service_number: Optional[str] = None
    unique_ingredient_identifier: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DrugId):
            self.id = DrugId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.original_optimus_label is not None and not isinstance(self.original_optimus_label, str):
            self.original_optimus_label = str(self.original_optimus_label)

        if not isinstance(self.direct_sources, list):
            self.direct_sources = [self.direct_sources] if self.direct_sources is not None else []
        self.direct_sources = [v if isinstance(v, str) else str(v) for v in self.direct_sources]

        if not isinstance(self.indirect_sources, list):
            self.indirect_sources = [self.indirect_sources] if self.indirect_sources is not None else []
        self.indirect_sources = [v if isinstance(v, str) else str(v) for v in self.indirect_sources]

        if not isinstance(self.has_synonym, list):
            self.has_synonym = [self.has_synonym] if self.has_synonym is not None else []
        self.has_synonym = [v if isinstance(v, SynonymId) else SynonymId(v) for v in self.has_synonym]

        if not isinstance(self.has_cross_reference, list):
            self.has_cross_reference = [self.has_cross_reference] if self.has_cross_reference is not None else []
        self.has_cross_reference = [v if isinstance(v, DatabaseAccessionId) else DatabaseAccessionId(v) for v in self.has_cross_reference]

        if not isinstance(self.modulates_pathogenic_mechanism, list):
            self.modulates_pathogenic_mechanism = [self.modulates_pathogenic_mechanism] if self.modulates_pathogenic_mechanism is not None else []
        self.modulates_pathogenic_mechanism = [v if isinstance(v, PathogenicMechanismId) else PathogenicMechanismId(v) for v in self.modulates_pathogenic_mechanism]

        if not isinstance(self.targets_gene, list):
            self.targets_gene = [self.targets_gene] if self.targets_gene is not None else []
        self.targets_gene = [v if isinstance(v, GeneId) else GeneId(v) for v in self.targets_gene]

        if not isinstance(self.targets_protein, list):
            self.targets_protein = [self.targets_protein] if self.targets_protein is not None else []
        self.targets_protein = [v if isinstance(v, ProteinId) else ProteinId(v) for v in self.targets_protein]

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        if not isinstance(self.source_ids, list):
            self.source_ids = [self.source_ids] if self.source_ids is not None else []
        self.source_ids = [v if isinstance(v, str) else str(v) for v in self.source_ids]

        if not isinstance(self.trade_names, list):
            self.trade_names = [self.trade_names] if self.trade_names is not None else []
        self.trade_names = [v if isinstance(v, str) else str(v) for v in self.trade_names]

        if not isinstance(self.accession_numbers, list):
            self.accession_numbers = [self.accession_numbers] if self.accession_numbers is not None else []
        self.accession_numbers = [v if isinstance(v, str) else str(v) for v in self.accession_numbers]

        if self.inchi_key is not None and not isinstance(self.inchi_key, str):
            self.inchi_key = str(self.inchi_key)

        if self.cd_formula is not None and not isinstance(self.cd_formula, str):
            self.cd_formula = str(self.cd_formula)

        if self.is_approved is not None and not isinstance(self.is_approved, Bool):
            self.is_approved = Bool(self.is_approved)

        if self.has_been_withdrawn is not None and not isinstance(self.has_been_withdrawn, Bool):
            self.has_been_withdrawn = Bool(self.has_been_withdrawn)

        if self.black_box_warning is not None and not isinstance(self.black_box_warning, Bool):
            self.black_box_warning = Bool(self.black_box_warning)

        if self.year_of_first_approval is not None and not isinstance(self.year_of_first_approval, int):
            self.year_of_first_approval = int(self.year_of_first_approval)

        if self.maximum_clinical_trial_phase is not None and not isinstance(self.maximum_clinical_trial_phase, float):
            self.maximum_clinical_trial_phase = float(self.maximum_clinical_trial_phase)

        if self.status is not None and not isinstance(self.status, str):
            self.status = str(self.status)

        if self.chemical_abstracts_service_number is not None and not isinstance(self.chemical_abstracts_service_number, str):
            self.chemical_abstracts_service_number = str(self.chemical_abstracts_service_number)

        if self.unique_ingredient_identifier is not None and not isinstance(self.unique_ingredient_identifier, str):
            self.unique_ingredient_identifier = str(self.unique_ingredient_identifier)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Exposure(PhysicalEntity):
    """
    An environmental, chemical, lifestyle, or other exposure concept represented in OptimusKG. Current Neo4j label:
    `EXP`.

    Property detail from OptimusKG source schema: A chemical, physical, or environmental exposure node. Represents 881
    exposures (0.5% of nodes) linked to biological outcomes via CTD (Comparative Toxicogenomics Database). Covers
    chemical exposures, physical agents, dietary factors, and lifestyle exposures. Source: Comparative Toxicogenomics
    Database (CTD). Node file: nodes/exposure.parquet
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["EnvironmentalExposure"]
    class_class_curie: ClassVar[str] = "biolink:EnvironmentalExposure"
    class_name: ClassVar[str] = "Exposure"
    class_model_uri: ClassVar[URIRef] = ALSKG.Exposure

    id: Union[str, ExposureId] = None
    name: Optional[str] = None
    original_optimus_label: Optional[str] = None
    direct_sources: Optional[Union[str, list[str]]] = empty_list()
    indirect_sources: Optional[Union[str, list[str]]] = empty_list()
    has_synonym: Optional[Union[Union[str, SynonymId], list[Union[str, SynonymId]]]] = empty_list()
    has_cross_reference: Optional[Union[Union[str, DatabaseAccessionId], list[Union[str, DatabaseAccessionId]]]] = empty_list()
    source_categories: Optional[Union[str, list[str]]] = empty_list()
    source_details: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExposureId):
            self.id = ExposureId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.original_optimus_label is not None and not isinstance(self.original_optimus_label, str):
            self.original_optimus_label = str(self.original_optimus_label)

        if not isinstance(self.direct_sources, list):
            self.direct_sources = [self.direct_sources] if self.direct_sources is not None else []
        self.direct_sources = [v if isinstance(v, str) else str(v) for v in self.direct_sources]

        if not isinstance(self.indirect_sources, list):
            self.indirect_sources = [self.indirect_sources] if self.indirect_sources is not None else []
        self.indirect_sources = [v if isinstance(v, str) else str(v) for v in self.indirect_sources]

        if not isinstance(self.has_synonym, list):
            self.has_synonym = [self.has_synonym] if self.has_synonym is not None else []
        self.has_synonym = [v if isinstance(v, SynonymId) else SynonymId(v) for v in self.has_synonym]

        if not isinstance(self.has_cross_reference, list):
            self.has_cross_reference = [self.has_cross_reference] if self.has_cross_reference is not None else []
        self.has_cross_reference = [v if isinstance(v, DatabaseAccessionId) else DatabaseAccessionId(v) for v in self.has_cross_reference]

        if not isinstance(self.source_categories, list):
            self.source_categories = [self.source_categories] if self.source_categories is not None else []
        self.source_categories = [v if isinstance(v, str) else str(v) for v in self.source_categories]

        if self.source_details is not None and not isinstance(self.source_details, str):
            self.source_details = str(self.source_details)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Gene(PhysicalEntity):
    """
    A gene or gene-level biological entity represented in OptimusKG. Current Neo4j label: `GEN`.

    Property detail from OptimusKG source schema: A protein-coding or non-coding gene node. Represents 61,306 human
    genes (32.2% of nodes) from Ensembl, harmonized with HGNC approved symbols. Contains rich molecular, functional,
    pharmacological, and clinical metadata sourced from Open Targets, DisGeNET, Bgee, and HGNC. Primary ontologies:
    ENSG (Ensembl Gene IDs), NCBIGene. Node file: nodes/gene.parquet
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Gene"]
    class_class_curie: ClassVar[str] = "biolink:Gene"
    class_name: ClassVar[str] = "Gene"
    class_model_uri: ClassVar[URIRef] = ALSKG.Gene

    id: Union[str, GeneId] = None
    name: Optional[str] = None
    symbol: Optional[str] = None
    original_optimus_label: Optional[str] = None
    direct_sources: Optional[Union[str, list[str]]] = empty_list()
    indirect_sources: Optional[Union[str, list[str]]] = empty_list()
    encodes: Optional[Union[Union[str, ProteinId], list[Union[str, ProteinId]]]] = empty_list()
    has_synonym: Optional[Union[Union[str, SynonymId], list[Union[str, SynonymId]]]] = empty_list()
    has_cross_reference: Optional[Union[Union[str, DatabaseAccessionId], list[Union[str, DatabaseAccessionId]]]] = empty_list()
    gene_has_expression_context: Optional[Union[str, GeneExpressionContextId]] = None
    has_variant: Optional[Union[Union[str, SequenceVariantId], list[Union[str, SequenceVariantId]]]] = empty_list()
    contributes_to_pathogenic_mechanism: Optional[Union[Union[str, PathogenicMechanismId], list[Union[str, PathogenicMechanismId]]]] = empty_list()
    has_expression_result: Optional[Union[Union[str, DifferentialExpressionStatementId], list[Union[str, DifferentialExpressionStatementId]]]] = empty_list()
    gene_has_variant: Optional[Union[str, SequenceVariantId]] = None
    gene_contributes_to_pathogenic_mechanism: Optional[Union[str, PathogenicMechanismId]] = None
    biotype: Optional[Union[str, "GeneBiotypeEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneId):
            self.id = GeneId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.symbol is not None and not isinstance(self.symbol, str):
            self.symbol = str(self.symbol)

        if self.original_optimus_label is not None and not isinstance(self.original_optimus_label, str):
            self.original_optimus_label = str(self.original_optimus_label)

        if not isinstance(self.direct_sources, list):
            self.direct_sources = [self.direct_sources] if self.direct_sources is not None else []
        self.direct_sources = [v if isinstance(v, str) else str(v) for v in self.direct_sources]

        if not isinstance(self.indirect_sources, list):
            self.indirect_sources = [self.indirect_sources] if self.indirect_sources is not None else []
        self.indirect_sources = [v if isinstance(v, str) else str(v) for v in self.indirect_sources]

        if not isinstance(self.encodes, list):
            self.encodes = [self.encodes] if self.encodes is not None else []
        self.encodes = [v if isinstance(v, ProteinId) else ProteinId(v) for v in self.encodes]

        if not isinstance(self.has_synonym, list):
            self.has_synonym = [self.has_synonym] if self.has_synonym is not None else []
        self.has_synonym = [v if isinstance(v, SynonymId) else SynonymId(v) for v in self.has_synonym]

        if not isinstance(self.has_cross_reference, list):
            self.has_cross_reference = [self.has_cross_reference] if self.has_cross_reference is not None else []
        self.has_cross_reference = [v if isinstance(v, DatabaseAccessionId) else DatabaseAccessionId(v) for v in self.has_cross_reference]

        if self.gene_has_expression_context is not None and not isinstance(self.gene_has_expression_context, GeneExpressionContextId):
            self.gene_has_expression_context = GeneExpressionContextId(self.gene_has_expression_context)

        if not isinstance(self.has_variant, list):
            self.has_variant = [self.has_variant] if self.has_variant is not None else []
        self.has_variant = [v if isinstance(v, SequenceVariantId) else SequenceVariantId(v) for v in self.has_variant]

        if not isinstance(self.contributes_to_pathogenic_mechanism, list):
            self.contributes_to_pathogenic_mechanism = [self.contributes_to_pathogenic_mechanism] if self.contributes_to_pathogenic_mechanism is not None else []
        self.contributes_to_pathogenic_mechanism = [v if isinstance(v, PathogenicMechanismId) else PathogenicMechanismId(v) for v in self.contributes_to_pathogenic_mechanism]

        if not isinstance(self.has_expression_result, list):
            self.has_expression_result = [self.has_expression_result] if self.has_expression_result is not None else []
        self.has_expression_result = [v if isinstance(v, DifferentialExpressionStatementId) else DifferentialExpressionStatementId(v) for v in self.has_expression_result]

        if self.gene_has_variant is not None and not isinstance(self.gene_has_variant, SequenceVariantId):
            self.gene_has_variant = SequenceVariantId(self.gene_has_variant)

        if self.gene_contributes_to_pathogenic_mechanism is not None and not isinstance(self.gene_contributes_to_pathogenic_mechanism, PathogenicMechanismId):
            self.gene_contributes_to_pathogenic_mechanism = PathogenicMechanismId(self.gene_contributes_to_pathogenic_mechanism)

        if self.biotype is not None and not isinstance(self.biotype, GeneBiotypeEnum):
            self.biotype = GeneBiotypeEnum(self.biotype)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MolecularFunction(OntologyClass):
    """
    A Gene Ontology molecular function term represented in OptimusKG. Current Neo4j label: `MFN`.

    Property detail from OptimusKG source schema: A Gene Ontology (GO) molecular function node. Represents 10,161
    biochemical and enzymatic activities (5.3% of nodes) that gene products perform at the molecular level (e.g.
    "protein kinase activity", "DNA binding", "ATP hydrolysis activity"). Source: Gene Ontology (GO). Node file:
    nodes/molecular_function.parquet
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["MolecularActivity"]
    class_class_curie: ClassVar[str] = "biolink:MolecularActivity"
    class_name: ClassVar[str] = "MolecularFunction"
    class_model_uri: ClassVar[URIRef] = ALSKG.MolecularFunction

    id: Union[str, MolecularFunctionId] = None
    name: Optional[str] = None
    original_optimus_label: Optional[str] = None
    direct_sources: Optional[Union[str, list[str]]] = empty_list()
    indirect_sources: Optional[Union[str, list[str]]] = empty_list()
    has_synonym: Optional[Union[Union[str, SynonymId], list[Union[str, SynonymId]]]] = empty_list()
    has_cross_reference: Optional[Union[Union[str, DatabaseAccessionId], list[Union[str, DatabaseAccessionId]]]] = empty_list()
    definition: Optional[str] = None
    synonyms: Optional[Union[str, list[str]]] = empty_list()
    xrefs: Optional[Union[str, list[str]]] = empty_list()
    ontology: Optional[Union[str, OntologyMetadataId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MolecularFunctionId):
            self.id = MolecularFunctionId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.original_optimus_label is not None and not isinstance(self.original_optimus_label, str):
            self.original_optimus_label = str(self.original_optimus_label)

        if not isinstance(self.direct_sources, list):
            self.direct_sources = [self.direct_sources] if self.direct_sources is not None else []
        self.direct_sources = [v if isinstance(v, str) else str(v) for v in self.direct_sources]

        if not isinstance(self.indirect_sources, list):
            self.indirect_sources = [self.indirect_sources] if self.indirect_sources is not None else []
        self.indirect_sources = [v if isinstance(v, str) else str(v) for v in self.indirect_sources]

        if not isinstance(self.has_synonym, list):
            self.has_synonym = [self.has_synonym] if self.has_synonym is not None else []
        self.has_synonym = [v if isinstance(v, SynonymId) else SynonymId(v) for v in self.has_synonym]

        if not isinstance(self.has_cross_reference, list):
            self.has_cross_reference = [self.has_cross_reference] if self.has_cross_reference is not None else []
        self.has_cross_reference = [v if isinstance(v, DatabaseAccessionId) else DatabaseAccessionId(v) for v in self.has_cross_reference]

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        if not isinstance(self.xrefs, list):
            self.xrefs = [self.xrefs] if self.xrefs is not None else []
        self.xrefs = [v if isinstance(v, str) else str(v) for v in self.xrefs]

        if self.ontology is not None and not isinstance(self.ontology, OntologyMetadataId):
            self.ontology = OntologyMetadataId(self.ontology)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Phenotype(ClinicalEntity):
    """
    A phenotype or clinical feature represented in OptimusKG. Current Neo4j label: `PHE`.

    Property detail from OptimusKG source schema: A clinical phenotype or phenotypic abnormality node. Represents
    19,341 phenotypes (10.2% of nodes) from HPO and MedDRA, describing observable clinical features and traits
    associated with diseases. Sources: HPO, MedDRA, Open Targets. Node file: nodes/phenotype.parquet
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["PhenotypicFeature"]
    class_class_curie: ClassVar[str] = "biolink:PhenotypicFeature"
    class_name: ClassVar[str] = "Phenotype"
    class_model_uri: ClassVar[URIRef] = ALSKG.Phenotype

    id: Union[str, PhenotypeId] = None
    name: Optional[str] = None
    original_optimus_label: Optional[str] = None
    direct_sources: Optional[Union[str, list[str]]] = empty_list()
    indirect_sources: Optional[Union[str, list[str]]] = empty_list()
    has_synonym: Optional[Union[Union[str, SynonymId], list[Union[str, SynonymId]]]] = empty_list()
    has_cross_reference: Optional[Union[Union[str, DatabaseAccessionId], list[Union[str, DatabaseAccessionId]]]] = empty_list()
    is_supported_by: Optional[Union[Union[str, EvidenceRecordId], list[Union[str, EvidenceRecordId]]]] = empty_list()
    description: Optional[str] = None
    code: Optional[str] = None
    type: Optional[str] = None
    parents: Optional[Union[str, list[str]]] = empty_list()
    children: Optional[Union[str, list[str]]] = empty_list()
    ancestors: Optional[Union[str, list[str]]] = empty_list()
    descendants: Optional[Union[str, list[str]]] = empty_list()
    is_leaf: Optional[Union[bool, Bool]] = None
    exact_synonyms: Optional[Union[str, list[str]]] = empty_list()
    related_synonyms: Optional[Union[str, list[str]]] = empty_list()
    narrow_synonyms: Optional[Union[str, list[str]]] = empty_list()
    broad_synonyms: Optional[Union[str, list[str]]] = empty_list()
    obsolete_terms: Optional[Union[str, list[str]]] = empty_list()
    obsolete_xrefs: Optional[Union[str, list[str]]] = empty_list()
    xrefs: Optional[Union[str, list[str]]] = empty_list()
    concept_ids: Optional[Union[str, list[str]]] = empty_list()
    concept_names: Optional[Union[str, list[str]]] = empty_list()
    umls_cui: Optional[str] = None
    snomed_full_names: Optional[Union[str, list[str]]] = empty_list()
    snomed_concept_ids: Optional[Union[str, list[str]]] = empty_list()
    cui_semantic_type: Optional[str] = None
    ontology: Optional[Union[str, OntologyMetadataId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhenotypeId):
            self.id = PhenotypeId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.original_optimus_label is not None and not isinstance(self.original_optimus_label, str):
            self.original_optimus_label = str(self.original_optimus_label)

        if not isinstance(self.direct_sources, list):
            self.direct_sources = [self.direct_sources] if self.direct_sources is not None else []
        self.direct_sources = [v if isinstance(v, str) else str(v) for v in self.direct_sources]

        if not isinstance(self.indirect_sources, list):
            self.indirect_sources = [self.indirect_sources] if self.indirect_sources is not None else []
        self.indirect_sources = [v if isinstance(v, str) else str(v) for v in self.indirect_sources]

        if not isinstance(self.has_synonym, list):
            self.has_synonym = [self.has_synonym] if self.has_synonym is not None else []
        self.has_synonym = [v if isinstance(v, SynonymId) else SynonymId(v) for v in self.has_synonym]

        if not isinstance(self.has_cross_reference, list):
            self.has_cross_reference = [self.has_cross_reference] if self.has_cross_reference is not None else []
        self.has_cross_reference = [v if isinstance(v, DatabaseAccessionId) else DatabaseAccessionId(v) for v in self.has_cross_reference]

        if not isinstance(self.is_supported_by, list):
            self.is_supported_by = [self.is_supported_by] if self.is_supported_by is not None else []
        self.is_supported_by = [v if isinstance(v, EvidenceRecordId) else EvidenceRecordId(v) for v in self.is_supported_by]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.code is not None and not isinstance(self.code, str):
            self.code = str(self.code)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.parents, list):
            self.parents = [self.parents] if self.parents is not None else []
        self.parents = [v if isinstance(v, str) else str(v) for v in self.parents]

        if not isinstance(self.children, list):
            self.children = [self.children] if self.children is not None else []
        self.children = [v if isinstance(v, str) else str(v) for v in self.children]

        if not isinstance(self.ancestors, list):
            self.ancestors = [self.ancestors] if self.ancestors is not None else []
        self.ancestors = [v if isinstance(v, str) else str(v) for v in self.ancestors]

        if not isinstance(self.descendants, list):
            self.descendants = [self.descendants] if self.descendants is not None else []
        self.descendants = [v if isinstance(v, str) else str(v) for v in self.descendants]

        if self.is_leaf is not None and not isinstance(self.is_leaf, Bool):
            self.is_leaf = Bool(self.is_leaf)

        if not isinstance(self.exact_synonyms, list):
            self.exact_synonyms = [self.exact_synonyms] if self.exact_synonyms is not None else []
        self.exact_synonyms = [v if isinstance(v, str) else str(v) for v in self.exact_synonyms]

        if not isinstance(self.related_synonyms, list):
            self.related_synonyms = [self.related_synonyms] if self.related_synonyms is not None else []
        self.related_synonyms = [v if isinstance(v, str) else str(v) for v in self.related_synonyms]

        if not isinstance(self.narrow_synonyms, list):
            self.narrow_synonyms = [self.narrow_synonyms] if self.narrow_synonyms is not None else []
        self.narrow_synonyms = [v if isinstance(v, str) else str(v) for v in self.narrow_synonyms]

        if not isinstance(self.broad_synonyms, list):
            self.broad_synonyms = [self.broad_synonyms] if self.broad_synonyms is not None else []
        self.broad_synonyms = [v if isinstance(v, str) else str(v) for v in self.broad_synonyms]

        if not isinstance(self.obsolete_terms, list):
            self.obsolete_terms = [self.obsolete_terms] if self.obsolete_terms is not None else []
        self.obsolete_terms = [v if isinstance(v, str) else str(v) for v in self.obsolete_terms]

        if not isinstance(self.obsolete_xrefs, list):
            self.obsolete_xrefs = [self.obsolete_xrefs] if self.obsolete_xrefs is not None else []
        self.obsolete_xrefs = [v if isinstance(v, str) else str(v) for v in self.obsolete_xrefs]

        if not isinstance(self.xrefs, list):
            self.xrefs = [self.xrefs] if self.xrefs is not None else []
        self.xrefs = [v if isinstance(v, str) else str(v) for v in self.xrefs]

        if not isinstance(self.concept_ids, list):
            self.concept_ids = [self.concept_ids] if self.concept_ids is not None else []
        self.concept_ids = [v if isinstance(v, str) else str(v) for v in self.concept_ids]

        if not isinstance(self.concept_names, list):
            self.concept_names = [self.concept_names] if self.concept_names is not None else []
        self.concept_names = [v if isinstance(v, str) else str(v) for v in self.concept_names]

        if self.umls_cui is not None and not isinstance(self.umls_cui, str):
            self.umls_cui = str(self.umls_cui)

        if not isinstance(self.snomed_full_names, list):
            self.snomed_full_names = [self.snomed_full_names] if self.snomed_full_names is not None else []
        self.snomed_full_names = [v if isinstance(v, str) else str(v) for v in self.snomed_full_names]

        if not isinstance(self.snomed_concept_ids, list):
            self.snomed_concept_ids = [self.snomed_concept_ids] if self.snomed_concept_ids is not None else []
        self.snomed_concept_ids = [v if isinstance(v, str) else str(v) for v in self.snomed_concept_ids]

        if self.cui_semantic_type is not None and not isinstance(self.cui_semantic_type, str):
            self.cui_semantic_type = str(self.cui_semantic_type)

        if self.ontology is not None and not isinstance(self.ontology, OntologyMetadataId):
            self.ontology = OntologyMetadataId(self.ontology)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Pathway(OntologyClass):
    """
    A biological pathway represented in OptimusKG. Current Neo4j label: `PWY`.

    Property detail from OptimusKG source schema: A biological pathway node. Represents 2,805 curated pathways (1.5%
    of nodes) from Reactome, covering molecular reactions, signaling cascades, metabolic processes, and disease
    pathways in human cells. Sources: Open Targets, Reactome. Node file: nodes/pathway.parquet
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Pathway"]
    class_class_curie: ClassVar[str] = "biolink:Pathway"
    class_name: ClassVar[str] = "Pathway"
    class_model_uri: ClassVar[URIRef] = ALSKG.Pathway

    id: Union[str, PathwayId] = None
    name: Optional[str] = None
    original_optimus_label: Optional[str] = None
    direct_sources: Optional[Union[str, list[str]]] = empty_list()
    indirect_sources: Optional[Union[str, list[str]]] = empty_list()
    species: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PathwayId):
            self.id = PathwayId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.original_optimus_label is not None and not isinstance(self.original_optimus_label, str):
            self.original_optimus_label = str(self.original_optimus_label)

        if not isinstance(self.direct_sources, list):
            self.direct_sources = [self.direct_sources] if self.direct_sources is not None else []
        self.direct_sources = [v if isinstance(v, str) else str(v) for v in self.direct_sources]

        if not isinstance(self.indirect_sources, list):
            self.indirect_sources = [self.indirect_sources] if self.indirect_sources is not None else []
        self.indirect_sources = [v if isinstance(v, str) else str(v) for v in self.indirect_sources]

        if self.species is not None and not isinstance(self.species, str):
            self.species = str(self.species)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RelationshipAssertion(YAMLRoot):
    """
    Abstract root class for all typed, asserted relationships between named entities in OptimusKG. All family-level
    abstract classes and concrete relationship classes inherit subject, object, undirected, sources, and evidence
    slots from here. Four canonical direct children: HierarchyRelationship, AssociationRelationship,
    PharmacologicalRelationship, FunctionalAnnotationRelationship. Additional families: ExposureEntityRelationship
    (under AssociationRelationship), ExpressionRelationship (under AssociationRelationship),
    MolecularSubtypeRelationship (direct child, covers AnalyticalEntity edges).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RDF["Statement"]
    class_class_curie: ClassVar[str] = "rdf:Statement"
    class_name: ClassVar[str] = "RelationshipAssertion"
    class_model_uri: ClassVar[URIRef] = ALSKG.RelationshipAssertion

    has_evidence_record: Optional[Union[Union[str, EvidenceRecordId], list[Union[str, EvidenceRecordId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.has_evidence_record, list):
            self.has_evidence_record = [self.has_evidence_record] if self.has_evidence_record is not None else []
        self.has_evidence_record = [v if isinstance(v, EvidenceRecordId) else EvidenceRecordId(v) for v in self.has_evidence_record]

        super().__post_init__(**kwargs)


class HierarchyRelationship(RelationshipAssertion):
    """
    A parent, subclass, or ontology hierarchy relationship in the current OptimusKG Neo4j graph. This groups PARENT
    and IS_A edges while preserving the exact Neo4j relationship type in each concrete subclass.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["HierarchyRelationship"]
    class_class_curie: ClassVar[str] = "okg:HierarchyRelationship"
    class_name: ClassVar[str] = "HierarchyRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.HierarchyRelationship


class AssociationRelationship(RelationshipAssertion):
    """
    Abstract family for evidence-bearing association edges between biomedical entities. Covers gene-disease,
    disease-phenotype, phenotype-gene, drug-drug, drug-gene, exposure-entity, and gene-gene interaction relationships.
    Renamed from EntityAssociationRelationship (v0.3.0) for clarity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["AssociationRelationship"]
    class_class_curie: ClassVar[str] = "okg:AssociationRelationship"
    class_name: ClassVar[str] = "AssociationRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.AssociationRelationship


class FunctionalAnnotationRelationship(RelationshipAssertion):
    """
    Abstract family for GO annotation and pathway membership relationships. Connects genes to biological processes
    (BPO-GEN), cellular components (CCO-GEN), molecular functions (MFN-GEN), and pathways (PWY-GEN). One of the four
    canonical relationship families in OptimusKG v0.4.0.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["FunctionalAnnotationRelationship"]
    class_class_curie: ClassVar[str] = "okg:FunctionalAnnotationRelationship"
    class_name: ClassVar[str] = "FunctionalAnnotationRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.FunctionalAnnotationRelationship


@dataclass(repr=False)
class PharmacologicalRelationship(RelationshipAssertion):
    """
    Abstract family for drug therapeutic-use relationships, including indication, contraindication, off-label use, and
    adverse drug reactions. Subject is always a Drug node. Renamed from TherapeuticUseRelationship (v0.3.0) to reflect
    that this family covers all drug action semantics, not only clinical therapeutic use.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["PharmacologicalRelationship"]
    class_class_curie: ClassVar[str] = "okg:PharmacologicalRelationship"
    class_name: ClassVar[str] = "PharmacologicalRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.PharmacologicalRelationship

    subject: Optional[Union[str, DrugId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExposureEntityRelationship(AssociationRelationship):
    """
    Abstract family for exposure-to-entity association relationships. Now a subclass of AssociationRelationship rather
    than a direct child of RelationshipAssertion (v0.4.0 consolidation). Subject is always an Exposure node.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["ExposureEntityRelationship"]
    class_class_curie: ClassVar[str] = "okg:ExposureEntityRelationship"
    class_name: ClassVar[str] = "ExposureEntityRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.ExposureEntityRelationship

    subject: Optional[Union[str, ExposureId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, ExposureId):
            self.subject = ExposureId(self.subject)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhenotypeHierarchyRelationship(HierarchyRelationship):
    """
    Hierarchy relationship between Phenotype nodes, or from a phenotype to a disease when the installed graph uses a
    PARENT pattern across those labels.

    Property detail: Hierarchical relationships between HPO phenotype terms. Relation: PARENT (is_a, has_part within
    HPO ontology). Undirected: False. Count: 24,862. Source: HPO.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["PhenotypeHierarchyRelationship"]
    class_class_curie: ClassVar[str] = "okg:PhenotypeHierarchyRelationship"
    class_name: ClassVar[str] = "PhenotypeHierarchyRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.PhenotypeHierarchyRelationship

    subject: Optional[Union[str, PhenotypeId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, PhenotypeId):
            self.subject = PhenotypeId(self.subject)

        super().__post_init__(**kwargs)


class MolecularSubtypeRelationship(RelationshipAssertion):
    """
    Abstract family for all relationships involving a MolecularSubtype (AnalyticalEntity) node. Groups
    disease-to-subtype (HAS_MOLECULAR_SUBTYPE), gene-to-subtype (DYSREGULATED_IN), and subtype-to-anatomy
    (MEASURED_IN) relationships. Kept as a distinct family because MolecularSubtype is an AnalyticalEntity, not a
    standard ClinicalEntity, and its relationship semantics differ from standard biomedical association edges.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["MolecularSubtypeRelationship"]
    class_class_curie: ClassVar[str] = "okg:MolecularSubtypeRelationship"
    class_name: ClassVar[str] = "MolecularSubtypeRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.MolecularSubtypeRelationship


@dataclass(repr=False)
class AnatomyGeneExpressionRelationship(AssociationRelationship):
    """
    Parent class for anatomy-to-gene expression relationships, including expression present and expression absent
    edges.

    Property detail: Gene expression associations between anatomical structures and genes. Relations:
    EXPRESSION_PRESENT or EXPRESSION_ABSENT. Undirected: True. Count: 8,787,955 (40.3% of all edges). Source: Bgee
    (curated RNA-seq expression data, v2024-05-17). NOTE: ANA-GEN is the second-largest edge type and the most common
    category of edges lacking literature support (661/1413 unsupported edges in the PaperQA3 validation), reflecting
    the lag between data deposition and narrative synthesis in publications.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["AnatomyGeneExpressionRelationship"]
    class_class_curie: ClassVar[str] = "okg:AnatomyGeneExpressionRelationship"
    class_name: ClassVar[str] = "AnatomyGeneExpressionRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.AnatomyGeneExpressionRelationship

    expression_rank: Optional[int] = None
    call_quality: Optional[Union[str, "ExpressionCallQualityEnum"]] = None
    subject: Optional[Union[str, AnatomyId]] = None
    object: Optional[Union[str, GeneId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.expression_rank is not None and not isinstance(self.expression_rank, int):
            self.expression_rank = int(self.expression_rank)

        if self.call_quality is not None and not isinstance(self.call_quality, ExpressionCallQualityEnum):
            self.call_quality = ExpressionCallQualityEnum(self.call_quality)

        if self.subject is not None and not isinstance(self.subject, AnatomyId):
            self.subject = AnatomyId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DiseasePhenotypeRelationship(AssociationRelationship):
    """
    Concrete relationship class for disease-to-phenotype relationships, including phenotype presence annotations.

    Property detail: Clinical associations between diseases and their characteristic phenotypic features. Relation:
    PHENOTYPE_PRESENT. Undirected: True. Count: 157,144. Source: Open Targets (via HPO annotations).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DiseasePhenotypeRelationship"]
    class_class_curie: ClassVar[str] = "okg:DiseasePhenotypeRelationship"
    class_name: ClassVar[str] = "DiseasePhenotypeRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DiseasePhenotypeRelationship

    aspect: Optional[Union[str, list[str]]] = empty_list()
    evidence_type: Optional[Union[str, list[str]]] = empty_list()
    frequency: Optional[Union[str, list[str]]] = empty_list()
    onset: Optional[Union[str, list[str]]] = empty_list()
    modifiers: Optional[Union[str, list[str]]] = empty_list()
    sexes: Optional[Union[str, list[str]]] = empty_list()
    qualifier_not: Optional[Union[bool, Bool]] = None
    bio_curation: Optional[Union[str, list[str]]] = empty_list()
    references: Optional[Union[str, list[str]]] = empty_list()
    subject: Optional[Union[str, DiseaseId]] = None
    object: Optional[Union[str, PhenotypeId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.aspect, list):
            self.aspect = [self.aspect] if self.aspect is not None else []
        self.aspect = [v if isinstance(v, str) else str(v) for v in self.aspect]

        if not isinstance(self.evidence_type, list):
            self.evidence_type = [self.evidence_type] if self.evidence_type is not None else []
        self.evidence_type = [v if isinstance(v, str) else str(v) for v in self.evidence_type]

        if not isinstance(self.frequency, list):
            self.frequency = [self.frequency] if self.frequency is not None else []
        self.frequency = [v if isinstance(v, str) else str(v) for v in self.frequency]

        if not isinstance(self.onset, list):
            self.onset = [self.onset] if self.onset is not None else []
        self.onset = [v if isinstance(v, str) else str(v) for v in self.onset]

        if not isinstance(self.modifiers, list):
            self.modifiers = [self.modifiers] if self.modifiers is not None else []
        self.modifiers = [v if isinstance(v, str) else str(v) for v in self.modifiers]

        if not isinstance(self.sexes, list):
            self.sexes = [self.sexes] if self.sexes is not None else []
        self.sexes = [v if isinstance(v, str) else str(v) for v in self.sexes]

        if self.qualifier_not is not None and not isinstance(self.qualifier_not, Bool):
            self.qualifier_not = Bool(self.qualifier_not)

        if not isinstance(self.bio_curation, list):
            self.bio_curation = [self.bio_curation] if self.bio_curation is not None else []
        self.bio_curation = [v if isinstance(v, str) else str(v) for v in self.bio_curation]

        if not isinstance(self.references, list):
            self.references = [self.references] if self.references is not None else []
        self.references = [v if isinstance(v, str) else str(v) for v in self.references]

        if self.subject is not None and not isinstance(self.subject, DiseaseId):
            self.subject = DiseaseId(self.subject)

        if self.object is not None and not isinstance(self.object, PhenotypeId):
            self.object = PhenotypeId(self.object)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugBiologicalProcessTherapeuticRelationship(PharmacologicalRelationship):
    """
    Concrete relationship class for drug-to-biological-process therapeutic-use relationships.

    Property detail: Drug indications linked to biological processes. Relation: INDICATION. Undirected: True. Count:
    62. Source: Open Targets.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugBiologicalProcessTherapeuticRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugBiologicalProcessTherapeuticRelationship"
    class_name: ClassVar[str] = "DrugBiologicalProcessTherapeuticRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugBiologicalProcessTherapeuticRelationship

    highest_clinical_trial_phase: Optional[float] = None
    reference_ids: Optional[Union[str, list[str]]] = empty_list()
    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, BiologicalProcessId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.highest_clinical_trial_phase is not None and not isinstance(self.highest_clinical_trial_phase, float):
            self.highest_clinical_trial_phase = float(self.highest_clinical_trial_phase)

        if not isinstance(self.reference_ids, list):
            self.reference_ids = [self.reference_ids] if self.reference_ids is not None else []
        self.reference_ids = [v if isinstance(v, str) else str(v) for v in self.reference_ids]

        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, BiologicalProcessId):
            self.object = BiologicalProcessId(self.object)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugDiseaseTherapeuticRelationship(PharmacologicalRelationship):
    """
    Parent class for drug-to-disease therapeutic-use relationships, including indication, contraindication, and
    off-label use.

    Property detail: Drug-disease therapeutic associations including indications, contraindications, and off-label
    uses. Relations: INDICATION, CONTRAINDICATION, OFF_LABEL_USE. Undirected: True. Count: 70,380. Sources:
    DrugCentral, Open Targets. Indirect: ATC, Clinical Trials, DailyMed, EMA, FDA, INN, USAN.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugDiseaseTherapeuticRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugDiseaseTherapeuticRelationship"
    class_name: ClassVar[str] = "DrugDiseaseTherapeuticRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugDiseaseTherapeuticRelationship

    highest_clinical_trial_phase: Optional[float] = None
    structure_id: Optional[str] = None
    drug_disease_id: Optional[str] = None
    reference_ids: Optional[Union[str, list[str]]] = empty_list()
    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, DiseaseId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.highest_clinical_trial_phase is not None and not isinstance(self.highest_clinical_trial_phase, float):
            self.highest_clinical_trial_phase = float(self.highest_clinical_trial_phase)

        if self.structure_id is not None and not isinstance(self.structure_id, str):
            self.structure_id = str(self.structure_id)

        if self.drug_disease_id is not None and not isinstance(self.drug_disease_id, str):
            self.drug_disease_id = str(self.drug_disease_id)

        if not isinstance(self.reference_ids, list):
            self.reference_ids = [self.reference_ids] if self.reference_ids is not None else []
        self.reference_ids = [v if isinstance(v, str) else str(v) for v in self.reference_ids]

        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, DiseaseId):
            self.object = DiseaseId(self.object)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugPhenotypeTherapeuticRelationship(PharmacologicalRelationship):
    """
    Parent class for drug-to-phenotype therapeutic and adverse-event relationships.

    Property detail: Drug effects on clinical phenotypic outcomes, including adverse reactions, indications,
    contraindications, and off-label uses. Relations: ADVERSE_DRUG_REACTION, ASSOCIATED_WITH, CONTRAINDICATION,
    INDICATION, OFF_LABEL_USE. Undirected: True. Count: 13,758. Sources: DrugCentral, OnSIDES, Open Targets. OnSIDES
    data: adverse drug events extracted from FDA labels using PubMedBERT.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugPhenotypeTherapeuticRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugPhenotypeTherapeuticRelationship"
    class_name: ClassVar[str] = "DrugPhenotypeTherapeuticRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugPhenotypeTherapeuticRelationship

    highest_clinical_trial_phase: Optional[float] = None
    structure_id: Optional[str] = None
    drug_disease_id: Optional[str] = None
    reference_ids: Optional[Union[str, list[str]]] = empty_list()
    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, PhenotypeId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.highest_clinical_trial_phase is not None and not isinstance(self.highest_clinical_trial_phase, float):
            self.highest_clinical_trial_phase = float(self.highest_clinical_trial_phase)

        if self.structure_id is not None and not isinstance(self.structure_id, str):
            self.structure_id = str(self.structure_id)

        if self.drug_disease_id is not None and not isinstance(self.drug_disease_id, str):
            self.drug_disease_id = str(self.drug_disease_id)

        if not isinstance(self.reference_ids, list):
            self.reference_ids = [self.reference_ids] if self.reference_ids is not None else []
        self.reference_ids = [v if isinstance(v, str) else str(v) for v in self.reference_ids]

        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, PhenotypeId):
            self.object = PhenotypeId(self.object)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugDrugRelationship(AssociationRelationship):
    """
    Concrete relationship class for drug-to-drug relationships such as synergistic interaction.

    Property detail: Drug-drug interactions and hierarchical drug relationships. Relations: SYNERGISTIC_INTERACTION,
    PARENT. Undirected: False. Count: 1,345,376. Source: DrugBank, Open Targets. NOTE: DRG-DRG is the third-largest
    edge type. It includes both pharmacological interactions (DDIs from DrugBank) and ontological parent-child
    relationships within drug classification hierarchies.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugDrugRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugDrugRelationship"
    class_name: ClassVar[str] = "DrugDrugRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugDrugRelationship

    interaction_description: Optional[str] = None
    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, DrugId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.interaction_description is not None and not isinstance(self.interaction_description, str):
            self.interaction_description = str(self.interaction_description)

        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, DrugId):
            self.object = DrugId(self.object)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugGeneRelationship(AssociationRelationship):
    """
    Parent class for all OptimusKG relationships between Drug and Gene nodes. This groups target, modulation,
    transporter, enzyme, carrier, and other pharmacologic relationship types.

    Property detail: Drug-target interactions with pharmacological mechanism annotations. Relations: 23 types
    including ACTIVATOR, AGONIST, ANTAGONIST, INHIBITOR, TARGET, SUBSTRATE, CARRIER, TRANSPORTER, ENZYME, etc.
    Undirected: False. Count: 20,694. Sources: DrugBank, Open Targets. Indirect: BNF, Clinical Trials, DOI, DailyMed,
    EMA, Expert, FDA, HMA, ISBN, IUPHAR, KEGG, Other, PMC, Patent, PubChem, PubMed, UniProt, Wikipedia.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugGeneRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugGeneRelationship"
    class_name: ClassVar[str] = "DrugGeneRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugGeneRelationship

    source_ids: Optional[Union[str, list[str]]] = empty_list()
    mechanisms_of_action: Optional[Union[str, list[str]]] = empty_list()
    source_urls: Optional[Union[str, list[str]]] = empty_list()
    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, GeneId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.source_ids, list):
            self.source_ids = [self.source_ids] if self.source_ids is not None else []
        self.source_ids = [v if isinstance(v, str) else str(v) for v in self.source_ids]

        if not isinstance(self.mechanisms_of_action, list):
            self.mechanisms_of_action = [self.mechanisms_of_action] if self.mechanisms_of_action is not None else []
        self.mechanisms_of_action = [v if isinstance(v, str) else str(v) for v in self.mechanisms_of_action]

        if not isinstance(self.source_urls, list):
            self.source_urls = [self.source_urls] if self.source_urls is not None else []
        self.source_urls = [v if isinstance(v, str) else str(v) for v in self.source_urls]

        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugGeneTargetingRelationship(DrugGeneRelationship):
    """
    Drug-gene relationship indicating target designation, target binding, substrate status, or direct drug-target
    association.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugGeneTargetingRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugGeneTargetingRelationship"
    class_name: ClassVar[str] = "DrugGeneTargetingRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugGeneTargetingRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, GeneId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugGeneModulationRelationship(DrugGeneRelationship):
    """
    Drug-gene relationship indicating that the drug changes the activity, abundance, state, opening, stability,
    degradation, release, or function of the gene product.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugGeneModulationRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugGeneModulationRelationship"
    class_name: ClassVar[str] = "DrugGeneModulationRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugGeneModulationRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, GeneId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugGeneRoleRelationship(DrugGeneRelationship):
    """
    Drug-gene relationship describing the role of a gene product in drug metabolism, transport, or carrier behavior.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugGeneRoleRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugGeneRoleRelationship"
    class_name: ClassVar[str] = "DrugGeneRoleRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugGeneRoleRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, GeneId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AnatomyHasParentAnatomyRelationship(HierarchyRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:ANA)-[:PARENT]->(:ANA)`, represented with full class names
    as Anatomy -> Anatomy. Parent-child hierarchy relationship from the source concept to a broader or parent concept
    in the same or related ontology.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["AnatomyParentAnatomyRelationship"]
    class_class_curie: ClassVar[str] = "okg:AnatomyParentAnatomyRelationship"
    class_name: ClassVar[str] = "AnatomyHasParentAnatomyRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.AnatomyHasParentAnatomyRelationship

    subject: Optional[Union[str, AnatomyId]] = None
    object: Optional[Union[str, AnatomyId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, AnatomyId):
            self.subject = AnatomyId(self.subject)

        if self.object is not None and not isinstance(self.object, AnatomyId):
            self.object = AnatomyId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AnatomyHasGeneExpressionAbsentRelationship(AnatomyGeneExpressionRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:ANA)-[:EXPRESSION_ABSENT]->(:GEN)`, represented with full
    class names as Anatomy -> Gene. Gene expression is reported absent in an anatomical context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["AnatomyExpressionAbsentGeneRelationship"]
    class_class_curie: ClassVar[str] = "okg:AnatomyExpressionAbsentGeneRelationship"
    class_name: ClassVar[str] = "AnatomyHasGeneExpressionAbsentRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.AnatomyHasGeneExpressionAbsentRelationship

    subject: Optional[Union[str, AnatomyId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, AnatomyId):
            self.subject = AnatomyId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AnatomyHasGeneExpressionPresentRelationship(AnatomyGeneExpressionRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:ANA)-[:EXPRESSION_PRESENT]->(:GEN)`, represented with full
    class names as Anatomy -> Gene. Gene expression is reported present in an anatomical context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["AnatomyExpressionPresentGeneRelationship"]
    class_class_curie: ClassVar[str] = "okg:AnatomyExpressionPresentGeneRelationship"
    class_name: ClassVar[str] = "AnatomyHasGeneExpressionPresentRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.AnatomyHasGeneExpressionPresentRelationship

    subject: Optional[Union[str, AnatomyId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, AnatomyId):
            self.subject = AnatomyId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiologicalProcessIsSubclassOfRelationship(HierarchyRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:BPO)-[:IS_A]->(:BPO)`, represented with full class names as
    BiologicalProcess -> BiologicalProcess. Ontology subclass relationship indicating the source concept is a kind of
    the target concept.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["BiologicalProcessIsABiologicalProcessRelationship"]
    class_class_curie: ClassVar[str] = "okg:BiologicalProcessIsABiologicalProcessRelationship"
    class_name: ClassVar[str] = "BiologicalProcessIsSubclassOfRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.BiologicalProcessIsSubclassOfRelationship

    subject: Optional[Union[str, BiologicalProcessId]] = None
    object: Optional[Union[str, BiologicalProcessId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, BiologicalProcessId):
            self.subject = BiologicalProcessId(self.subject)

        if self.object is not None and not isinstance(self.object, BiologicalProcessId):
            self.object = BiologicalProcessId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiologicalProcessHasParticipatingGeneRelationship(FunctionalAnnotationRelationship):
    """
    A biological-process-to-gene relationship corresponding to Neo4j
    `(:BiologicalProcess)-[:INTERACTS_WITH]->(:Gene)`. In the semantic view, interpret as a gene annotated to or
    participating in a biological process, not necessarily a physical interaction.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["BiologicalProcessInteractsWithGeneRelationship"]
    class_class_curie: ClassVar[str] = "okg:BiologicalProcessInteractsWithGeneRelationship"
    class_name: ClassVar[str] = "BiologicalProcessHasParticipatingGeneRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.BiologicalProcessHasParticipatingGeneRelationship

    subject: Optional[Union[str, BiologicalProcessId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, BiologicalProcessId):
            self.subject = BiologicalProcessId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CellularComponentIsSubclassOfRelationship(HierarchyRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:CCO)-[:IS_A]->(:CCO)`, represented with full class names as
    CellularComponent -> CellularComponent. Ontology subclass relationship indicating the source concept is a kind of
    the target concept.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["CellularComponentIsACellularComponentRelationship"]
    class_class_curie: ClassVar[str] = "okg:CellularComponentIsACellularComponentRelationship"
    class_name: ClassVar[str] = "CellularComponentIsSubclassOfRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.CellularComponentIsSubclassOfRelationship

    subject: Optional[Union[str, CellularComponentId]] = None
    object: Optional[Union[str, CellularComponentId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, CellularComponentId):
            self.subject = CellularComponentId(self.subject)

        if self.object is not None and not isinstance(self.object, CellularComponentId):
            self.object = CellularComponentId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CellularComponentHasLocatedGeneRelationship(FunctionalAnnotationRelationship):
    """
    A cellular-component-to-gene relationship corresponding to Neo4j
    `(:CellularComponent)-[:INTERACTS_WITH]->(:Gene)`. In the semantic view, interpret as gene/gene-product cellular
    component localization or annotation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["CellularComponentInteractsWithGeneRelationship"]
    class_class_curie: ClassVar[str] = "okg:CellularComponentInteractsWithGeneRelationship"
    class_name: ClassVar[str] = "CellularComponentHasLocatedGeneRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.CellularComponentHasLocatedGeneRelationship

    subject: Optional[Union[str, CellularComponentId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, CellularComponentId):
            self.subject = CellularComponentId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DiseaseHasParentDiseaseRelationship(HierarchyRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DIS)-[:PARENT]->(:DIS)`, represented with full class names
    as Disease -> Disease. Parent-child hierarchy relationship from the source concept to a broader or parent concept
    in the same or related ontology.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DiseaseParentDiseaseRelationship"]
    class_class_curie: ClassVar[str] = "okg:DiseaseParentDiseaseRelationship"
    class_name: ClassVar[str] = "DiseaseHasParentDiseaseRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DiseaseHasParentDiseaseRelationship

    subject: Optional[Union[str, DiseaseId]] = None
    object: Optional[Union[str, DiseaseId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DiseaseId):
            self.subject = DiseaseId(self.subject)

        if self.object is not None and not isinstance(self.object, DiseaseId):
            self.object = DiseaseId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DiseaseAssociatedWithGeneRelationship(AssociationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DIS)-[:ASSOCIATED_WITH]->(:GEN)`, represented with full
    class names as Disease -> Gene. Association relationship; generally evidence-bearing but not necessarily causal.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DiseaseAssociatedWithGeneRelationship"]
    class_class_curie: ClassVar[str] = "okg:DiseaseAssociatedWithGeneRelationship"
    class_name: ClassVar[str] = "DiseaseAssociatedWithGeneRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DiseaseAssociatedWithGeneRelationship

    subject: Optional[Union[str, DiseaseId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DiseaseId):
            self.subject = DiseaseId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DiseaseHasPhenotypeRelationship(DiseasePhenotypeRelationship):
    """
    A disease-to-phenotype relationship corresponding to Neo4j `(:Disease)-[:PHENOTYPE_PRESENT]->(:Phenotype)`. It
    means the disease has/presents the phenotype. The inverse natural-language reading is "the phenotype is present in
    the disease", but the current graph direction is Disease -> Phenotype.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DiseasePhenotypePresentPhenotypeRelationship"]
    class_class_curie: ClassVar[str] = "okg:DiseasePhenotypePresentPhenotypeRelationship"
    class_name: ClassVar[str] = "DiseaseHasPhenotypeRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DiseaseHasPhenotypeRelationship

    subject: Optional[Union[str, DiseaseId]] = None
    object: Optional[Union[str, PhenotypeId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DiseaseId):
            self.subject = DiseaseId(self.subject)

        if self.object is not None and not isinstance(self.object, PhenotypeId):
            self.object = PhenotypeId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugHasIndicationForBiologicalProcessRelationship(DrugBiologicalProcessTherapeuticRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:INDICATION]->(:BPO)`, represented with full class
    names as Drug -> BiologicalProcess. Drug has an indicated therapeutic use for a disease, phenotype, or biological
    process context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugIndicationBiologicalProcessRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugIndicationBiologicalProcessRelationship"
    class_name: ClassVar[str] = "DrugHasIndicationForBiologicalProcessRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugHasIndicationForBiologicalProcessRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, BiologicalProcessId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, BiologicalProcessId):
            self.object = BiologicalProcessId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugContraindicatedForDiseaseRelationship(DrugDiseaseTherapeuticRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:CONTRAINDICATION]->(:DIS)`, represented with full
    class names as Drug -> Disease. Drug is contraindicated for a disease or phenotype context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugContraindicationDiseaseRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugContraindicationDiseaseRelationship"
    class_name: ClassVar[str] = "DrugContraindicatedForDiseaseRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugContraindicatedForDiseaseRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, DiseaseId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, DiseaseId):
            self.object = DiseaseId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugIndicatedForDiseaseRelationship(DrugDiseaseTherapeuticRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:INDICATION]->(:DIS)`, represented with full class
    names as Drug -> Disease. Drug has an indicated therapeutic use for a disease, phenotype, or biological process
    context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugIndicationDiseaseRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugIndicationDiseaseRelationship"
    class_name: ClassVar[str] = "DrugIndicatedForDiseaseRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugIndicatedForDiseaseRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, DiseaseId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, DiseaseId):
            self.object = DiseaseId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugUsedOffLabelForDiseaseRelationship(DrugDiseaseTherapeuticRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:OFF_LABEL_USE]->(:DIS)`, represented with full class
    names as Drug -> Disease. Drug has off-label use for a disease or phenotype context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugOffLabelUseDiseaseRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugOffLabelUseDiseaseRelationship"
    class_name: ClassVar[str] = "DrugUsedOffLabelForDiseaseRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugUsedOffLabelForDiseaseRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, DiseaseId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, DiseaseId):
            self.object = DiseaseId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugHasParentDrugRelationship(HierarchyRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:PARENT]->(:DRG)`, represented with full class names
    as Drug -> Drug. Parent-child hierarchy relationship from the source concept to a broader or parent concept in the
    same or related ontology.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugParentDrugRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugParentDrugRelationship"
    class_name: ClassVar[str] = "DrugHasParentDrugRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugHasParentDrugRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, DrugId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, DrugId):
            self.object = DrugId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugHasSynergisticInteractionWithDrugRelationship(DrugDrugRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:SYNERGISTIC_INTERACTION]->(:DRG)`, represented with
    full class names as Drug -> Drug. Drug-drug relationship indicating synergistic interaction.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugSynergisticInteractionDrugRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugSynergisticInteractionDrugRelationship"
    class_name: ClassVar[str] = "DrugHasSynergisticInteractionWithDrugRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugHasSynergisticInteractionWithDrugRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, DrugId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, DrugId):
            self.object = DrugId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugActivatesGeneProductRelationship(DrugGeneModulationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:ACTIVATOR]->(:GEN)`, represented with full class
    names as Drug -> Gene. Drug activates the gene product or target associated with the gene.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugActivatorGeneRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugActivatorGeneRelationship"
    class_name: ClassVar[str] = "DrugActivatesGeneProductRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugActivatesGeneProductRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugAgonistOfGeneProductRelationship(DrugGeneModulationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:AGONIST]->(:GEN)`, represented with full class names
    as Drug -> Gene. Drug acts as an agonist of the gene product or target associated with the gene.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugAgonistGeneRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugAgonistGeneRelationship"
    class_name: ClassVar[str] = "DrugAgonistOfGeneProductRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugAgonistOfGeneProductRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugAllostericAntagonistOfGeneProductRelationship(DrugGeneModulationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:ALLOSTERIC_ANTAGONIST]->(:GEN)`, represented with
    full class names as Drug -> Gene. Drug acts as an allosteric antagonist of the gene product or target associated
    with the gene.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugAllostericAntagonistGeneRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugAllostericAntagonistGeneRelationship"
    class_name: ClassVar[str] = "DrugAllostericAntagonistOfGeneProductRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugAllostericAntagonistOfGeneProductRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugAntagonistOfGeneProductRelationship(DrugGeneModulationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:ANTAGONIST]->(:GEN)`, represented with full class
    names as Drug -> Gene. Drug acts as an antagonist of the gene product or target associated with the gene.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugAntagonistGeneRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugAntagonistGeneRelationship"
    class_name: ClassVar[str] = "DrugAntagonistOfGeneProductRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugAntagonistOfGeneProductRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugBindsGeneProductRelationship(DrugGeneTargetingRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:BINDING_AGENT]->(:GEN)`, represented with full class
    names as Drug -> Gene. Drug binds the gene product or target associated with the gene.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugBindingAgentGeneRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugBindingAgentGeneRelationship"
    class_name: ClassVar[str] = "DrugBindsGeneProductRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugBindsGeneProductRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugBlocksGeneProductRelationship(DrugGeneModulationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:BLOCKER]->(:GEN)`, represented with full class names
    as Drug -> Gene. Drug blocks the gene product or target associated with the gene.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugBlockerGeneRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugBlockerGeneRelationship"
    class_name: ClassVar[str] = "DrugBlocksGeneProductRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugBlocksGeneProductRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugHasCarrierGeneProductRelationship(DrugGeneRoleRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:CARRIER]->(:GEN)`, represented with full class names
    as Drug -> Gene. Drug-gene relationship where the gene product is a carrier in pharmacologic context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugCarrierGeneRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugCarrierGeneRelationship"
    class_name: ClassVar[str] = "DrugHasCarrierGeneProductRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugHasCarrierGeneProductRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugDegradesGeneProductRelationship(DrugGeneModulationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:DEGRADER]->(:GEN)`, represented with full class names
    as Drug -> Gene. Drug degrades or induces degradation of the gene product or target.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugDegraderGeneRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugDegraderGeneRelationship"
    class_name: ClassVar[str] = "DrugDegradesGeneProductRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugDegradesGeneProductRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugHasMetabolizingEnzymeGeneProductRelationship(DrugGeneRoleRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:ENZYME]->(:GEN)`, represented with full class names
    as Drug -> Gene. Drug-gene relationship where the gene product is an enzyme in drug metabolism or action context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugEnzymeGeneRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugEnzymeGeneRelationship"
    class_name: ClassVar[str] = "DrugHasMetabolizingEnzymeGeneProductRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugHasMetabolizingEnzymeGeneProductRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugInhibitsGeneProductRelationship(DrugGeneModulationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:INHIBITOR]->(:GEN)`, represented with full class
    names as Drug -> Gene. Drug inhibits the gene product or target associated with the gene.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugInhibitorGeneRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugInhibitorGeneRelationship"
    class_name: ClassVar[str] = "DrugInhibitsGeneProductRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugInhibitsGeneProductRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugInverseAgonistOfGeneProductRelationship(DrugGeneModulationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:INVERSE_AGONIST]->(:GEN)`, represented with full
    class names as Drug -> Gene. Drug acts as an inverse agonist of the gene product or target.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugInverseAgonistGeneRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugInverseAgonistGeneRelationship"
    class_name: ClassVar[str] = "DrugInverseAgonistOfGeneProductRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugInverseAgonistOfGeneProductRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugModulatesGeneProductRelationship(DrugGeneModulationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:MODULATOR]->(:GEN)`, represented with full class
    names as Drug -> Gene. Drug modulates the gene product or target associated with the gene.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugModulatorGeneRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugModulatorGeneRelationship"
    class_name: ClassVar[str] = "DrugModulatesGeneProductRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugModulatesGeneProductRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugNegativeAllostericModulatorOfGeneProductRelationship(DrugGeneModulationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:NEGATIVE_ALLOSTERIC_MODULATOR]->(:GEN)`, represented
    with full class names as Drug -> Gene. Drug acts as a negative allosteric modulator of the gene product or target.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugNegativeAllostericModulatorGeneRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugNegativeAllostericModulatorGeneRelationship"
    class_name: ClassVar[str] = "DrugNegativeAllostericModulatorOfGeneProductRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugNegativeAllostericModulatorOfGeneProductRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugNegativelyModulatesGeneProductRelationship(DrugGeneModulationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:NEGATIVE_MODULATOR]->(:GEN)`, represented with full
    class names as Drug -> Gene. Drug negatively modulates the gene product or target.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugNegativeModulatorGeneRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugNegativeModulatorGeneRelationship"
    class_name: ClassVar[str] = "DrugNegativelyModulatesGeneProductRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugNegativelyModulatesGeneProductRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugOpensGeneProductRelationship(DrugGeneModulationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:OPENER]->(:GEN)`, represented with full class names
    as Drug -> Gene. Drug opens the gene product or target, often a channel target.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugOpenerGeneRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugOpenerGeneRelationship"
    class_name: ClassVar[str] = "DrugOpensGeneProductRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugOpensGeneProductRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugPartialAgonistOfGeneProductRelationship(DrugGeneModulationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:PARTIAL_AGONIST]->(:GEN)`, represented with full
    class names as Drug -> Gene. Drug acts as a partial agonist of the gene product or target.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugPartialAgonistGeneRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugPartialAgonistGeneRelationship"
    class_name: ClassVar[str] = "DrugPartialAgonistOfGeneProductRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugPartialAgonistOfGeneProductRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugPositiveAllostericModulatorOfGeneProductRelationship(DrugGeneModulationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:POSITIVE_ALLOSTERIC_MODULATOR]->(:GEN)`, represented
    with full class names as Drug -> Gene. Drug acts as a positive allosteric modulator of the gene product or target.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugPositiveAllostericModulatorGeneRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugPositiveAllostericModulatorGeneRelationship"
    class_name: ClassVar[str] = "DrugPositiveAllostericModulatorOfGeneProductRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugPositiveAllostericModulatorOfGeneProductRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugPositivelyModulatesGeneProductRelationship(DrugGeneModulationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:POSITIVE_MODULATOR]->(:GEN)`, represented with full
    class names as Drug -> Gene. Drug positively modulates the gene product or target.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugPositiveModulatorGeneRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugPositiveModulatorGeneRelationship"
    class_name: ClassVar[str] = "DrugPositivelyModulatesGeneProductRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugPositivelyModulatesGeneProductRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugReleasingAgentOfGeneProductRelationship(DrugGeneModulationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:RELEASING_AGENT]->(:GEN)`, represented with full
    class names as Drug -> Gene. Drug acts as a releasing agent affecting the gene product or related target system.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugReleasingAgentGeneRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugReleasingAgentGeneRelationship"
    class_name: ClassVar[str] = "DrugReleasingAgentOfGeneProductRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugReleasingAgentOfGeneProductRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugStabilizesGeneProductRelationship(DrugGeneModulationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:STABILISER]->(:GEN)`, represented with full class
    names as Drug -> Gene. Drug stabilizes the gene product or target.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugStabiliserGeneRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugStabiliserGeneRelationship"
    class_name: ClassVar[str] = "DrugStabilizesGeneProductRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugStabilizesGeneProductRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugIsSubstrateOfGeneProductRelationship(DrugGeneTargetingRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:SUBSTRATE]->(:GEN)`, represented with full class
    names as Drug -> Gene. Drug is a substrate of the gene product, often an enzyme or transporter.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugSubstrateGeneRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugSubstrateGeneRelationship"
    class_name: ClassVar[str] = "DrugIsSubstrateOfGeneProductRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugIsSubstrateOfGeneProductRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugTargetsGeneProductRelationship(DrugGeneTargetingRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:TARGET]->(:GEN)`, represented with full class names
    as Drug -> Gene. Drug targets the gene product associated with the gene.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugTargetGeneRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugTargetGeneRelationship"
    class_name: ClassVar[str] = "DrugTargetsGeneProductRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugTargetsGeneProductRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugHasTransporterGeneProductRelationship(DrugGeneRoleRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:TRANSPORTER]->(:GEN)`, represented with full class
    names as Drug -> Gene. Drug-gene relationship where the gene product is a transporter in pharmacologic context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugTransporterGeneRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugTransporterGeneRelationship"
    class_name: ClassVar[str] = "DrugHasTransporterGeneProductRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugHasTransporterGeneProductRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugHasAdversePhenotypeRelationship(DrugPhenotypeTherapeuticRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:ADVERSE_DRUG_REACTION]->(:PHE)`, represented with
    full class names as Drug -> Phenotype. Drug-to-phenotype relationship indicating an adverse drug reaction.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugAdverseDrugReactionPhenotypeRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugAdverseDrugReactionPhenotypeRelationship"
    class_name: ClassVar[str] = "DrugHasAdversePhenotypeRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugHasAdversePhenotypeRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, PhenotypeId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, PhenotypeId):
            self.object = PhenotypeId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugAssociatedWithPhenotypeRelationship(DrugPhenotypeTherapeuticRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:ASSOCIATED_WITH]->(:PHE)`, represented with full
    class names as Drug -> Phenotype. Association relationship; generally evidence-bearing but not necessarily causal.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugAssociatedWithPhenotypeRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugAssociatedWithPhenotypeRelationship"
    class_name: ClassVar[str] = "DrugAssociatedWithPhenotypeRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugAssociatedWithPhenotypeRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, PhenotypeId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, PhenotypeId):
            self.object = PhenotypeId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugContraindicatedForPhenotypeRelationship(DrugPhenotypeTherapeuticRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:CONTRAINDICATION]->(:PHE)`, represented with full
    class names as Drug -> Phenotype. Drug is contraindicated for a disease or phenotype context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugContraindicationPhenotypeRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugContraindicationPhenotypeRelationship"
    class_name: ClassVar[str] = "DrugContraindicatedForPhenotypeRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugContraindicatedForPhenotypeRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, PhenotypeId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, PhenotypeId):
            self.object = PhenotypeId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugIndicatedForPhenotypeRelationship(DrugPhenotypeTherapeuticRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:INDICATION]->(:PHE)`, represented with full class
    names as Drug -> Phenotype. Drug has an indicated therapeutic use for a disease, phenotype, or biological process
    context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugIndicationPhenotypeRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugIndicationPhenotypeRelationship"
    class_name: ClassVar[str] = "DrugIndicatedForPhenotypeRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugIndicatedForPhenotypeRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, PhenotypeId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, PhenotypeId):
            self.object = PhenotypeId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugUsedOffLabelForPhenotypeRelationship(DrugPhenotypeTherapeuticRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:DRG)-[:OFF_LABEL_USE]->(:PHE)`, represented with full class
    names as Drug -> Phenotype. Drug has off-label use for a disease or phenotype context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DrugOffLabelUsePhenotypeRelationship"]
    class_class_curie: ClassVar[str] = "okg:DrugOffLabelUsePhenotypeRelationship"
    class_name: ClassVar[str] = "DrugUsedOffLabelForPhenotypeRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugUsedOffLabelForPhenotypeRelationship

    subject: Optional[Union[str, DrugId]] = None
    object: Optional[Union[str, PhenotypeId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugId):
            self.subject = DrugId(self.subject)

        if self.object is not None and not isinstance(self.object, PhenotypeId):
            self.object = PhenotypeId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExposureAssociatedWithBiologicalProcessRelationship(ExposureEntityRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:EXP)-[:INTERACTS_WITH]->(:BPO)`, represented with full class
    names as Exposure -> BiologicalProcess. Generic interaction or annotation-style relationship. Interpret according
    to the source and node pair; it may indicate interaction, membership, annotation, or functional context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["ExposureInteractsWithBiologicalProcessRelationship"]
    class_class_curie: ClassVar[str] = "okg:ExposureInteractsWithBiologicalProcessRelationship"
    class_name: ClassVar[str] = "ExposureAssociatedWithBiologicalProcessRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.ExposureAssociatedWithBiologicalProcessRelationship

    subject: Optional[Union[str, ExposureId]] = None
    object: Optional[Union[str, BiologicalProcessId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, ExposureId):
            self.subject = ExposureId(self.subject)

        if self.object is not None and not isinstance(self.object, BiologicalProcessId):
            self.object = BiologicalProcessId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExposureAssociatedWithCellularComponentRelationship(ExposureEntityRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:EXP)-[:INTERACTS_WITH]->(:CCO)`, represented with full class
    names as Exposure -> CellularComponent. Generic interaction or annotation-style relationship. Interpret according
    to the source and node pair; it may indicate interaction, membership, annotation, or functional context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["ExposureInteractsWithCellularComponentRelationship"]
    class_class_curie: ClassVar[str] = "okg:ExposureInteractsWithCellularComponentRelationship"
    class_name: ClassVar[str] = "ExposureAssociatedWithCellularComponentRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.ExposureAssociatedWithCellularComponentRelationship

    subject: Optional[Union[str, ExposureId]] = None
    object: Optional[Union[str, CellularComponentId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, ExposureId):
            self.subject = ExposureId(self.subject)

        if self.object is not None and not isinstance(self.object, CellularComponentId):
            self.object = CellularComponentId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExposureLinkedToDiseaseRelationship(ExposureEntityRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:EXP)-[:LINKED_TO]->(:DIS)`, represented with full class
    names as Exposure -> Disease. Generic linkage relation; interpret as associative rather than causal unless source
    evidence says otherwise.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["ExposureLinkedToDiseaseRelationship"]
    class_class_curie: ClassVar[str] = "okg:ExposureLinkedToDiseaseRelationship"
    class_name: ClassVar[str] = "ExposureLinkedToDiseaseRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.ExposureLinkedToDiseaseRelationship

    subject: Optional[Union[str, ExposureId]] = None
    object: Optional[Union[str, DiseaseId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, ExposureId):
            self.subject = ExposureId(self.subject)

        if self.object is not None and not isinstance(self.object, DiseaseId):
            self.object = DiseaseId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExposureHasParentExposureRelationship(HierarchyRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:EXP)-[:PARENT]->(:EXP)`, represented with full class names
    as Exposure -> Exposure. Parent-child hierarchy relationship from the source concept to a broader or parent
    concept in the same or related ontology.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["ExposureParentExposureRelationship"]
    class_class_curie: ClassVar[str] = "okg:ExposureParentExposureRelationship"
    class_name: ClassVar[str] = "ExposureHasParentExposureRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.ExposureHasParentExposureRelationship

    subject: Optional[Union[str, ExposureId]] = None
    object: Optional[Union[str, ExposureId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, ExposureId):
            self.subject = ExposureId(self.subject)

        if self.object is not None and not isinstance(self.object, ExposureId):
            self.object = ExposureId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExposureAssociatedWithGeneRelationship(ExposureEntityRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:EXP)-[:INTERACTS_WITH]->(:GEN)`, represented with full class
    names as Exposure -> Gene. Generic interaction or annotation-style relationship. Interpret according to the source
    and node pair; it may indicate interaction, membership, annotation, or functional context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["ExposureInteractsWithGeneRelationship"]
    class_class_curie: ClassVar[str] = "okg:ExposureInteractsWithGeneRelationship"
    class_name: ClassVar[str] = "ExposureAssociatedWithGeneRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.ExposureAssociatedWithGeneRelationship

    subject: Optional[Union[str, ExposureId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, ExposureId):
            self.subject = ExposureId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExposureAssociatedWithMolecularFunctionRelationship(ExposureEntityRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:EXP)-[:INTERACTS_WITH]->(:MFN)`, represented with full class
    names as Exposure -> MolecularFunction. Generic interaction or annotation-style relationship. Interpret according
    to the source and node pair; it may indicate interaction, membership, annotation, or functional context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["ExposureInteractsWithMolecularFunctionRelationship"]
    class_class_curie: ClassVar[str] = "okg:ExposureInteractsWithMolecularFunctionRelationship"
    class_name: ClassVar[str] = "ExposureAssociatedWithMolecularFunctionRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.ExposureAssociatedWithMolecularFunctionRelationship

    subject: Optional[Union[str, ExposureId]] = None
    object: Optional[Union[str, MolecularFunctionId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, ExposureId):
            self.subject = ExposureId(self.subject)

        if self.object is not None and not isinstance(self.object, MolecularFunctionId):
            self.object = MolecularFunctionId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneInteractsWithGeneRelationship(AssociationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:GEN)-[:INTERACTS_WITH]->(:GEN)`, represented with full class
    names as Gene -> Gene. Generic interaction or annotation-style relationship. Interpret according to the source and
    node pair; it may indicate interaction, membership, annotation, or functional context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["GeneInteractsWithGeneRelationship"]
    class_class_curie: ClassVar[str] = "okg:GeneInteractsWithGeneRelationship"
    class_name: ClassVar[str] = "GeneInteractsWithGeneRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.GeneInteractsWithGeneRelationship

    subject: Optional[Union[str, GeneId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, GeneId):
            self.subject = GeneId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MolecularFunctionEnabledByGeneRelationship(FunctionalAnnotationRelationship):
    """
    A molecular-function-to-gene relationship corresponding to Neo4j
    `(:MolecularFunction)-[:INTERACTS_WITH]->(:Gene)`. In the semantic view, interpret as the gene/gene product
    enabling or being annotated to the molecular function.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["MolecularFunctionInteractsWithGeneRelationship"]
    class_class_curie: ClassVar[str] = "okg:MolecularFunctionInteractsWithGeneRelationship"
    class_name: ClassVar[str] = "MolecularFunctionEnabledByGeneRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.MolecularFunctionEnabledByGeneRelationship

    subject: Optional[Union[str, MolecularFunctionId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, MolecularFunctionId):
            self.subject = MolecularFunctionId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MolecularFunctionIsSubclassOfRelationship(HierarchyRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:MFN)-[:IS_A]->(:MFN)`, represented with full class names as
    MolecularFunction -> MolecularFunction. Ontology subclass relationship indicating the source concept is a kind of
    the target concept.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["MolecularFunctionIsAMolecularFunctionRelationship"]
    class_class_curie: ClassVar[str] = "okg:MolecularFunctionIsAMolecularFunctionRelationship"
    class_name: ClassVar[str] = "MolecularFunctionIsSubclassOfRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.MolecularFunctionIsSubclassOfRelationship

    subject: Optional[Union[str, MolecularFunctionId]] = None
    object: Optional[Union[str, MolecularFunctionId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, MolecularFunctionId):
            self.subject = MolecularFunctionId(self.subject)

        if self.object is not None and not isinstance(self.object, MolecularFunctionId):
            self.object = MolecularFunctionId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhenotypeHasParentDiseaseRelationship(PhenotypeHierarchyRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:PHE)-[:PARENT]->(:DIS)`, represented with full class names
    as Phenotype -> Disease. Parent-child hierarchy relationship from the source concept to a broader or parent
    concept in the same or related ontology.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["PhenotypeParentDiseaseRelationship"]
    class_class_curie: ClassVar[str] = "okg:PhenotypeParentDiseaseRelationship"
    class_name: ClassVar[str] = "PhenotypeHasParentDiseaseRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.PhenotypeHasParentDiseaseRelationship

    subject: Optional[Union[str, PhenotypeId]] = None
    object: Optional[Union[str, DiseaseId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, PhenotypeId):
            self.subject = PhenotypeId(self.subject)

        if self.object is not None and not isinstance(self.object, DiseaseId):
            self.object = DiseaseId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhenotypeAssociatedWithGeneRelationship(AssociationRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:PHE)-[:ASSOCIATED_WITH]->(:GEN)`, represented with full
    class names as Phenotype -> Gene. Association relationship; generally evidence-bearing but not necessarily causal.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["PhenotypeAssociatedWithGeneRelationship"]
    class_class_curie: ClassVar[str] = "okg:PhenotypeAssociatedWithGeneRelationship"
    class_name: ClassVar[str] = "PhenotypeAssociatedWithGeneRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.PhenotypeAssociatedWithGeneRelationship

    subject: Optional[Union[str, PhenotypeId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, PhenotypeId):
            self.subject = PhenotypeId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhenotypeHasParentPhenotypeRelationship(PhenotypeHierarchyRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:PHE)-[:PARENT]->(:PHE)`, represented with full class names
    as Phenotype -> Phenotype. Parent-child hierarchy relationship from the source concept to a broader or parent
    concept in the same or related ontology.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["PhenotypeParentPhenotypeRelationship"]
    class_class_curie: ClassVar[str] = "okg:PhenotypeParentPhenotypeRelationship"
    class_name: ClassVar[str] = "PhenotypeHasParentPhenotypeRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.PhenotypeHasParentPhenotypeRelationship

    subject: Optional[Union[str, PhenotypeId]] = None
    object: Optional[Union[str, PhenotypeId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, PhenotypeId):
            self.subject = PhenotypeId(self.subject)

        if self.object is not None and not isinstance(self.object, PhenotypeId):
            self.object = PhenotypeId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PathwayHasMemberGeneRelationship(FunctionalAnnotationRelationship):
    """
    A pathway-to-gene relationship corresponding to Neo4j `(:Pathway)-[:INTERACTS_WITH]->(:Gene)`. In the semantic
    view, interpret as pathway membership/participation rather than a generic interaction.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["PathwayInteractsWithGeneRelationship"]
    class_class_curie: ClassVar[str] = "okg:PathwayInteractsWithGeneRelationship"
    class_name: ClassVar[str] = "PathwayHasMemberGeneRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.PathwayHasMemberGeneRelationship

    subject: Optional[Union[str, PathwayId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, PathwayId):
            self.subject = PathwayId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PathwayHasParentPathwayRelationship(HierarchyRelationship):
    """
    Reified schema class for the current Neo4j pattern `(:PWY)-[:PARENT]->(:PWY)`, represented with full class names
    as Pathway -> Pathway. Parent-child hierarchy relationship from the source concept to a broader or parent concept
    in the same or related ontology.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["PathwayParentPathwayRelationship"]
    class_class_curie: ClassVar[str] = "okg:PathwayParentPathwayRelationship"
    class_name: ClassVar[str] = "PathwayHasParentPathwayRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.PathwayHasParentPathwayRelationship

    subject: Optional[Union[str, PathwayId]] = None
    object: Optional[Union[str, PathwayId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, PathwayId):
            self.subject = PathwayId(self.subject)

        if self.object is not None and not isinstance(self.object, PathwayId):
            self.object = PathwayId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DiseaseHasMolecularSubtypeConcreteRelationship(MolecularSubtypeRelationship):
    """
    Reified schema class for the Neo4j pattern `(:DIS)-[:HAS_MOLECULAR_SUBTYPE]->(:MST)`, represented with full class
    names as Disease -> MolecularSubtype. Indicates that a disease node is associated with a transcriptome-derived
    molecular subtype. This is a cross-cutting classification relationship, not an ontological subclass assertion.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["DiseaseHasMolecularSubtypeRelationship"]
    class_class_curie: ClassVar[str] = "okg:DiseaseHasMolecularSubtypeRelationship"
    class_name: ClassVar[str] = "DiseaseHasMolecularSubtypeConcreteRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DiseaseHasMolecularSubtypeConcreteRelationship

    subject: Optional[Union[str, DiseaseId]] = None
    object: Optional[Union[str, MolecularSubtypeId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DiseaseId):
            self.subject = DiseaseId(self.subject)

        if self.object is not None and not isinstance(self.object, MolecularSubtypeId):
            self.object = MolecularSubtypeId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MolecularSubtypeHasParentDiseaseRelationship(HierarchyRelationship):
    """
    Reified schema class for the Neo4j pattern `(:MST)-[:PARENT]->(:DIS)`, represented with full class names as
    MolecularSubtype -> Disease. Anchors a molecular subtype node to its parent disease in the knowledge graph
    hierarchy. Reuses the existing PARENT relationship type for compatibility with disease DAG traversal patterns.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["MolecularSubtypeParentDiseaseRelationship"]
    class_class_curie: ClassVar[str] = "okg:MolecularSubtypeParentDiseaseRelationship"
    class_name: ClassVar[str] = "MolecularSubtypeHasParentDiseaseRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.MolecularSubtypeHasParentDiseaseRelationship

    subject: Optional[Union[str, MolecularSubtypeId]] = None
    object: Optional[Union[str, DiseaseId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, MolecularSubtypeId):
            self.subject = MolecularSubtypeId(self.subject)

        if self.object is not None and not isinstance(self.object, DiseaseId):
            self.object = DiseaseId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MolecularSubtypeMeasuredInAnatomyRelationship(MolecularSubtypeRelationship):
    """
    Reified schema class for the Neo4j pattern `(:MST)-[:MEASURED_IN]->(:ANA)`, represented with full class names as
    MolecularSubtype -> Anatomy. Indicates the tissue context in which a molecular subtype was characterized (e.g.
    motor cortex, spinal cord). ALS-TE is cortex-only in the current NYGC dataset; ALS-Ox and ALS-Glia have both
    cortex and cord characterizations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["MolecularSubtypeMeasuredInAnatomyRelationship"]
    class_class_curie: ClassVar[str] = "okg:MolecularSubtypeMeasuredInAnatomyRelationship"
    class_name: ClassVar[str] = "MolecularSubtypeMeasuredInAnatomyRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.MolecularSubtypeMeasuredInAnatomyRelationship

    subject: Optional[Union[str, MolecularSubtypeId]] = None
    object: Optional[Union[str, AnatomyId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, MolecularSubtypeId):
            self.subject = MolecularSubtypeId(self.subject)

        if self.object is not None and not isinstance(self.object, AnatomyId):
            self.object = AnatomyId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


class ProvenanceEntity(YAMLRoot):
    """
    Abstract root for schema infrastructure and provenance records. Subclasses document the origin, identity, and
    evidence lineage of graph content without themselves being biomedical knowledge entities. Replaces the former
    SemanticEntity grouping for non-entity classes. Children: DataSource, Publication, DatabaseAccession (+
    CrossReference), Synonym.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Entity"]
    class_class_curie: ClassVar[str] = "prov:Entity"
    class_name: ClassVar[str] = "ProvenanceEntity"
    class_model_uri: ClassVar[URIRef] = ALSKG.ProvenanceEntity


@dataclass(repr=False)
class Sources(YAMLRoot):
    """
    Provenance tracking struct present on every node and edge in OptimusKG. Distinguishes between datasets that
    directly contributed the entity (primary ingestors) and those referenced indirectly through aggregators. Example
    direct sources: Open Targets, DisGeNET, Bgee. Example indirect sources: ClinGen, PsyGeNET, UniProt (via Open
    Targets).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["Sources"]
    class_class_curie: ClassVar[str] = "alskg:Sources"
    class_name: ClassVar[str] = "Sources"
    class_model_uri: ClassVar[URIRef] = ALSKG.Sources

    direct: Optional[Union[str, list[str]]] = empty_list()
    indirect: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.direct, list):
            self.direct = [self.direct] if self.direct is not None else []
        self.direct = [v if isinstance(v, str) else str(v) for v in self.direct]

        if not isinstance(self.indirect, list):
            self.indirect = [self.indirect] if self.indirect is not None else []
        self.indirect = [v if isinstance(v, str) else str(v) for v in self.indirect]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OntologyMetadata(YAMLRoot):
    """
    Metadata about the source ontology for a node. Captured verbatim from the OWL or JSON ontology file header at
    ingestion time.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["OntologyMetadata"]
    class_class_curie: ClassVar[str] = "alskg:OntologyMetadata"
    class_name: ClassVar[str] = "OntologyMetadata"
    class_model_uri: ClassVar[URIRef] = ALSKG.OntologyMetadata

    id: Union[str, OntologyMetadataId] = None
    name: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    license: Optional[str] = None
    version: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OntologyMetadataId):
            self.id = OntologyMetadataId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.license is not None and not isinstance(self.license, str):
            self.license = str(self.license)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Protein(PhysicalEntity):
    """
    A protein or protein-level biological entity associated with or encoded by a Gene. This semantic-view class
    normalizes values that may appear in OptimusKG gene properties such as associated_proteins.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Protein"]
    class_class_curie: ClassVar[str] = "biolink:Protein"
    class_name: ClassVar[str] = "Protein"
    class_model_uri: ClassVar[URIRef] = ALSKG.Protein

    id: Union[str, ProteinId] = None
    name: Optional[str] = None
    has_database_accession: Optional[Union[Union[str, DatabaseAccessionId], list[Union[str, DatabaseAccessionId]]]] = empty_list()
    has_isoform: Optional[Union[Union[str, ProteinIsoformId], list[Union[str, ProteinIsoformId]]]] = empty_list()
    contributes_to_pathogenic_mechanism: Optional[Union[Union[str, PathogenicMechanismId], list[Union[str, PathogenicMechanismId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProteinId):
            self.id = ProteinId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.has_database_accession, list):
            self.has_database_accession = [self.has_database_accession] if self.has_database_accession is not None else []
        self.has_database_accession = [v if isinstance(v, DatabaseAccessionId) else DatabaseAccessionId(v) for v in self.has_database_accession]

        if not isinstance(self.has_isoform, list):
            self.has_isoform = [self.has_isoform] if self.has_isoform is not None else []
        self.has_isoform = [v if isinstance(v, ProteinIsoformId) else ProteinIsoformId(v) for v in self.has_isoform]

        if not isinstance(self.contributes_to_pathogenic_mechanism, list):
            self.contributes_to_pathogenic_mechanism = [self.contributes_to_pathogenic_mechanism] if self.contributes_to_pathogenic_mechanism is not None else []
        self.contributes_to_pathogenic_mechanism = [v if isinstance(v, PathogenicMechanismId) else PathogenicMechanismId(v) for v in self.contributes_to_pathogenic_mechanism]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProteinIsoform(Protein):
    """
    A specific protein isoform or translated product, for example an Ensembl protein accession that may represent a
    transcript-specific protein product.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["ProteinIsoform"]
    class_class_curie: ClassVar[str] = "alskg:ProteinIsoform"
    class_name: ClassVar[str] = "ProteinIsoform"
    class_model_uri: ClassVar[URIRef] = ALSKG.ProteinIsoform

    id: Union[str, ProteinIsoformId] = None
    name: Optional[str] = None
    has_database_accession: Optional[Union[Union[str, DatabaseAccessionId], list[Union[str, DatabaseAccessionId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProteinIsoformId):
            self.id = ProteinIsoformId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.has_database_accession, list):
            self.has_database_accession = [self.has_database_accession] if self.has_database_accession is not None else []
        self.has_database_accession = [v if isinstance(v, DatabaseAccessionId) else DatabaseAccessionId(v) for v in self.has_database_accession]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DatabaseAccession(ProvenanceEntity):
    """
    A database-specific identifier or accession for a biological entity. This class allows accessions to be modeled as
    nodes rather than JSON strings.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["DatabaseAccession"]
    class_class_curie: ClassVar[str] = "alskg:DatabaseAccession"
    class_name: ClassVar[str] = "DatabaseAccession"
    class_model_uri: ClassVar[URIRef] = ALSKG.DatabaseAccession

    id: Union[str, DatabaseAccessionId] = None
    accession: Optional[str] = None
    from_data_source: Optional[Union[str, DataSourceId]] = None
    version: Optional[str] = None
    status: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatabaseAccessionId):
            self.id = DatabaseAccessionId(self.id)

        if self.accession is not None and not isinstance(self.accession, str):
            self.accession = str(self.accession)

        if self.from_data_source is not None and not isinstance(self.from_data_source, DataSourceId):
            self.from_data_source = DataSourceId(self.from_data_source)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if self.status is not None and not isinstance(self.status, str):
            self.status = str(self.status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataSource(ProvenanceEntity):
    """
    A database, data resource, or source vocabulary contributing identifiers, evidence, or assertions to OptimusKG.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Entity"]
    class_class_curie: ClassVar[str] = "prov:Entity"
    class_name: ClassVar[str] = "DataSource"
    class_model_uri: ClassVar[URIRef] = ALSKG.DataSource

    id: Union[str, DataSourceId] = None
    name: Optional[str] = None
    source_type: Optional[str] = None
    url: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataSourceId):
            self.id = DataSourceId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.source_type is not None and not isinstance(self.source_type, str):
            self.source_type = str(self.source_type)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Publication(ProvenanceEntity):
    """
    A publication or bibliographic reference that supports an OptimusKG assertion or evidence item.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Publication"]
    class_class_curie: ClassVar[str] = "biolink:Publication"
    class_name: ClassVar[str] = "Publication"
    class_model_uri: ClassVar[URIRef] = ALSKG.Publication

    id: Union[str, PublicationId] = None
    name: Optional[str] = None
    pmid: Optional[str] = None
    doi: Optional[str] = None
    url: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublicationId):
            self.id = PublicationId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.pmid is not None and not isinstance(self.pmid, str):
            self.pmid = str(self.pmid)

        if self.doi is not None and not isinstance(self.doi, str):
            self.doi = str(self.doi)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EvidenceRecord(YAMLRoot):
    """
    A structured evidence item supporting a node, relationship, or knowledge statement in the semantic view.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["EvidenceType"]
    class_class_curie: ClassVar[str] = "biolink:EvidenceType"
    class_name: ClassVar[str] = "EvidenceRecord"
    class_model_uri: ClassVar[URIRef] = ALSKG.EvidenceRecord

    id: Union[str, EvidenceRecordId] = None
    evidence_type: Optional[str] = None
    confidence_score: Optional[float] = None
    has_publication: Optional[Union[Union[str, PublicationId], list[Union[str, PublicationId]]]] = empty_list()
    from_data_source: Optional[Union[str, DataSourceId]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EvidenceRecordId):
            self.id = EvidenceRecordId(self.id)

        if self.evidence_type is not None and not isinstance(self.evidence_type, str):
            self.evidence_type = str(self.evidence_type)

        if self.confidence_score is not None and not isinstance(self.confidence_score, float):
            self.confidence_score = float(self.confidence_score)

        if not isinstance(self.has_publication, list):
            self.has_publication = [self.has_publication] if self.has_publication is not None else []
        self.has_publication = [v if isinstance(v, PublicationId) else PublicationId(v) for v in self.has_publication]

        if self.from_data_source is not None and not isinstance(self.from_data_source, DataSourceId):
            self.from_data_source = DataSourceId(self.from_data_source)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Synonym(ProvenanceEntity):
    """
    A lexical synonym, alias, obsolete label, or alternate name with optional source attribution.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOS["altLabel"]
    class_class_curie: ClassVar[str] = "skos:altLabel"
    class_name: ClassVar[str] = "Synonym"
    class_model_uri: ClassVar[URIRef] = ALSKG.Synonym

    id: Union[str, SynonymId] = None
    name: Optional[str] = None
    synonym_scope: Optional[str] = None
    from_data_source: Optional[Union[str, DataSourceId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SynonymId):
            self.id = SynonymId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.synonym_scope is not None and not isinstance(self.synonym_scope, str):
            self.synonym_scope = str(self.synonym_scope)

        if self.from_data_source is not None and not isinstance(self.from_data_source, DataSourceId):
            self.from_data_source = DataSourceId(self.from_data_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CrossReference(DatabaseAccession):
    """
    A cross-reference from an OptimusKG entity to an external database or ontology identifier.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Attribute"]
    class_class_curie: ClassVar[str] = "biolink:Attribute"
    class_name: ClassVar[str] = "CrossReference"
    class_model_uri: ClassVar[URIRef] = ALSKG.CrossReference

    id: Union[str, CrossReferenceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CrossReferenceId):
            self.id = CrossReferenceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneHasExpressionContextRelationship(RelationshipAssertion):
    """
    Reified schema class for the Neo4j pattern `(:GEN)-[:HAS_EXPRESSION_CONTEXT]->(:GeneExpressionContext)`. Links a
    gene to a context node recording direction, molecular subtype, tissue, and provenance of a differential expression
    finding.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["GeneHasExpressionContextRelationship"]
    class_class_curie: ClassVar[str] = "okg:GeneHasExpressionContextRelationship"
    class_name: ClassVar[str] = "GeneHasExpressionContextRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.GeneHasExpressionContextRelationship

    subject: Optional[Union[str, GeneId]] = None
    object: Optional[Union[str, GeneExpressionContextId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, GeneId):
            self.subject = GeneId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneExpressionContextId):
            self.object = GeneExpressionContextId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExpressionContextInAnatomyRelationship(RelationshipAssertion):
    """
    Reified schema class for the Neo4j pattern `(:ECX)-[:IN_ANATOMY]->(:ANA)`. Links a GeneExpressionContext node to
    the tissue in which the differential expression was measured. Not present for iPSC cell model contexts without a
    corresponding anatomy node.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["ExpressionContextInAnatomyRelationship"]
    class_class_curie: ClassVar[str] = "okg:ExpressionContextInAnatomyRelationship"
    class_name: ClassVar[str] = "ExpressionContextInAnatomyRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.ExpressionContextInAnatomyRelationship

    subject: Optional[Union[str, GeneExpressionContextId]] = None
    object: Optional[Union[str, AnatomyId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, GeneExpressionContextId):
            self.subject = GeneExpressionContextId(self.subject)

        if self.object is not None and not isinstance(self.object, AnatomyId):
            self.object = AnatomyId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExpressionContextInMolecularSubtypeRelationship(RelationshipAssertion):
    """
    Reified schema class for the Neo4j pattern `(:ECX)-[:HAS_MOLECULAR_SUBTYPE]->(:MST)`. Links a
    GeneExpressionContext node to the molecular subtype whose transcriptomic signature the gene contributes to.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OKG["ExpressionContextInMolecularSubtypeRelationship"]
    class_class_curie: ClassVar[str] = "okg:ExpressionContextInMolecularSubtypeRelationship"
    class_name: ClassVar[str] = "ExpressionContextInMolecularSubtypeRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.ExpressionContextInMolecularSubtypeRelationship

    subject: Optional[Union[str, GeneExpressionContextId]] = None
    object: Optional[Union[str, MolecularSubtypeId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, GeneExpressionContextId):
            self.subject = GeneExpressionContextId(self.subject)

        if self.object is not None and not isinstance(self.object, MolecularSubtypeId):
            self.object = MolecularSubtypeId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AmyotrophicLateralSclerosis(Disease):
    """
    Amyotrophic lateral sclerosis as the focal disease class for ALS-KG. Use this class for the ALS disease node when
    extending OptimusKG; it may be represented by the same MONDO/DOID identifier used by the OptimusKG Disease node.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MONDO["0004976"]
    class_class_curie: ClassVar[str] = "MONDO:0004976"
    class_name: ClassVar[str] = "AmyotrophicLateralSclerosis"
    class_model_uri: ClassVar[URIRef] = ALSKG.AmyotrophicLateralSclerosis

    id: Union[str, AmyotrophicLateralSclerosisId] = None
    name: Optional[str] = None
    has_synonym: Optional[Union[Union[str, SynonymId], list[Union[str, SynonymId]]]] = empty_list()
    has_cross_reference: Optional[Union[Union[str, DatabaseAccessionId], list[Union[str, DatabaseAccessionId]]]] = empty_list()
    has_als_subtype: Optional[Union[Union[str, ALSSubtypeId], list[Union[str, ALSSubtypeId]]]] = empty_list()
    has_pathogenic_mechanism: Optional[Union[Union[str, PathogenicMechanismId], list[Union[str, PathogenicMechanismId]]]] = empty_list()
    has_phenotype_observation: Optional[Union[Union[str, PhenotypeObservationId], list[Union[str, PhenotypeObservationId]]]] = empty_list()
    affects_anatomy: Optional[Union[Union[str, AnatomyId], list[Union[str, AnatomyId]]]] = empty_list()
    involves_cell_type: Optional[Union[Union[str, CellTypeId], list[Union[str, CellTypeId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AmyotrophicLateralSclerosisId):
            self.id = AmyotrophicLateralSclerosisId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.has_synonym, list):
            self.has_synonym = [self.has_synonym] if self.has_synonym is not None else []
        self.has_synonym = [v if isinstance(v, SynonymId) else SynonymId(v) for v in self.has_synonym]

        if not isinstance(self.has_cross_reference, list):
            self.has_cross_reference = [self.has_cross_reference] if self.has_cross_reference is not None else []
        self.has_cross_reference = [v if isinstance(v, DatabaseAccessionId) else DatabaseAccessionId(v) for v in self.has_cross_reference]

        if not isinstance(self.has_als_subtype, list):
            self.has_als_subtype = [self.has_als_subtype] if self.has_als_subtype is not None else []
        self.has_als_subtype = [v if isinstance(v, ALSSubtypeId) else ALSSubtypeId(v) for v in self.has_als_subtype]

        if not isinstance(self.has_pathogenic_mechanism, list):
            self.has_pathogenic_mechanism = [self.has_pathogenic_mechanism] if self.has_pathogenic_mechanism is not None else []
        self.has_pathogenic_mechanism = [v if isinstance(v, PathogenicMechanismId) else PathogenicMechanismId(v) for v in self.has_pathogenic_mechanism]

        if not isinstance(self.has_phenotype_observation, list):
            self.has_phenotype_observation = [self.has_phenotype_observation] if self.has_phenotype_observation is not None else []
        self.has_phenotype_observation = [v if isinstance(v, PhenotypeObservationId) else PhenotypeObservationId(v) for v in self.has_phenotype_observation]

        if not isinstance(self.affects_anatomy, list):
            self.affects_anatomy = [self.affects_anatomy] if self.affects_anatomy is not None else []
        self.affects_anatomy = [v if isinstance(v, AnatomyId) else AnatomyId(v) for v in self.affects_anatomy]

        if not isinstance(self.involves_cell_type, list):
            self.involves_cell_type = [self.involves_cell_type] if self.involves_cell_type is not None else []
        self.involves_cell_type = [v if isinstance(v, CellTypeId) else CellTypeId(v) for v in self.involves_cell_type]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DiseaseSubtype(ClinicalEntity):
    """
    Abstract class for a subtype of a disease, including clinical, genetic, molecular, pathology, and
    progression-based subtypes.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["DiseaseSubtype"]
    class_class_curie: ClassVar[str] = "alskg:DiseaseSubtype"
    class_name: ClassVar[str] = "DiseaseSubtype"
    class_model_uri: ClassVar[URIRef] = ALSKG.DiseaseSubtype

    id: Union[str, DiseaseSubtypeId] = None
    name: Optional[str] = None
    is_subtype_of: Optional[Union[str, DiseaseId]] = None
    has_subtype_scheme: Optional[Union[Union[str, SubtypeSchemeId], list[Union[str, SubtypeSchemeId]]]] = empty_list()
    has_subtype_criterion: Optional[Union[Union[str, SubtypeCriterionId], list[Union[str, SubtypeCriterionId]]]] = empty_list()
    is_supported_by: Optional[Union[Union[str, EvidenceRecordId], list[Union[str, EvidenceRecordId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiseaseSubtypeId):
            self.id = DiseaseSubtypeId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.is_subtype_of is not None and not isinstance(self.is_subtype_of, DiseaseId):
            self.is_subtype_of = DiseaseId(self.is_subtype_of)

        if not isinstance(self.has_subtype_scheme, list):
            self.has_subtype_scheme = [self.has_subtype_scheme] if self.has_subtype_scheme is not None else []
        self.has_subtype_scheme = [v if isinstance(v, SubtypeSchemeId) else SubtypeSchemeId(v) for v in self.has_subtype_scheme]

        if not isinstance(self.has_subtype_criterion, list):
            self.has_subtype_criterion = [self.has_subtype_criterion] if self.has_subtype_criterion is not None else []
        self.has_subtype_criterion = [v if isinstance(v, SubtypeCriterionId) else SubtypeCriterionId(v) for v in self.has_subtype_criterion]

        if not isinstance(self.is_supported_by, list):
            self.is_supported_by = [self.is_supported_by] if self.is_supported_by is not None else []
        self.is_supported_by = [v if isinstance(v, EvidenceRecordId) else EvidenceRecordId(v) for v in self.is_supported_by]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ALSSubtype(DiseaseSubtype):
    """
    An ALS subtype defined by clinical onset, genotype, molecular signature, pathology, progression rate, anatomy,
    cell type, or another explicit subtype criterion.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["ALSSubtype"]
    class_class_curie: ClassVar[str] = "alskg:ALSSubtype"
    class_name: ClassVar[str] = "ALSSubtype"
    class_model_uri: ClassVar[URIRef] = ALSKG.ALSSubtype

    id: Union[str, ALSSubtypeId] = None
    name: Optional[str] = None
    is_subtype_of: Optional[Union[str, DiseaseId]] = None
    has_subtype_scheme: Optional[Union[Union[str, SubtypeSchemeId], list[Union[str, SubtypeSchemeId]]]] = empty_list()
    has_subtype_criterion: Optional[Union[Union[str, SubtypeCriterionId], list[Union[str, SubtypeCriterionId]]]] = empty_list()
    is_defined_by_gene: Optional[Union[Union[str, GeneId], list[Union[str, GeneId]]]] = empty_list()
    is_defined_by_variant: Optional[Union[Union[str, SequenceVariantId], list[Union[str, SequenceVariantId]]]] = empty_list()
    is_defined_by_pathogenic_mechanism: Optional[Union[Union[str, PathogenicMechanismId], list[Union[str, PathogenicMechanismId]]]] = empty_list()
    has_phenotype_observation: Optional[Union[Union[str, PhenotypeObservationId], list[Union[str, PhenotypeObservationId]]]] = empty_list()
    affects_anatomy: Optional[Union[Union[str, AnatomyId], list[Union[str, AnatomyId]]]] = empty_list()
    involves_cell_type: Optional[Union[Union[str, CellTypeId], list[Union[str, CellTypeId]]]] = empty_list()
    has_pathogenic_mechanism: Optional[Union[Union[str, PathogenicMechanismId], list[Union[str, PathogenicMechanismId]]]] = empty_list()
    has_expression_result: Optional[Union[Union[str, DifferentialExpressionStatementId], list[Union[str, DifferentialExpressionStatementId]]]] = empty_list()
    is_supported_by: Optional[Union[Union[str, EvidenceRecordId], list[Union[str, EvidenceRecordId]]]] = empty_list()
    als_subtype_is_subtype_of_disease: Optional[Union[str, DiseaseId]] = None
    als_subtype_has_subtype_scheme: Optional[Union[str, SubtypeSchemeId]] = None
    als_subtype_has_subtype_criterion: Optional[Union[str, SubtypeCriterionId]] = None
    als_subtype_defined_by_gene: Optional[Union[str, GeneId]] = None
    als_subtype_defined_by_variant: Optional[Union[str, SequenceVariantId]] = None
    als_subtype_has_pathogenic_mechanism: Optional[Union[str, PathogenicMechanismId]] = None
    als_subtype_affects_anatomy: Optional[Union[str, AnatomyId]] = None
    als_subtype_involves_cell_type: Optional[Union[str, CellTypeId]] = None
    als_subtype_has_phenotype_observation: Optional[Union[str, PhenotypeObservationId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ALSSubtypeId):
            self.id = ALSSubtypeId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.is_subtype_of is not None and not isinstance(self.is_subtype_of, DiseaseId):
            self.is_subtype_of = DiseaseId(self.is_subtype_of)

        if not isinstance(self.has_subtype_scheme, list):
            self.has_subtype_scheme = [self.has_subtype_scheme] if self.has_subtype_scheme is not None else []
        self.has_subtype_scheme = [v if isinstance(v, SubtypeSchemeId) else SubtypeSchemeId(v) for v in self.has_subtype_scheme]

        if not isinstance(self.has_subtype_criterion, list):
            self.has_subtype_criterion = [self.has_subtype_criterion] if self.has_subtype_criterion is not None else []
        self.has_subtype_criterion = [v if isinstance(v, SubtypeCriterionId) else SubtypeCriterionId(v) for v in self.has_subtype_criterion]

        if not isinstance(self.is_defined_by_gene, list):
            self.is_defined_by_gene = [self.is_defined_by_gene] if self.is_defined_by_gene is not None else []
        self.is_defined_by_gene = [v if isinstance(v, GeneId) else GeneId(v) for v in self.is_defined_by_gene]

        if not isinstance(self.is_defined_by_variant, list):
            self.is_defined_by_variant = [self.is_defined_by_variant] if self.is_defined_by_variant is not None else []
        self.is_defined_by_variant = [v if isinstance(v, SequenceVariantId) else SequenceVariantId(v) for v in self.is_defined_by_variant]

        if not isinstance(self.is_defined_by_pathogenic_mechanism, list):
            self.is_defined_by_pathogenic_mechanism = [self.is_defined_by_pathogenic_mechanism] if self.is_defined_by_pathogenic_mechanism is not None else []
        self.is_defined_by_pathogenic_mechanism = [v if isinstance(v, PathogenicMechanismId) else PathogenicMechanismId(v) for v in self.is_defined_by_pathogenic_mechanism]

        if not isinstance(self.has_phenotype_observation, list):
            self.has_phenotype_observation = [self.has_phenotype_observation] if self.has_phenotype_observation is not None else []
        self.has_phenotype_observation = [v if isinstance(v, PhenotypeObservationId) else PhenotypeObservationId(v) for v in self.has_phenotype_observation]

        if not isinstance(self.affects_anatomy, list):
            self.affects_anatomy = [self.affects_anatomy] if self.affects_anatomy is not None else []
        self.affects_anatomy = [v if isinstance(v, AnatomyId) else AnatomyId(v) for v in self.affects_anatomy]

        if not isinstance(self.involves_cell_type, list):
            self.involves_cell_type = [self.involves_cell_type] if self.involves_cell_type is not None else []
        self.involves_cell_type = [v if isinstance(v, CellTypeId) else CellTypeId(v) for v in self.involves_cell_type]

        if not isinstance(self.has_pathogenic_mechanism, list):
            self.has_pathogenic_mechanism = [self.has_pathogenic_mechanism] if self.has_pathogenic_mechanism is not None else []
        self.has_pathogenic_mechanism = [v if isinstance(v, PathogenicMechanismId) else PathogenicMechanismId(v) for v in self.has_pathogenic_mechanism]

        if not isinstance(self.has_expression_result, list):
            self.has_expression_result = [self.has_expression_result] if self.has_expression_result is not None else []
        self.has_expression_result = [v if isinstance(v, DifferentialExpressionStatementId) else DifferentialExpressionStatementId(v) for v in self.has_expression_result]

        if not isinstance(self.is_supported_by, list):
            self.is_supported_by = [self.is_supported_by] if self.is_supported_by is not None else []
        self.is_supported_by = [v if isinstance(v, EvidenceRecordId) else EvidenceRecordId(v) for v in self.is_supported_by]

        if self.als_subtype_is_subtype_of_disease is not None and not isinstance(self.als_subtype_is_subtype_of_disease, DiseaseId):
            self.als_subtype_is_subtype_of_disease = DiseaseId(self.als_subtype_is_subtype_of_disease)

        if self.als_subtype_has_subtype_scheme is not None and not isinstance(self.als_subtype_has_subtype_scheme, SubtypeSchemeId):
            self.als_subtype_has_subtype_scheme = SubtypeSchemeId(self.als_subtype_has_subtype_scheme)

        if self.als_subtype_has_subtype_criterion is not None and not isinstance(self.als_subtype_has_subtype_criterion, SubtypeCriterionId):
            self.als_subtype_has_subtype_criterion = SubtypeCriterionId(self.als_subtype_has_subtype_criterion)

        if self.als_subtype_defined_by_gene is not None and not isinstance(self.als_subtype_defined_by_gene, GeneId):
            self.als_subtype_defined_by_gene = GeneId(self.als_subtype_defined_by_gene)

        if self.als_subtype_defined_by_variant is not None and not isinstance(self.als_subtype_defined_by_variant, SequenceVariantId):
            self.als_subtype_defined_by_variant = SequenceVariantId(self.als_subtype_defined_by_variant)

        if self.als_subtype_has_pathogenic_mechanism is not None and not isinstance(self.als_subtype_has_pathogenic_mechanism, PathogenicMechanismId):
            self.als_subtype_has_pathogenic_mechanism = PathogenicMechanismId(self.als_subtype_has_pathogenic_mechanism)

        if self.als_subtype_affects_anatomy is not None and not isinstance(self.als_subtype_affects_anatomy, AnatomyId):
            self.als_subtype_affects_anatomy = AnatomyId(self.als_subtype_affects_anatomy)

        if self.als_subtype_involves_cell_type is not None and not isinstance(self.als_subtype_involves_cell_type, CellTypeId):
            self.als_subtype_involves_cell_type = CellTypeId(self.als_subtype_involves_cell_type)

        if self.als_subtype_has_phenotype_observation is not None and not isinstance(self.als_subtype_has_phenotype_observation, PhenotypeObservationId):
            self.als_subtype_has_phenotype_observation = PhenotypeObservationId(self.als_subtype_has_phenotype_observation)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MolecularSubtype(ALSSubtype):
    """
    A molecular ALS subtype defined by transcriptomic, multi-omic, pathology-associated, or computational evidence.
    This class preserves compatibility with the current Neo4j `MST` label while making MolecularSubtype a proper
    subclass of ALSSubtype.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["MolecularSubtype"]
    class_class_curie: ClassVar[str] = "alskg:MolecularSubtype"
    class_name: ClassVar[str] = "MolecularSubtype"
    class_model_uri: ClassVar[URIRef] = ALSKG.MolecularSubtype

    id: Union[str, MolecularSubtypeId] = None
    name: Optional[str] = None
    original_optimus_label: Optional[str] = None
    direct_sources: Optional[Union[str, list[str]]] = empty_list()
    indirect_sources: Optional[Union[str, list[str]]] = empty_list()
    has_synonym: Optional[Union[Union[str, SynonymId], list[Union[str, SynonymId]]]] = empty_list()
    has_cross_reference: Optional[Union[Union[str, DatabaseAccessionId], list[Union[str, DatabaseAccessionId]]]] = empty_list()
    has_subtype_scheme: Optional[Union[Union[str, SubtypeSchemeId], list[Union[str, SubtypeSchemeId]]]] = empty_list()
    has_subtype_criterion: Optional[Union[Union[str, SubtypeCriterionId], list[Union[str, SubtypeCriterionId]]]] = empty_list()
    has_pathogenic_mechanism: Optional[Union[Union[str, PathogenicMechanismId], list[Union[str, PathogenicMechanismId]]]] = empty_list()
    affects_anatomy: Optional[Union[Union[str, AnatomyId], list[Union[str, AnatomyId]]]] = empty_list()
    involves_cell_type: Optional[Union[Union[str, CellTypeId], list[Union[str, CellTypeId]]]] = empty_list()
    is_supported_by: Optional[Union[Union[str, EvidenceRecordId], list[Union[str, EvidenceRecordId]]]] = empty_list()
    has_phenotype_observation: Optional[Union[Union[str, PhenotypeObservationId], list[Union[str, PhenotypeObservationId]]]] = empty_list()
    has_expression_result: Optional[Union[Union[str, DifferentialExpressionStatementId], list[Union[str, DifferentialExpressionStatementId]]]] = empty_list()
    full_name: Optional[str] = None
    defining_mechanism: Optional[str] = None
    key_pathways: Optional[Union[str, list[str]]] = empty_list()
    classification_basis: Optional[Union[str, "MolecularSubtypeClassificationBasisEnum"]] = None
    tissue_origin: Optional[Union[str, list[str]]] = empty_list()
    prevalence_pct: Optional[float] = None
    survival_months_median: Optional[float] = None
    onset_age_mean: Optional[float] = None
    prognosis_note: Optional[str] = None
    cohort: Optional[str] = None
    pubmed_id: Optional[str] = None
    label_color: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MolecularSubtypeId):
            self.id = MolecularSubtypeId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.original_optimus_label is not None and not isinstance(self.original_optimus_label, str):
            self.original_optimus_label = str(self.original_optimus_label)

        if not isinstance(self.direct_sources, list):
            self.direct_sources = [self.direct_sources] if self.direct_sources is not None else []
        self.direct_sources = [v if isinstance(v, str) else str(v) for v in self.direct_sources]

        if not isinstance(self.indirect_sources, list):
            self.indirect_sources = [self.indirect_sources] if self.indirect_sources is not None else []
        self.indirect_sources = [v if isinstance(v, str) else str(v) for v in self.indirect_sources]

        if not isinstance(self.has_synonym, list):
            self.has_synonym = [self.has_synonym] if self.has_synonym is not None else []
        self.has_synonym = [v if isinstance(v, SynonymId) else SynonymId(v) for v in self.has_synonym]

        if not isinstance(self.has_cross_reference, list):
            self.has_cross_reference = [self.has_cross_reference] if self.has_cross_reference is not None else []
        self.has_cross_reference = [v if isinstance(v, DatabaseAccessionId) else DatabaseAccessionId(v) for v in self.has_cross_reference]

        if not isinstance(self.has_subtype_scheme, list):
            self.has_subtype_scheme = [self.has_subtype_scheme] if self.has_subtype_scheme is not None else []
        self.has_subtype_scheme = [v if isinstance(v, SubtypeSchemeId) else SubtypeSchemeId(v) for v in self.has_subtype_scheme]

        if not isinstance(self.has_subtype_criterion, list):
            self.has_subtype_criterion = [self.has_subtype_criterion] if self.has_subtype_criterion is not None else []
        self.has_subtype_criterion = [v if isinstance(v, SubtypeCriterionId) else SubtypeCriterionId(v) for v in self.has_subtype_criterion]

        if not isinstance(self.has_pathogenic_mechanism, list):
            self.has_pathogenic_mechanism = [self.has_pathogenic_mechanism] if self.has_pathogenic_mechanism is not None else []
        self.has_pathogenic_mechanism = [v if isinstance(v, PathogenicMechanismId) else PathogenicMechanismId(v) for v in self.has_pathogenic_mechanism]

        if not isinstance(self.affects_anatomy, list):
            self.affects_anatomy = [self.affects_anatomy] if self.affects_anatomy is not None else []
        self.affects_anatomy = [v if isinstance(v, AnatomyId) else AnatomyId(v) for v in self.affects_anatomy]

        if not isinstance(self.involves_cell_type, list):
            self.involves_cell_type = [self.involves_cell_type] if self.involves_cell_type is not None else []
        self.involves_cell_type = [v if isinstance(v, CellTypeId) else CellTypeId(v) for v in self.involves_cell_type]

        if not isinstance(self.is_supported_by, list):
            self.is_supported_by = [self.is_supported_by] if self.is_supported_by is not None else []
        self.is_supported_by = [v if isinstance(v, EvidenceRecordId) else EvidenceRecordId(v) for v in self.is_supported_by]

        if not isinstance(self.has_phenotype_observation, list):
            self.has_phenotype_observation = [self.has_phenotype_observation] if self.has_phenotype_observation is not None else []
        self.has_phenotype_observation = [v if isinstance(v, PhenotypeObservationId) else PhenotypeObservationId(v) for v in self.has_phenotype_observation]

        if not isinstance(self.has_expression_result, list):
            self.has_expression_result = [self.has_expression_result] if self.has_expression_result is not None else []
        self.has_expression_result = [v if isinstance(v, DifferentialExpressionStatementId) else DifferentialExpressionStatementId(v) for v in self.has_expression_result]

        if self.full_name is not None and not isinstance(self.full_name, str):
            self.full_name = str(self.full_name)

        if self.defining_mechanism is not None and not isinstance(self.defining_mechanism, str):
            self.defining_mechanism = str(self.defining_mechanism)

        if not isinstance(self.key_pathways, list):
            self.key_pathways = [self.key_pathways] if self.key_pathways is not None else []
        self.key_pathways = [v if isinstance(v, str) else str(v) for v in self.key_pathways]

        if self.classification_basis is not None and not isinstance(self.classification_basis, MolecularSubtypeClassificationBasisEnum):
            self.classification_basis = MolecularSubtypeClassificationBasisEnum(self.classification_basis)

        if not isinstance(self.tissue_origin, list):
            self.tissue_origin = [self.tissue_origin] if self.tissue_origin is not None else []
        self.tissue_origin = [v if isinstance(v, str) else str(v) for v in self.tissue_origin]

        if self.prevalence_pct is not None and not isinstance(self.prevalence_pct, float):
            self.prevalence_pct = float(self.prevalence_pct)

        if self.survival_months_median is not None and not isinstance(self.survival_months_median, float):
            self.survival_months_median = float(self.survival_months_median)

        if self.onset_age_mean is not None and not isinstance(self.onset_age_mean, float):
            self.onset_age_mean = float(self.onset_age_mean)

        if self.prognosis_note is not None and not isinstance(self.prognosis_note, str):
            self.prognosis_note = str(self.prognosis_note)

        if self.cohort is not None and not isinstance(self.cohort, str):
            self.cohort = str(self.cohort)

        if self.pubmed_id is not None and not isinstance(self.pubmed_id, str):
            self.pubmed_id = str(self.pubmed_id)

        if self.label_color is not None and not isinstance(self.label_color, str):
            self.label_color = str(self.label_color)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ClinicalSubtype(ALSSubtype):
    """
    ALS subtype defined primarily by clinical presentation, such as bulbar-onset ALS, limb-onset ALS, ALS-FTD,
    upper-motor-neuron-predominant ALS, or lower-motor-neuron-predominant ALS.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["ClinicalSubtype"]
    class_class_curie: ClassVar[str] = "alskg:ClinicalSubtype"
    class_name: ClassVar[str] = "ClinicalSubtype"
    class_model_uri: ClassVar[URIRef] = ALSKG.ClinicalSubtype

    id: Union[str, ClinicalSubtypeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ClinicalSubtypeId):
            self.id = ClinicalSubtypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneticSubtype(ALSSubtype):
    """
    ALS subtype defined by a causal, risk-associated, or clinically meaningful gene/variant, such as SOD1-ALS,
    C9orf72-ALS, TARDBP-ALS, or FUS-ALS.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["GeneticSubtype"]
    class_class_curie: ClassVar[str] = "alskg:GeneticSubtype"
    class_name: ClassVar[str] = "GeneticSubtype"
    class_model_uri: ClassVar[URIRef] = ALSKG.GeneticSubtype

    id: Union[str, GeneticSubtypeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneticSubtypeId):
            self.id = GeneticSubtypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PathologySubtype(ALSSubtype):
    """
    ALS subtype defined by pathology or proteinopathy pattern, such as TDP-43 pathology or SOD1 aggregation pattern.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["PathologySubtype"]
    class_class_curie: ClassVar[str] = "alskg:PathologySubtype"
    class_name: ClassVar[str] = "PathologySubtype"
    class_model_uri: ClassVar[URIRef] = ALSKG.PathologySubtype

    id: Union[str, PathologySubtypeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PathologySubtypeId):
            self.id = PathologySubtypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProgressionSubtype(ALSSubtype):
    """
    ALS subtype defined by disease progression trajectory, such as fast-progressor, slow-progressor, or
    respiratory-onset progression pattern.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["ProgressionSubtype"]
    class_class_curie: ClassVar[str] = "alskg:ProgressionSubtype"
    class_name: ClassVar[str] = "ProgressionSubtype"
    class_model_uri: ClassVar[URIRef] = ALSKG.ProgressionSubtype

    id: Union[str, ProgressionSubtypeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProgressionSubtypeId):
            self.id = ProgressionSubtypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SubtypeScheme(AnalyticalEntity):
    """
    A scheme or taxonomy used to classify ALS subtypes, such as clinical-onset subtype, ALS-OPM motor phenotype,
    genotype subtype, molecular cluster, pathology subtype, or progression subtype.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["SubtypeScheme"]
    class_class_curie: ClassVar[str] = "alskg:SubtypeScheme"
    class_name: ClassVar[str] = "SubtypeScheme"
    class_model_uri: ClassVar[URIRef] = ALSKG.SubtypeScheme

    id: Union[str, SubtypeSchemeId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    from_data_source: Optional[Union[str, DataSourceId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SubtypeSchemeId):
            self.id = SubtypeSchemeId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.from_data_source is not None and not isinstance(self.from_data_source, DataSourceId):
            self.from_data_source = DataSourceId(self.from_data_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SubtypeCriterion(AnalyticalEntity):
    """
    A criterion used to assign or define an ALS subtype, such as a gene variant, symptom pattern, anatomical onset
    region, transcriptomic signature, pathology feature, or progression threshold.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["SubtypeCriterion"]
    class_class_curie: ClassVar[str] = "alskg:SubtypeCriterion"
    class_name: ClassVar[str] = "SubtypeCriterion"
    class_model_uri: ClassVar[URIRef] = ALSKG.SubtypeCriterion

    id: Union[str, SubtypeCriterionId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    is_supported_by: Optional[Union[Union[str, EvidenceRecordId], list[Union[str, EvidenceRecordId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SubtypeCriterionId):
            self.id = SubtypeCriterionId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.is_supported_by, list):
            self.is_supported_by = [self.is_supported_by] if self.is_supported_by is not None else []
        self.is_supported_by = [v if isinstance(v, EvidenceRecordId) else EvidenceRecordId(v) for v in self.is_supported_by]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SequenceVariant(PhysicalEntity):
    """
    A genomic sequence variant relevant to ALS, including SNVs, indels, structural variants, copy number changes, and
    repeat expansions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SO["0001060"]
    class_class_curie: ClassVar[str] = "SO:0001060"
    class_name: ClassVar[str] = "SequenceVariant"
    class_model_uri: ClassVar[URIRef] = ALSKG.SequenceVariant

    id: Union[str, SequenceVariantId] = None
    name: Optional[str] = None
    has_variant_type: Optional[str] = None
    has_pathogenicity: Optional[Union[str, "PathogenicityEnum"]] = None
    affects_gene: Optional[Union[Union[str, GeneId], list[Union[str, GeneId]]]] = empty_list()
    alters_protein: Optional[Union[Union[str, ProteinId], list[Union[str, ProteinId]]]] = empty_list()
    is_supported_by: Optional[Union[Union[str, EvidenceRecordId], list[Union[str, EvidenceRecordId]]]] = empty_list()
    variant_affects_gene: Optional[Union[str, GeneId]] = None
    variant_alters_protein: Optional[Union[str, ProteinId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SequenceVariantId):
            self.id = SequenceVariantId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.has_variant_type is not None and not isinstance(self.has_variant_type, str):
            self.has_variant_type = str(self.has_variant_type)

        if self.has_pathogenicity is not None and not isinstance(self.has_pathogenicity, PathogenicityEnum):
            self.has_pathogenicity = PathogenicityEnum(self.has_pathogenicity)

        if not isinstance(self.affects_gene, list):
            self.affects_gene = [self.affects_gene] if self.affects_gene is not None else []
        self.affects_gene = [v if isinstance(v, GeneId) else GeneId(v) for v in self.affects_gene]

        if not isinstance(self.alters_protein, list):
            self.alters_protein = [self.alters_protein] if self.alters_protein is not None else []
        self.alters_protein = [v if isinstance(v, ProteinId) else ProteinId(v) for v in self.alters_protein]

        if not isinstance(self.is_supported_by, list):
            self.is_supported_by = [self.is_supported_by] if self.is_supported_by is not None else []
        self.is_supported_by = [v if isinstance(v, EvidenceRecordId) else EvidenceRecordId(v) for v in self.is_supported_by]

        if self.variant_affects_gene is not None and not isinstance(self.variant_affects_gene, GeneId):
            self.variant_affects_gene = GeneId(self.variant_affects_gene)

        if self.variant_alters_protein is not None and not isinstance(self.variant_alters_protein, ProteinId):
            self.variant_alters_protein = ProteinId(self.variant_alters_protein)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RepeatExpansion(SequenceVariant):
    """
    A repeat expansion variant, such as the C9orf72 hexanucleotide repeat expansion associated with ALS/FTD.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SO["0002165"]
    class_class_curie: ClassVar[str] = "SO:0002165"
    class_name: ClassVar[str] = "RepeatExpansion"
    class_model_uri: ClassVar[URIRef] = ALSKG.RepeatExpansion

    id: Union[str, RepeatExpansionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RepeatExpansionId):
            self.id = RepeatExpansionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CellType(OntologyClass):
    """
    A cell type relevant to ALS biology, such as upper motor neuron, lower motor neuron, astrocyte, microglia,
    oligodendrocyte, skeletal muscle cell, or immune cell. Prefer Cell Ontology CURIEs when available.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Cell"]
    class_class_curie: ClassVar[str] = "biolink:Cell"
    class_name: ClassVar[str] = "CellType"
    class_model_uri: ClassVar[URIRef] = ALSKG.CellType

    id: Union[str, CellTypeId] = None
    name: Optional[str] = None
    has_synonym: Optional[Union[Union[str, SynonymId], list[Union[str, SynonymId]]]] = empty_list()
    has_cross_reference: Optional[Union[Union[str, DatabaseAccessionId], list[Union[str, DatabaseAccessionId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellTypeId):
            self.id = CellTypeId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.has_synonym, list):
            self.has_synonym = [self.has_synonym] if self.has_synonym is not None else []
        self.has_synonym = [v if isinstance(v, SynonymId) else SynonymId(v) for v in self.has_synonym]

        if not isinstance(self.has_cross_reference, list):
            self.has_cross_reference = [self.has_cross_reference] if self.has_cross_reference is not None else []
        self.has_cross_reference = [v if isinstance(v, DatabaseAccessionId) else DatabaseAccessionId(v) for v in self.has_cross_reference]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PathogenicMechanism(AnalyticalEntity):
    """
    A biological mechanism that contributes to ALS initiation, progression, cellular dysfunction, or phenotype, such
    as TDP-43 proteinopathy, SOD1 toxic gain of function, C9orf72 repeat expansion toxicity, impaired RNA metabolism,
    mitochondrial dysfunction, oxidative stress, neuroinflammation, excitotoxicity, or impaired proteostasis.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["PathogenicMechanism"]
    class_class_curie: ClassVar[str] = "alskg:PathogenicMechanism"
    class_name: ClassVar[str] = "PathogenicMechanism"
    class_model_uri: ClassVar[URIRef] = ALSKG.PathogenicMechanism

    id: Union[str, PathogenicMechanismId] = None
    name: Optional[str] = None
    has_pathogenic_mechanism_category: Optional[Union[str, "PathogenicMechanismEnum"]] = None
    involves_biological_process: Optional[Union[Union[str, BiologicalProcessId], list[Union[str, BiologicalProcessId]]]] = empty_list()
    involves_molecular_function: Optional[Union[Union[str, MolecularFunctionId], list[Union[str, MolecularFunctionId]]]] = empty_list()
    affects_anatomy: Optional[Union[Union[str, AnatomyId], list[Union[str, AnatomyId]]]] = empty_list()
    involves_cell_type: Optional[Union[Union[str, CellTypeId], list[Union[str, CellTypeId]]]] = empty_list()
    is_supported_by: Optional[Union[Union[str, EvidenceRecordId], list[Union[str, EvidenceRecordId]]]] = empty_list()
    pathogenic_mechanism_occurs_in_cell_type: Optional[Union[str, CellTypeId]] = None
    pathogenic_mechanism_occurs_in_anatomy: Optional[Union[str, AnatomyId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PathogenicMechanismId):
            self.id = PathogenicMechanismId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.has_pathogenic_mechanism_category is not None and not isinstance(self.has_pathogenic_mechanism_category, PathogenicMechanismEnum):
            self.has_pathogenic_mechanism_category = PathogenicMechanismEnum(self.has_pathogenic_mechanism_category)

        if not isinstance(self.involves_biological_process, list):
            self.involves_biological_process = [self.involves_biological_process] if self.involves_biological_process is not None else []
        self.involves_biological_process = [v if isinstance(v, BiologicalProcessId) else BiologicalProcessId(v) for v in self.involves_biological_process]

        if not isinstance(self.involves_molecular_function, list):
            self.involves_molecular_function = [self.involves_molecular_function] if self.involves_molecular_function is not None else []
        self.involves_molecular_function = [v if isinstance(v, MolecularFunctionId) else MolecularFunctionId(v) for v in self.involves_molecular_function]

        if not isinstance(self.affects_anatomy, list):
            self.affects_anatomy = [self.affects_anatomy] if self.affects_anatomy is not None else []
        self.affects_anatomy = [v if isinstance(v, AnatomyId) else AnatomyId(v) for v in self.affects_anatomy]

        if not isinstance(self.involves_cell_type, list):
            self.involves_cell_type = [self.involves_cell_type] if self.involves_cell_type is not None else []
        self.involves_cell_type = [v if isinstance(v, CellTypeId) else CellTypeId(v) for v in self.involves_cell_type]

        if not isinstance(self.is_supported_by, list):
            self.is_supported_by = [self.is_supported_by] if self.is_supported_by is not None else []
        self.is_supported_by = [v if isinstance(v, EvidenceRecordId) else EvidenceRecordId(v) for v in self.is_supported_by]

        if self.pathogenic_mechanism_occurs_in_cell_type is not None and not isinstance(self.pathogenic_mechanism_occurs_in_cell_type, CellTypeId):
            self.pathogenic_mechanism_occurs_in_cell_type = CellTypeId(self.pathogenic_mechanism_occurs_in_cell_type)

        if self.pathogenic_mechanism_occurs_in_anatomy is not None and not isinstance(self.pathogenic_mechanism_occurs_in_anatomy, AnatomyId):
            self.pathogenic_mechanism_occurs_in_anatomy = AnatomyId(self.pathogenic_mechanism_occurs_in_anatomy)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MolecularEvent(AnalyticalEntity):
    """
    A specific molecular event involved in ALS pathogenesis, such as TDP-43 nuclear depletion, cytoplasmic
    aggregation, altered splicing, repeat RNA foci formation, DPR protein accumulation, mitochondrial complex
    dysregulation, or complement activation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["MolecularEvent"]
    class_class_curie: ClassVar[str] = "alskg:MolecularEvent"
    class_name: ClassVar[str] = "MolecularEvent"
    class_model_uri: ClassVar[URIRef] = ALSKG.MolecularEvent

    id: Union[str, MolecularEventId] = None
    name: Optional[str] = None
    contributes_to_pathogenic_mechanism: Optional[Union[Union[str, PathogenicMechanismId], list[Union[str, PathogenicMechanismId]]]] = empty_list()
    is_supported_by: Optional[Union[Union[str, EvidenceRecordId], list[Union[str, EvidenceRecordId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MolecularEventId):
            self.id = MolecularEventId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.contributes_to_pathogenic_mechanism, list):
            self.contributes_to_pathogenic_mechanism = [self.contributes_to_pathogenic_mechanism] if self.contributes_to_pathogenic_mechanism is not None else []
        self.contributes_to_pathogenic_mechanism = [v if isinstance(v, PathogenicMechanismId) else PathogenicMechanismId(v) for v in self.contributes_to_pathogenic_mechanism]

        if not isinstance(self.is_supported_by, list):
            self.is_supported_by = [self.is_supported_by] if self.is_supported_by is not None else []
        self.is_supported_by = [v if isinstance(v, EvidenceRecordId) else EvidenceRecordId(v) for v in self.is_supported_by]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProteinAggregate(PhysicalEntity):
    """
    An abnormal protein aggregate or pathological inclusion relevant to ALS, such as phosphorylated TDP-43 inclusions,
    SOD1 aggregates, FUS inclusions, or dipeptide-repeat protein aggregates.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["ProteinAggregate"]
    class_class_curie: ClassVar[str] = "alskg:ProteinAggregate"
    class_name: ClassVar[str] = "ProteinAggregate"
    class_model_uri: ClassVar[URIRef] = ALSKG.ProteinAggregate

    id: Union[str, ProteinAggregateId] = None
    name: Optional[str] = None
    has_protein_component: Optional[Union[Union[str, ProteinId], list[Union[str, ProteinId]]]] = empty_list()
    occurs_in_cell_type: Optional[Union[Union[str, CellTypeId], list[Union[str, CellTypeId]]]] = empty_list()
    occurs_in_anatomy: Optional[Union[Union[str, AnatomyId], list[Union[str, AnatomyId]]]] = empty_list()
    is_supported_by: Optional[Union[Union[str, EvidenceRecordId], list[Union[str, EvidenceRecordId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProteinAggregateId):
            self.id = ProteinAggregateId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.has_protein_component, list):
            self.has_protein_component = [self.has_protein_component] if self.has_protein_component is not None else []
        self.has_protein_component = [v if isinstance(v, ProteinId) else ProteinId(v) for v in self.has_protein_component]

        if not isinstance(self.occurs_in_cell_type, list):
            self.occurs_in_cell_type = [self.occurs_in_cell_type] if self.occurs_in_cell_type is not None else []
        self.occurs_in_cell_type = [v if isinstance(v, CellTypeId) else CellTypeId(v) for v in self.occurs_in_cell_type]

        if not isinstance(self.occurs_in_anatomy, list):
            self.occurs_in_anatomy = [self.occurs_in_anatomy] if self.occurs_in_anatomy is not None else []
        self.occurs_in_anatomy = [v if isinstance(v, AnatomyId) else AnatomyId(v) for v in self.occurs_in_anatomy]

        if not isinstance(self.is_supported_by, list):
            self.is_supported_by = [self.is_supported_by] if self.is_supported_by is not None else []
        self.is_supported_by = [v if isinstance(v, EvidenceRecordId) else EvidenceRecordId(v) for v in self.is_supported_by]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EvidenceStatement(AnalyticalEntity):
    """
    A reified, evidence-backed assertion in ALS-KG. Use statement/result nodes when the claim depends on subtype,
    tissue, cell type, cohort, assay, statistical support, or publication evidence.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RDF["Statement"]
    class_class_curie: ClassVar[str] = "rdf:Statement"
    class_name: ClassVar[str] = "EvidenceStatement"
    class_model_uri: ClassVar[URIRef] = ALSKG.EvidenceStatement

    id: Union[str, EvidenceStatementId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    is_supported_by: Optional[Union[Union[str, EvidenceRecordId], list[Union[str, EvidenceRecordId]]]] = empty_list()
    derives_from_dataset: Optional[Union[str, DatasetId]] = None
    occurs_in_cohort: Optional[Union[str, CohortId]] = None
    confidence_score: Optional[float] = None
    evidence_statement_supported_by_evidence: Optional[Union[str, EvidenceRecordId]] = None
    evidence_statement_derives_from_dataset: Optional[Union[str, DatasetId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EvidenceStatementId):
            self.id = EvidenceStatementId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.is_supported_by, list):
            self.is_supported_by = [self.is_supported_by] if self.is_supported_by is not None else []
        self.is_supported_by = [v if isinstance(v, EvidenceRecordId) else EvidenceRecordId(v) for v in self.is_supported_by]

        if self.derives_from_dataset is not None and not isinstance(self.derives_from_dataset, DatasetId):
            self.derives_from_dataset = DatasetId(self.derives_from_dataset)

        if self.occurs_in_cohort is not None and not isinstance(self.occurs_in_cohort, CohortId):
            self.occurs_in_cohort = CohortId(self.occurs_in_cohort)

        if self.confidence_score is not None and not isinstance(self.confidence_score, float):
            self.confidence_score = float(self.confidence_score)

        if self.evidence_statement_supported_by_evidence is not None and not isinstance(self.evidence_statement_supported_by_evidence, EvidenceRecordId):
            self.evidence_statement_supported_by_evidence = EvidenceRecordId(self.evidence_statement_supported_by_evidence)

        if self.evidence_statement_derives_from_dataset is not None and not isinstance(self.evidence_statement_derives_from_dataset, DatasetId):
            self.evidence_statement_derives_from_dataset = DatasetId(self.evidence_statement_derives_from_dataset)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PathogenesisStatement(EvidenceStatement):
    """
    An evidence-backed assertion connecting a gene, variant, protein, molecular event, subtype, anatomy, or cell type
    to an ALS pathogenic mechanism.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["PathogenesisStatement"]
    class_class_curie: ClassVar[str] = "alskg:PathogenesisStatement"
    class_name: ClassVar[str] = "PathogenesisStatement"
    class_model_uri: ClassVar[URIRef] = ALSKG.PathogenesisStatement

    id: Union[str, PathogenesisStatementId] = None
    contributes_to_pathogenic_mechanism: Optional[Union[Union[str, PathogenicMechanismId], list[Union[str, PathogenicMechanismId]]]] = empty_list()
    occurs_in_disease_context: Optional[Union[str, DiseaseId]] = None
    occurs_in_subtype_context: Optional[Union[str, ALSSubtypeId]] = None
    occurs_in_cell_type: Optional[Union[Union[str, CellTypeId], list[Union[str, CellTypeId]]]] = empty_list()
    occurs_in_anatomy: Optional[Union[Union[str, AnatomyId], list[Union[str, AnatomyId]]]] = empty_list()
    is_supported_by: Optional[Union[Union[str, EvidenceRecordId], list[Union[str, EvidenceRecordId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PathogenesisStatementId):
            self.id = PathogenesisStatementId(self.id)

        if not isinstance(self.contributes_to_pathogenic_mechanism, list):
            self.contributes_to_pathogenic_mechanism = [self.contributes_to_pathogenic_mechanism] if self.contributes_to_pathogenic_mechanism is not None else []
        self.contributes_to_pathogenic_mechanism = [v if isinstance(v, PathogenicMechanismId) else PathogenicMechanismId(v) for v in self.contributes_to_pathogenic_mechanism]

        if self.occurs_in_disease_context is not None and not isinstance(self.occurs_in_disease_context, DiseaseId):
            self.occurs_in_disease_context = DiseaseId(self.occurs_in_disease_context)

        if self.occurs_in_subtype_context is not None and not isinstance(self.occurs_in_subtype_context, ALSSubtypeId):
            self.occurs_in_subtype_context = ALSSubtypeId(self.occurs_in_subtype_context)

        if not isinstance(self.occurs_in_cell_type, list):
            self.occurs_in_cell_type = [self.occurs_in_cell_type] if self.occurs_in_cell_type is not None else []
        self.occurs_in_cell_type = [v if isinstance(v, CellTypeId) else CellTypeId(v) for v in self.occurs_in_cell_type]

        if not isinstance(self.occurs_in_anatomy, list):
            self.occurs_in_anatomy = [self.occurs_in_anatomy] if self.occurs_in_anatomy is not None else []
        self.occurs_in_anatomy = [v if isinstance(v, AnatomyId) else AnatomyId(v) for v in self.occurs_in_anatomy]

        if not isinstance(self.is_supported_by, list):
            self.is_supported_by = [self.is_supported_by] if self.is_supported_by is not None else []
        self.is_supported_by = [v if isinstance(v, EvidenceRecordId) else EvidenceRecordId(v) for v in self.is_supported_by]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DifferentialExpressionStatement(EvidenceStatement):
    """
    A differential gene-expression assertion in an ALS context, including direction, comparator, subtype, anatomy,
    cell type, cohort, sample, assay, dataset, and statistical support. This is the semantic parent for the
    Neo4j-compatible GeneExpressionContext class.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["DifferentialExpressionStatement"]
    class_class_curie: ClassVar[str] = "alskg:DifferentialExpressionStatement"
    class_name: ClassVar[str] = "DifferentialExpressionStatement"
    class_model_uri: ClassVar[URIRef] = ALSKG.DifferentialExpressionStatement

    id: Union[str, DifferentialExpressionStatementId] = None
    measures_gene_expression_of: Optional[Union[str, GeneId]] = None
    has_expression_direction: Optional[Union[str, "ExpressionDirectionEnum"]] = None
    has_log_fold_change: Optional[float] = None
    has_p_value: Optional[float] = None
    has_adjusted_p_value: Optional[float] = None
    has_false_discovery_rate: Optional[float] = None
    compares_against: Optional[Union[str, ComparatorGroupId]] = None
    occurs_in_disease_context: Optional[Union[str, DiseaseId]] = None
    occurs_in_subtype_context: Optional[Union[str, ALSSubtypeId]] = None
    occurs_in_cell_type: Optional[Union[Union[str, CellTypeId], list[Union[str, CellTypeId]]]] = empty_list()
    occurs_in_anatomy: Optional[Union[Union[str, AnatomyId], list[Union[str, AnatomyId]]]] = empty_list()
    occurs_in_cohort: Optional[Union[str, CohortId]] = None
    measured_in_sample: Optional[Union[str, SampleId]] = None
    measured_by_assay: Optional[Union[str, AssayId]] = None
    derives_from_dataset: Optional[Union[str, DatasetId]] = None
    is_supported_by: Optional[Union[Union[str, EvidenceRecordId], list[Union[str, EvidenceRecordId]]]] = empty_list()
    differential_expression_measures_gene: Optional[Union[str, GeneId]] = None
    differential_expression_occurs_in_subtype: Optional[Union[str, ALSSubtypeId]] = None
    differential_expression_occurs_in_anatomy: Optional[Union[str, AnatomyId]] = None
    differential_expression_occurs_in_cell_type: Optional[Union[str, CellTypeId]] = None
    differential_expression_measured_by_assay: Optional[Union[str, AssayId]] = None
    differential_expression_derives_from_dataset: Optional[Union[str, DatasetId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DifferentialExpressionStatementId):
            self.id = DifferentialExpressionStatementId(self.id)

        if self.measures_gene_expression_of is not None and not isinstance(self.measures_gene_expression_of, GeneId):
            self.measures_gene_expression_of = GeneId(self.measures_gene_expression_of)

        if self.has_expression_direction is not None and not isinstance(self.has_expression_direction, ExpressionDirectionEnum):
            self.has_expression_direction = ExpressionDirectionEnum(self.has_expression_direction)

        if self.has_log_fold_change is not None and not isinstance(self.has_log_fold_change, float):
            self.has_log_fold_change = float(self.has_log_fold_change)

        if self.has_p_value is not None and not isinstance(self.has_p_value, float):
            self.has_p_value = float(self.has_p_value)

        if self.has_adjusted_p_value is not None and not isinstance(self.has_adjusted_p_value, float):
            self.has_adjusted_p_value = float(self.has_adjusted_p_value)

        if self.has_false_discovery_rate is not None and not isinstance(self.has_false_discovery_rate, float):
            self.has_false_discovery_rate = float(self.has_false_discovery_rate)

        if self.compares_against is not None and not isinstance(self.compares_against, ComparatorGroupId):
            self.compares_against = ComparatorGroupId(self.compares_against)

        if self.occurs_in_disease_context is not None and not isinstance(self.occurs_in_disease_context, DiseaseId):
            self.occurs_in_disease_context = DiseaseId(self.occurs_in_disease_context)

        if self.occurs_in_subtype_context is not None and not isinstance(self.occurs_in_subtype_context, ALSSubtypeId):
            self.occurs_in_subtype_context = ALSSubtypeId(self.occurs_in_subtype_context)

        if not isinstance(self.occurs_in_cell_type, list):
            self.occurs_in_cell_type = [self.occurs_in_cell_type] if self.occurs_in_cell_type is not None else []
        self.occurs_in_cell_type = [v if isinstance(v, CellTypeId) else CellTypeId(v) for v in self.occurs_in_cell_type]

        if not isinstance(self.occurs_in_anatomy, list):
            self.occurs_in_anatomy = [self.occurs_in_anatomy] if self.occurs_in_anatomy is not None else []
        self.occurs_in_anatomy = [v if isinstance(v, AnatomyId) else AnatomyId(v) for v in self.occurs_in_anatomy]

        if self.occurs_in_cohort is not None and not isinstance(self.occurs_in_cohort, CohortId):
            self.occurs_in_cohort = CohortId(self.occurs_in_cohort)

        if self.measured_in_sample is not None and not isinstance(self.measured_in_sample, SampleId):
            self.measured_in_sample = SampleId(self.measured_in_sample)

        if self.measured_by_assay is not None and not isinstance(self.measured_by_assay, AssayId):
            self.measured_by_assay = AssayId(self.measured_by_assay)

        if self.derives_from_dataset is not None and not isinstance(self.derives_from_dataset, DatasetId):
            self.derives_from_dataset = DatasetId(self.derives_from_dataset)

        if not isinstance(self.is_supported_by, list):
            self.is_supported_by = [self.is_supported_by] if self.is_supported_by is not None else []
        self.is_supported_by = [v if isinstance(v, EvidenceRecordId) else EvidenceRecordId(v) for v in self.is_supported_by]

        if self.differential_expression_measures_gene is not None and not isinstance(self.differential_expression_measures_gene, GeneId):
            self.differential_expression_measures_gene = GeneId(self.differential_expression_measures_gene)

        if self.differential_expression_occurs_in_subtype is not None and not isinstance(self.differential_expression_occurs_in_subtype, ALSSubtypeId):
            self.differential_expression_occurs_in_subtype = ALSSubtypeId(self.differential_expression_occurs_in_subtype)

        if self.differential_expression_occurs_in_anatomy is not None and not isinstance(self.differential_expression_occurs_in_anatomy, AnatomyId):
            self.differential_expression_occurs_in_anatomy = AnatomyId(self.differential_expression_occurs_in_anatomy)

        if self.differential_expression_occurs_in_cell_type is not None and not isinstance(self.differential_expression_occurs_in_cell_type, CellTypeId):
            self.differential_expression_occurs_in_cell_type = CellTypeId(self.differential_expression_occurs_in_cell_type)

        if self.differential_expression_measured_by_assay is not None and not isinstance(self.differential_expression_measured_by_assay, AssayId):
            self.differential_expression_measured_by_assay = AssayId(self.differential_expression_measured_by_assay)

        if self.differential_expression_derives_from_dataset is not None and not isinstance(self.differential_expression_derives_from_dataset, DatasetId):
            self.differential_expression_derives_from_dataset = DatasetId(self.differential_expression_derives_from_dataset)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneExpressionContext(DifferentialExpressionStatement):
    """
    Neo4j-compatible concrete expression-context node for ALS-KG. Prefer the parent class
    DifferentialExpressionStatement for ontology semantics; use GeneExpressionContext when materializing expression
    findings as Neo4j nodes such as ECX.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["GeneExpressionContext"]
    class_class_curie: ClassVar[str] = "alskg:GeneExpressionContext"
    class_name: ClassVar[str] = "GeneExpressionContext"
    class_model_uri: ClassVar[URIRef] = ALSKG.GeneExpressionContext

    id: Union[str, GeneExpressionContextId] = None
    gene: Union[str, GeneId] = None
    molecular_subtype: Union[str, MolecularSubtypeId] = None
    direction: Union[str, "ExpressionDirectionEnum"] = None
    source: Optional[str] = None
    direct_sources: Optional[Union[str, list[str]]] = empty_list()
    indirect_sources: Optional[Union[str, list[str]]] = empty_list()
    measures_gene_expression_of: Optional[Union[str, GeneId]] = None
    has_expression_direction: Optional[Union[str, "ExpressionDirectionEnum"]] = None
    occurs_in_subtype_context: Optional[Union[str, ALSSubtypeId]] = None
    occurs_in_cell_type: Optional[Union[Union[str, CellTypeId], list[Union[str, CellTypeId]]]] = empty_list()
    occurs_in_anatomy: Optional[Union[Union[str, AnatomyId], list[Union[str, AnatomyId]]]] = empty_list()
    measured_in_sample: Optional[Union[str, SampleId]] = None
    measured_by_assay: Optional[Union[str, AssayId]] = None
    derives_from_dataset: Optional[Union[str, DatasetId]] = None
    is_supported_by: Optional[Union[Union[str, EvidenceRecordId], list[Union[str, EvidenceRecordId]]]] = empty_list()
    anatomy: Optional[Union[str, AnatomyId]] = None
    biological_context_type: Optional[Union[str, "BiologicalContextTypeEnum"]] = None
    cell_model: Optional[str] = None
    year: Optional[int] = None
    validated_in: Optional[Union[str, list[str]]] = empty_list()
    biological_note: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneExpressionContextId):
            self.id = GeneExpressionContextId(self.id)

        if self._is_empty(self.gene):
            self.MissingRequiredField("gene")
        if not isinstance(self.gene, GeneId):
            self.gene = GeneId(self.gene)

        if self._is_empty(self.molecular_subtype):
            self.MissingRequiredField("molecular_subtype")
        if not isinstance(self.molecular_subtype, MolecularSubtypeId):
            self.molecular_subtype = MolecularSubtypeId(self.molecular_subtype)

        if self._is_empty(self.direction):
            self.MissingRequiredField("direction")
        if not isinstance(self.direction, ExpressionDirectionEnum):
            self.direction = ExpressionDirectionEnum(self.direction)

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        if not isinstance(self.direct_sources, list):
            self.direct_sources = [self.direct_sources] if self.direct_sources is not None else []
        self.direct_sources = [v if isinstance(v, str) else str(v) for v in self.direct_sources]

        if not isinstance(self.indirect_sources, list):
            self.indirect_sources = [self.indirect_sources] if self.indirect_sources is not None else []
        self.indirect_sources = [v if isinstance(v, str) else str(v) for v in self.indirect_sources]

        if self.measures_gene_expression_of is not None and not isinstance(self.measures_gene_expression_of, GeneId):
            self.measures_gene_expression_of = GeneId(self.measures_gene_expression_of)

        if self.has_expression_direction is not None and not isinstance(self.has_expression_direction, ExpressionDirectionEnum):
            self.has_expression_direction = ExpressionDirectionEnum(self.has_expression_direction)

        if self.occurs_in_subtype_context is not None and not isinstance(self.occurs_in_subtype_context, ALSSubtypeId):
            self.occurs_in_subtype_context = ALSSubtypeId(self.occurs_in_subtype_context)

        if not isinstance(self.occurs_in_cell_type, list):
            self.occurs_in_cell_type = [self.occurs_in_cell_type] if self.occurs_in_cell_type is not None else []
        self.occurs_in_cell_type = [v if isinstance(v, CellTypeId) else CellTypeId(v) for v in self.occurs_in_cell_type]

        if not isinstance(self.occurs_in_anatomy, list):
            self.occurs_in_anatomy = [self.occurs_in_anatomy] if self.occurs_in_anatomy is not None else []
        self.occurs_in_anatomy = [v if isinstance(v, AnatomyId) else AnatomyId(v) for v in self.occurs_in_anatomy]

        if self.measured_in_sample is not None and not isinstance(self.measured_in_sample, SampleId):
            self.measured_in_sample = SampleId(self.measured_in_sample)

        if self.measured_by_assay is not None and not isinstance(self.measured_by_assay, AssayId):
            self.measured_by_assay = AssayId(self.measured_by_assay)

        if self.derives_from_dataset is not None and not isinstance(self.derives_from_dataset, DatasetId):
            self.derives_from_dataset = DatasetId(self.derives_from_dataset)

        if not isinstance(self.is_supported_by, list):
            self.is_supported_by = [self.is_supported_by] if self.is_supported_by is not None else []
        self.is_supported_by = [v if isinstance(v, EvidenceRecordId) else EvidenceRecordId(v) for v in self.is_supported_by]

        if self.anatomy is not None and not isinstance(self.anatomy, AnatomyId):
            self.anatomy = AnatomyId(self.anatomy)

        if self.biological_context_type is not None and not isinstance(self.biological_context_type, BiologicalContextTypeEnum):
            self.biological_context_type = BiologicalContextTypeEnum(self.biological_context_type)

        if self.cell_model is not None and not isinstance(self.cell_model, str):
            self.cell_model = str(self.cell_model)

        if self.year is not None and not isinstance(self.year, int):
            self.year = int(self.year)

        if not isinstance(self.validated_in, list):
            self.validated_in = [self.validated_in] if self.validated_in is not None else []
        self.validated_in = [v if isinstance(v, str) else str(v) for v in self.validated_in]

        if self.biological_note is not None and not isinstance(self.biological_note, str):
            self.biological_note = str(self.biological_note)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProteinAbundanceResult(EvidenceStatement):
    """
    A protein abundance, localization, or pathology result in an ALS context, including protein, aggregate, tissue,
    cell type, assay, cohort, and evidence.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["ProteinAbundanceResult"]
    class_class_curie: ClassVar[str] = "alskg:ProteinAbundanceResult"
    class_name: ClassVar[str] = "ProteinAbundanceResult"
    class_model_uri: ClassVar[URIRef] = ALSKG.ProteinAbundanceResult

    id: Union[str, ProteinAbundanceResultId] = None
    measures_protein_abundance_of: Optional[Union[str, ProteinId]] = None
    has_abundance_direction: Optional[Union[str, "ExpressionDirectionEnum"]] = None
    occurs_in_disease_context: Optional[Union[str, DiseaseId]] = None
    occurs_in_subtype_context: Optional[Union[str, ALSSubtypeId]] = None
    occurs_in_cell_type: Optional[Union[Union[str, CellTypeId], list[Union[str, CellTypeId]]]] = empty_list()
    occurs_in_anatomy: Optional[Union[Union[str, AnatomyId], list[Union[str, AnatomyId]]]] = empty_list()
    measured_in_sample: Optional[Union[str, SampleId]] = None
    measured_by_assay: Optional[Union[str, AssayId]] = None
    derives_from_dataset: Optional[Union[str, DatasetId]] = None
    is_supported_by: Optional[Union[Union[str, EvidenceRecordId], list[Union[str, EvidenceRecordId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProteinAbundanceResultId):
            self.id = ProteinAbundanceResultId(self.id)

        if self.measures_protein_abundance_of is not None and not isinstance(self.measures_protein_abundance_of, ProteinId):
            self.measures_protein_abundance_of = ProteinId(self.measures_protein_abundance_of)

        if self.has_abundance_direction is not None and not isinstance(self.has_abundance_direction, ExpressionDirectionEnum):
            self.has_abundance_direction = ExpressionDirectionEnum(self.has_abundance_direction)

        if self.occurs_in_disease_context is not None and not isinstance(self.occurs_in_disease_context, DiseaseId):
            self.occurs_in_disease_context = DiseaseId(self.occurs_in_disease_context)

        if self.occurs_in_subtype_context is not None and not isinstance(self.occurs_in_subtype_context, ALSSubtypeId):
            self.occurs_in_subtype_context = ALSSubtypeId(self.occurs_in_subtype_context)

        if not isinstance(self.occurs_in_cell_type, list):
            self.occurs_in_cell_type = [self.occurs_in_cell_type] if self.occurs_in_cell_type is not None else []
        self.occurs_in_cell_type = [v if isinstance(v, CellTypeId) else CellTypeId(v) for v in self.occurs_in_cell_type]

        if not isinstance(self.occurs_in_anatomy, list):
            self.occurs_in_anatomy = [self.occurs_in_anatomy] if self.occurs_in_anatomy is not None else []
        self.occurs_in_anatomy = [v if isinstance(v, AnatomyId) else AnatomyId(v) for v in self.occurs_in_anatomy]

        if self.measured_in_sample is not None and not isinstance(self.measured_in_sample, SampleId):
            self.measured_in_sample = SampleId(self.measured_in_sample)

        if self.measured_by_assay is not None and not isinstance(self.measured_by_assay, AssayId):
            self.measured_by_assay = AssayId(self.measured_by_assay)

        if self.derives_from_dataset is not None and not isinstance(self.derives_from_dataset, DatasetId):
            self.derives_from_dataset = DatasetId(self.derives_from_dataset)

        if not isinstance(self.is_supported_by, list):
            self.is_supported_by = [self.is_supported_by] if self.is_supported_by is not None else []
        self.is_supported_by = [v if isinstance(v, EvidenceRecordId) else EvidenceRecordId(v) for v in self.is_supported_by]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhenotypeObservation(EvidenceStatement):
    """
    A contextual observation that a phenotype, symptom, sign, or clinical feature is present, absent, frequent, rare,
    early, late, or otherwise characterized in ALS or an ALS subtype.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["PhenotypeObservation"]
    class_class_curie: ClassVar[str] = "alskg:PhenotypeObservation"
    class_name: ClassVar[str] = "PhenotypeObservation"
    class_model_uri: ClassVar[URIRef] = ALSKG.PhenotypeObservation

    id: Union[str, PhenotypeObservationId] = None
    has_observed_phenotype: Optional[Union[str, PhenotypeId]] = None
    occurs_in_disease_context: Optional[Union[str, DiseaseId]] = None
    occurs_in_subtype_context: Optional[Union[str, ALSSubtypeId]] = None
    has_disease_stage: Optional[Union[str, DiseaseStageId]] = None
    has_progression_pattern: Optional[Union[str, ProgressionPatternId]] = None
    occurs_in_cohort: Optional[Union[str, CohortId]] = None
    is_supported_by: Optional[Union[Union[str, EvidenceRecordId], list[Union[str, EvidenceRecordId]]]] = empty_list()
    phenotype_observation_has_observed_phenotype: Optional[Union[str, PhenotypeId]] = None
    phenotype_observation_occurs_in_subtype: Optional[Union[str, ALSSubtypeId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhenotypeObservationId):
            self.id = PhenotypeObservationId(self.id)

        if self.has_observed_phenotype is not None and not isinstance(self.has_observed_phenotype, PhenotypeId):
            self.has_observed_phenotype = PhenotypeId(self.has_observed_phenotype)

        if self.occurs_in_disease_context is not None and not isinstance(self.occurs_in_disease_context, DiseaseId):
            self.occurs_in_disease_context = DiseaseId(self.occurs_in_disease_context)

        if self.occurs_in_subtype_context is not None and not isinstance(self.occurs_in_subtype_context, ALSSubtypeId):
            self.occurs_in_subtype_context = ALSSubtypeId(self.occurs_in_subtype_context)

        if self.has_disease_stage is not None and not isinstance(self.has_disease_stage, DiseaseStageId):
            self.has_disease_stage = DiseaseStageId(self.has_disease_stage)

        if self.has_progression_pattern is not None and not isinstance(self.has_progression_pattern, ProgressionPatternId):
            self.has_progression_pattern = ProgressionPatternId(self.has_progression_pattern)

        if self.occurs_in_cohort is not None and not isinstance(self.occurs_in_cohort, CohortId):
            self.occurs_in_cohort = CohortId(self.occurs_in_cohort)

        if not isinstance(self.is_supported_by, list):
            self.is_supported_by = [self.is_supported_by] if self.is_supported_by is not None else []
        self.is_supported_by = [v if isinstance(v, EvidenceRecordId) else EvidenceRecordId(v) for v in self.is_supported_by]

        if self.phenotype_observation_has_observed_phenotype is not None and not isinstance(self.phenotype_observation_has_observed_phenotype, PhenotypeId):
            self.phenotype_observation_has_observed_phenotype = PhenotypeId(self.phenotype_observation_has_observed_phenotype)

        if self.phenotype_observation_occurs_in_subtype is not None and not isinstance(self.phenotype_observation_occurs_in_subtype, ALSSubtypeId):
            self.phenotype_observation_occurs_in_subtype = ALSSubtypeId(self.phenotype_observation_occurs_in_subtype)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DiseaseStage(ClinicalEntity):
    """
    A temporal or clinical stage of ALS, such as early disease, established disease, late disease, pre-symptomatic
    carrier state, or time since symptom onset.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["DiseaseStage"]
    class_class_curie: ClassVar[str] = "alskg:DiseaseStage"
    class_name: ClassVar[str] = "DiseaseStage"
    class_model_uri: ClassVar[URIRef] = ALSKG.DiseaseStage

    id: Union[str, DiseaseStageId] = None
    name: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiseaseStageId):
            self.id = DiseaseStageId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProgressionPattern(ClinicalEntity):
    """
    A disease progression pattern such as fast progression, slow progression, respiratory progression, spreading
    pattern, or ALSFRS-R decline trajectory.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["ProgressionPattern"]
    class_class_curie: ClassVar[str] = "alskg:ProgressionPattern"
    class_name: ClassVar[str] = "ProgressionPattern"
    class_model_uri: ClassVar[URIRef] = ALSKG.ProgressionPattern

    id: Union[str, ProgressionPatternId] = None
    name: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProgressionPatternId):
            self.id = ProgressionPatternId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Biomarker(ClinicalEntity):
    """
    A molecular, imaging, electrophysiological, pathological, or clinical biomarker relevant to ALS diagnosis,
    subtype, prognosis, progression, mechanism, or therapeutic response.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Biomarker"]
    class_class_curie: ClassVar[str] = "biolink:Biomarker"
    class_name: ClassVar[str] = "Biomarker"
    class_model_uri: ClassVar[URIRef] = ALSKG.Biomarker

    id: Union[str, BiomarkerId] = None
    name: Optional[str] = None
    biomarker_for_disease: Optional[Union[Union[str, DiseaseId], list[Union[str, DiseaseId]]]] = empty_list()
    biomarker_for_subtype: Optional[Union[Union[str, ALSSubtypeId], list[Union[str, ALSSubtypeId]]]] = empty_list()
    indicates_pathogenic_mechanism: Optional[Union[Union[str, PathogenicMechanismId], list[Union[str, PathogenicMechanismId]]]] = empty_list()
    measured_by_assay: Optional[Union[str, AssayId]] = None
    is_supported_by: Optional[Union[Union[str, EvidenceRecordId], list[Union[str, EvidenceRecordId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiomarkerId):
            self.id = BiomarkerId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.biomarker_for_disease, list):
            self.biomarker_for_disease = [self.biomarker_for_disease] if self.biomarker_for_disease is not None else []
        self.biomarker_for_disease = [v if isinstance(v, DiseaseId) else DiseaseId(v) for v in self.biomarker_for_disease]

        if not isinstance(self.biomarker_for_subtype, list):
            self.biomarker_for_subtype = [self.biomarker_for_subtype] if self.biomarker_for_subtype is not None else []
        self.biomarker_for_subtype = [v if isinstance(v, ALSSubtypeId) else ALSSubtypeId(v) for v in self.biomarker_for_subtype]

        if not isinstance(self.indicates_pathogenic_mechanism, list):
            self.indicates_pathogenic_mechanism = [self.indicates_pathogenic_mechanism] if self.indicates_pathogenic_mechanism is not None else []
        self.indicates_pathogenic_mechanism = [v if isinstance(v, PathogenicMechanismId) else PathogenicMechanismId(v) for v in self.indicates_pathogenic_mechanism]

        if self.measured_by_assay is not None and not isinstance(self.measured_by_assay, AssayId):
            self.measured_by_assay = AssayId(self.measured_by_assay)

        if not isinstance(self.is_supported_by, list):
            self.is_supported_by = [self.is_supported_by] if self.is_supported_by is not None else []
        self.is_supported_by = [v if isinstance(v, EvidenceRecordId) else EvidenceRecordId(v) for v in self.is_supported_by]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Study(ProvenanceEntity):
    """
    A research study generating ALS evidence, datasets, cohorts, measurements, or publications.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000066"]
    class_class_curie: ClassVar[str] = "OBI:0000066"
    class_name: ClassVar[str] = "Study"
    class_model_uri: ClassVar[URIRef] = ALSKG.Study

    id: Union[str, StudyId] = None
    name: Optional[str] = None
    has_publication: Optional[Union[Union[str, PublicationId], list[Union[str, PublicationId]]]] = empty_list()
    from_data_source: Optional[Union[str, DataSourceId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StudyId):
            self.id = StudyId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.has_publication, list):
            self.has_publication = [self.has_publication] if self.has_publication is not None else []
        self.has_publication = [v if isinstance(v, PublicationId) else PublicationId(v) for v in self.has_publication]

        if self.from_data_source is not None and not isinstance(self.from_data_source, DataSourceId):
            self.from_data_source = DataSourceId(self.from_data_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Dataset(ProvenanceEntity):
    """
    A dataset used as evidence or source for ALS-KG statements, such as Target ALS, Answer ALS, NYGC ALS, Project
    MinE, ALL ALS, or GEO studies.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Dataset"]
    class_class_curie: ClassVar[str] = "schema:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = ALSKG.Dataset

    id: Union[str, DatasetId] = None
    name: Optional[str] = None
    from_data_source: Optional[Union[str, DataSourceId]] = None
    has_publication: Optional[Union[Union[str, PublicationId], list[Union[str, PublicationId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetId):
            self.id = DatasetId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.from_data_source is not None and not isinstance(self.from_data_source, DataSourceId):
            self.from_data_source = DataSourceId(self.from_data_source)

        if not isinstance(self.has_publication, list):
            self.has_publication = [self.has_publication] if self.has_publication is not None else []
        self.has_publication = [v if isinstance(v, PublicationId) else PublicationId(v) for v in self.has_publication]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Cohort(ProvenanceEntity):
    """
    A participant group, case/control group, genotype group, subtype group, or study cohort used in ALS research.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000202"]
    class_class_curie: ClassVar[str] = "OBI:0000202"
    class_name: ClassVar[str] = "Cohort"
    class_model_uri: ClassVar[URIRef] = ALSKG.Cohort

    id: Union[str, CohortId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    from_data_source: Optional[Union[str, DataSourceId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CohortId):
            self.id = CohortId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.from_data_source is not None and not isinstance(self.from_data_source, DataSourceId):
            self.from_data_source = DataSourceId(self.from_data_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ComparatorGroup(Cohort):
    """
    A comparator group used in differential expression, biomarker, or clinical analyses, such as control, non-ALS,
    sporadic ALS, C9orf72-ALS, or healthy motor neuron group.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["ComparatorGroup"]
    class_class_curie: ClassVar[str] = "alskg:ComparatorGroup"
    class_name: ClassVar[str] = "ComparatorGroup"
    class_model_uri: ClassVar[URIRef] = ALSKG.ComparatorGroup

    id: Union[str, ComparatorGroupId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComparatorGroupId):
            self.id = ComparatorGroupId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sample(ProvenanceEntity):
    """
    A biological sample or specimen used in ALS analysis, such as postmortem spinal cord, motor cortex, CSF, blood,
    iPSC-derived motor neurons, or sorted cell populations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0100051"]
    class_class_curie: ClassVar[str] = "OBI:0100051"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = ALSKG.Sample

    id: Union[str, SampleId] = None
    name: Optional[str] = None
    derived_from_anatomy: Optional[Union[str, AnatomyId]] = None
    has_cell_type: Optional[Union[Union[str, CellTypeId], list[Union[str, CellTypeId]]]] = empty_list()
    occurs_in_disease_context: Optional[Union[str, DiseaseId]] = None
    occurs_in_subtype_context: Optional[Union[str, ALSSubtypeId]] = None
    from_data_source: Optional[Union[str, DataSourceId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SampleId):
            self.id = SampleId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.derived_from_anatomy is not None and not isinstance(self.derived_from_anatomy, AnatomyId):
            self.derived_from_anatomy = AnatomyId(self.derived_from_anatomy)

        if not isinstance(self.has_cell_type, list):
            self.has_cell_type = [self.has_cell_type] if self.has_cell_type is not None else []
        self.has_cell_type = [v if isinstance(v, CellTypeId) else CellTypeId(v) for v in self.has_cell_type]

        if self.occurs_in_disease_context is not None and not isinstance(self.occurs_in_disease_context, DiseaseId):
            self.occurs_in_disease_context = DiseaseId(self.occurs_in_disease_context)

        if self.occurs_in_subtype_context is not None and not isinstance(self.occurs_in_subtype_context, ALSSubtypeId):
            self.occurs_in_subtype_context = ALSSubtypeId(self.occurs_in_subtype_context)

        if self.from_data_source is not None and not isinstance(self.from_data_source, DataSourceId):
            self.from_data_source = DataSourceId(self.from_data_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Assay(ProvenanceEntity):
    """
    An assay or measurement method used to generate ALS evidence, such as bulk RNA-seq, single-nucleus RNA-seq,
    spatial transcriptomics, proteomics, WGS, immunostaining, or clinical assessment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000070"]
    class_class_curie: ClassVar[str] = "OBI:0000070"
    class_name: ClassVar[str] = "Assay"
    class_model_uri: ClassVar[URIRef] = ALSKG.Assay

    id: Union[str, AssayId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AssayId):
            self.id = AssayId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ModelSystem(AnalyticalEntity):
    """
    A biological model system used to study ALS, including animal models, iPSC-derived cells, organoids, cell lines,
    or perturbation systems.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["ModelSystem"]
    class_class_curie: ClassVar[str] = "alskg:ModelSystem"
    class_name: ClassVar[str] = "ModelSystem"
    class_model_uri: ClassVar[URIRef] = ALSKG.ModelSystem

    id: Union[str, ModelSystemId] = None
    name: Optional[str] = None
    models_disease: Optional[Union[str, DiseaseId]] = None
    models_subtype: Optional[Union[str, ALSSubtypeId]] = None
    has_genetic_perturbation: Optional[Union[Union[str, NamedEntityId], list[Union[str, NamedEntityId]]]] = empty_list()
    is_supported_by: Optional[Union[Union[str, EvidenceRecordId], list[Union[str, EvidenceRecordId]]]] = empty_list()
    model_system_models_subtype: Optional[Union[str, ALSSubtypeId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ModelSystemId):
            self.id = ModelSystemId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.models_disease is not None and not isinstance(self.models_disease, DiseaseId):
            self.models_disease = DiseaseId(self.models_disease)

        if self.models_subtype is not None and not isinstance(self.models_subtype, ALSSubtypeId):
            self.models_subtype = ALSSubtypeId(self.models_subtype)

        if not isinstance(self.has_genetic_perturbation, list):
            self.has_genetic_perturbation = [self.has_genetic_perturbation] if self.has_genetic_perturbation is not None else []
        self.has_genetic_perturbation = [v if isinstance(v, NamedEntityId) else NamedEntityId(v) for v in self.has_genetic_perturbation]

        if not isinstance(self.is_supported_by, list):
            self.is_supported_by = [self.is_supported_by] if self.is_supported_by is not None else []
        self.is_supported_by = [v if isinstance(v, EvidenceRecordId) else EvidenceRecordId(v) for v in self.is_supported_by]

        if self.model_system_models_subtype is not None and not isinstance(self.model_system_models_subtype, ALSSubtypeId):
            self.model_system_models_subtype = ALSSubtypeId(self.model_system_models_subtype)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TherapeuticIntervention(ClinicalEntity):
    """
    A therapeutic intervention relevant to ALS, including small molecules, antisense oligonucleotides, gene therapy,
    biologics, rehabilitation, respiratory support, or investigational therapies.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Treatment"]
    class_class_curie: ClassVar[str] = "biolink:Treatment"
    class_name: ClassVar[str] = "TherapeuticIntervention"
    class_model_uri: ClassVar[URIRef] = ALSKG.TherapeuticIntervention

    id: Union[str, TherapeuticInterventionId] = None
    name: Optional[str] = None
    targets_gene: Optional[Union[Union[str, GeneId], list[Union[str, GeneId]]]] = empty_list()
    targets_protein: Optional[Union[Union[str, ProteinId], list[Union[str, ProteinId]]]] = empty_list()
    modulates_pathogenic_mechanism: Optional[Union[Union[str, PathogenicMechanismId], list[Union[str, PathogenicMechanismId]]]] = empty_list()
    tested_in_clinical_trial: Optional[Union[Union[str, ClinicalTrialId], list[Union[str, ClinicalTrialId]]]] = empty_list()
    therapeutic_intervention_tested_in_clinical_trial: Optional[Union[str, ClinicalTrialId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TherapeuticInterventionId):
            self.id = TherapeuticInterventionId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.targets_gene, list):
            self.targets_gene = [self.targets_gene] if self.targets_gene is not None else []
        self.targets_gene = [v if isinstance(v, GeneId) else GeneId(v) for v in self.targets_gene]

        if not isinstance(self.targets_protein, list):
            self.targets_protein = [self.targets_protein] if self.targets_protein is not None else []
        self.targets_protein = [v if isinstance(v, ProteinId) else ProteinId(v) for v in self.targets_protein]

        if not isinstance(self.modulates_pathogenic_mechanism, list):
            self.modulates_pathogenic_mechanism = [self.modulates_pathogenic_mechanism] if self.modulates_pathogenic_mechanism is not None else []
        self.modulates_pathogenic_mechanism = [v if isinstance(v, PathogenicMechanismId) else PathogenicMechanismId(v) for v in self.modulates_pathogenic_mechanism]

        if not isinstance(self.tested_in_clinical_trial, list):
            self.tested_in_clinical_trial = [self.tested_in_clinical_trial] if self.tested_in_clinical_trial is not None else []
        self.tested_in_clinical_trial = [v if isinstance(v, ClinicalTrialId) else ClinicalTrialId(v) for v in self.tested_in_clinical_trial]

        if self.therapeutic_intervention_tested_in_clinical_trial is not None and not isinstance(self.therapeutic_intervention_tested_in_clinical_trial, ClinicalTrialId):
            self.therapeutic_intervention_tested_in_clinical_trial = ClinicalTrialId(self.therapeutic_intervention_tested_in_clinical_trial)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ClinicalTrial(Study):
    """
    A clinical trial or interventional study relevant to ALS, ALS subtypes, therapies, biomarkers, or outcomes.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ClinicalTrial"]
    class_class_curie: ClassVar[str] = "biolink:ClinicalTrial"
    class_name: ClassVar[str] = "ClinicalTrial"
    class_model_uri: ClassVar[URIRef] = ALSKG.ClinicalTrial

    id: Union[str, ClinicalTrialId] = None
    name: Optional[str] = None
    tests_intervention: Optional[Union[Union[str, TherapeuticInterventionId], list[Union[str, TherapeuticInterventionId]]]] = empty_list()
    enrolls_subtype: Optional[Union[Union[str, ALSSubtypeId], list[Union[str, ALSSubtypeId]]]] = empty_list()
    has_outcome_measure: Optional[Union[Union[str, NamedEntityId], list[Union[str, NamedEntityId]]]] = empty_list()
    has_publication: Optional[Union[Union[str, PublicationId], list[Union[str, PublicationId]]]] = empty_list()
    clinical_trial_enrolls_subtype: Optional[Union[str, ALSSubtypeId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ClinicalTrialId):
            self.id = ClinicalTrialId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.tests_intervention, list):
            self.tests_intervention = [self.tests_intervention] if self.tests_intervention is not None else []
        self.tests_intervention = [v if isinstance(v, TherapeuticInterventionId) else TherapeuticInterventionId(v) for v in self.tests_intervention]

        if not isinstance(self.enrolls_subtype, list):
            self.enrolls_subtype = [self.enrolls_subtype] if self.enrolls_subtype is not None else []
        self.enrolls_subtype = [v if isinstance(v, ALSSubtypeId) else ALSSubtypeId(v) for v in self.enrolls_subtype]

        if not isinstance(self.has_outcome_measure, list):
            self.has_outcome_measure = [self.has_outcome_measure] if self.has_outcome_measure is not None else []
        self.has_outcome_measure = [v if isinstance(v, NamedEntityId) else NamedEntityId(v) for v in self.has_outcome_measure]

        if not isinstance(self.has_publication, list):
            self.has_publication = [self.has_publication] if self.has_publication is not None else []
        self.has_publication = [v if isinstance(v, PublicationId) else PublicationId(v) for v in self.has_publication]

        if self.clinical_trial_enrolls_subtype is not None and not isinstance(self.clinical_trial_enrolls_subtype, ALSSubtypeId):
            self.clinical_trial_enrolls_subtype = ALSSubtypeId(self.clinical_trial_enrolls_subtype)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugRepurposingHypothesis(EvidenceStatement):
    """
    A hypothesis that a drug or therapeutic intervention may be relevant to ALS or an ALS subtype based on target
    genes, disease mechanisms, expression directionality, pathways, biomarkers, model evidence, or clinical evidence.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["DrugRepurposingHypothesis"]
    class_class_curie: ClassVar[str] = "alskg:DrugRepurposingHypothesis"
    class_name: ClassVar[str] = "DrugRepurposingHypothesis"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugRepurposingHypothesis

    id: Union[str, DrugRepurposingHypothesisId] = None
    prioritizes_drug: Optional[Union[str, DrugId]] = None
    targets_gene: Optional[Union[Union[str, GeneId], list[Union[str, GeneId]]]] = empty_list()
    targets_protein: Optional[Union[Union[str, ProteinId], list[Union[str, ProteinId]]]] = empty_list()
    modulates_pathogenic_mechanism: Optional[Union[Union[str, PathogenicMechanismId], list[Union[str, PathogenicMechanismId]]]] = empty_list()
    occurs_in_disease_context: Optional[Union[str, DiseaseId]] = None
    occurs_in_subtype_context: Optional[Union[str, ALSSubtypeId]] = None
    has_evidence_basis: Optional[Union[Union[str, EvidenceStatementId], list[Union[str, EvidenceStatementId]]]] = empty_list()
    is_supported_by: Optional[Union[Union[str, EvidenceRecordId], list[Union[str, EvidenceRecordId]]]] = empty_list()
    drug_repurposing_hypothesis_prioritizes_drug: Optional[Union[str, DrugId]] = None
    drug_repurposing_hypothesis_targets_gene: Optional[Union[str, GeneId]] = None
    drug_repurposing_hypothesis_modulates_pathogenic_mechanism: Optional[Union[str, PathogenicMechanismId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DrugRepurposingHypothesisId):
            self.id = DrugRepurposingHypothesisId(self.id)

        if self.prioritizes_drug is not None and not isinstance(self.prioritizes_drug, DrugId):
            self.prioritizes_drug = DrugId(self.prioritizes_drug)

        if not isinstance(self.targets_gene, list):
            self.targets_gene = [self.targets_gene] if self.targets_gene is not None else []
        self.targets_gene = [v if isinstance(v, GeneId) else GeneId(v) for v in self.targets_gene]

        if not isinstance(self.targets_protein, list):
            self.targets_protein = [self.targets_protein] if self.targets_protein is not None else []
        self.targets_protein = [v if isinstance(v, ProteinId) else ProteinId(v) for v in self.targets_protein]

        if not isinstance(self.modulates_pathogenic_mechanism, list):
            self.modulates_pathogenic_mechanism = [self.modulates_pathogenic_mechanism] if self.modulates_pathogenic_mechanism is not None else []
        self.modulates_pathogenic_mechanism = [v if isinstance(v, PathogenicMechanismId) else PathogenicMechanismId(v) for v in self.modulates_pathogenic_mechanism]

        if self.occurs_in_disease_context is not None and not isinstance(self.occurs_in_disease_context, DiseaseId):
            self.occurs_in_disease_context = DiseaseId(self.occurs_in_disease_context)

        if self.occurs_in_subtype_context is not None and not isinstance(self.occurs_in_subtype_context, ALSSubtypeId):
            self.occurs_in_subtype_context = ALSSubtypeId(self.occurs_in_subtype_context)

        if not isinstance(self.has_evidence_basis, list):
            self.has_evidence_basis = [self.has_evidence_basis] if self.has_evidence_basis is not None else []
        self.has_evidence_basis = [v if isinstance(v, EvidenceStatementId) else EvidenceStatementId(v) for v in self.has_evidence_basis]

        if not isinstance(self.is_supported_by, list):
            self.is_supported_by = [self.is_supported_by] if self.is_supported_by is not None else []
        self.is_supported_by = [v if isinstance(v, EvidenceRecordId) else EvidenceRecordId(v) for v in self.is_supported_by]

        if self.drug_repurposing_hypothesis_prioritizes_drug is not None and not isinstance(self.drug_repurposing_hypothesis_prioritizes_drug, DrugId):
            self.drug_repurposing_hypothesis_prioritizes_drug = DrugId(self.drug_repurposing_hypothesis_prioritizes_drug)

        if self.drug_repurposing_hypothesis_targets_gene is not None and not isinstance(self.drug_repurposing_hypothesis_targets_gene, GeneId):
            self.drug_repurposing_hypothesis_targets_gene = GeneId(self.drug_repurposing_hypothesis_targets_gene)

        if self.drug_repurposing_hypothesis_modulates_pathogenic_mechanism is not None and not isinstance(self.drug_repurposing_hypothesis_modulates_pathogenic_mechanism, PathogenicMechanismId):
            self.drug_repurposing_hypothesis_modulates_pathogenic_mechanism = PathogenicMechanismId(self.drug_repurposing_hypothesis_modulates_pathogenic_mechanism)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiologicalAgent(Exposure):
    """
    Optional ALS-KG class for infectious, microbiome, or biological exposure agents if these are intentionally
    modeled. For ALS pathogenesis, prefer PathogenicMechanism rather than BiologicalAgent unless the assertion is
    truly about an organism or biological exposure.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["BiologicalAgent"]
    class_class_curie: ClassVar[str] = "alskg:BiologicalAgent"
    class_name: ClassVar[str] = "BiologicalAgent"
    class_model_uri: ClassVar[URIRef] = ALSKG.BiologicalAgent

    id: Union[str, BiologicalAgentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiologicalAgentId):
            self.id = BiologicalAgentId(self.id)

        super().__post_init__(**kwargs)


class ALSRelationship(RelationshipAssertion):
    """
    Abstract parent for ALS-KG extension relationships that can be materialized in Neo4j while preserving OptimusKG
    compatibility.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["ALSRelationship"]
    class_class_curie: ClassVar[str] = "alskg:ALSRelationship"
    class_name: ClassVar[str] = "ALSRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.ALSRelationship


class ALSSubtypeRelationship(ALSRelationship):
    """
    Relationships defining, classifying, or contextualizing ALS subtypes.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["ALSSubtypeRelationship"]
    class_class_curie: ClassVar[str] = "alskg:ALSSubtypeRelationship"
    class_name: ClassVar[str] = "ALSSubtypeRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.ALSSubtypeRelationship


class ALSPathogenesisRelationship(ALSRelationship):
    """
    Relationships connecting genes, variants, proteins, subtypes, mechanisms, cell types, and anatomy in ALS
    pathogenesis.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["ALSPathogenesisRelationship"]
    class_class_curie: ClassVar[str] = "alskg:ALSPathogenesisRelationship"
    class_name: ClassVar[str] = "ALSPathogenesisRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.ALSPathogenesisRelationship


class ALSExpressionRelationship(ALSRelationship):
    """
    Relationships connecting differential expression results to genes, subtype, anatomy, cell type, sample, assay,
    cohort, dataset, and evidence.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["ALSExpressionRelationship"]
    class_class_curie: ClassVar[str] = "alskg:ALSExpressionRelationship"
    class_name: ClassVar[str] = "ALSExpressionRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.ALSExpressionRelationship


class ALSEvidenceRelationship(ALSRelationship):
    """
    Relationships connecting ALS-KG statements, results, subtypes, and hypotheses to studies, datasets, cohorts,
    samples, assays, publications, and evidence.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["ALSEvidenceRelationship"]
    class_class_curie: ClassVar[str] = "alskg:ALSEvidenceRelationship"
    class_name: ClassVar[str] = "ALSEvidenceRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.ALSEvidenceRelationship


class ALSTherapeuticRelationship(ALSRelationship):
    """
    Relationships supporting ALS therapeutic intervention, target, clinical trial, and drug repurposing hypotheses.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["ALSTherapeuticRelationship"]
    class_class_curie: ClassVar[str] = "alskg:ALSTherapeuticRelationship"
    class_name: ClassVar[str] = "ALSTherapeuticRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.ALSTherapeuticRelationship


@dataclass(repr=False)
class DiseaseHasALSSubtypeRelationship(ALSSubtypeRelationship):
    """
    Disease-to-subtype relationship meaning the disease has the ALS subtype.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["DiseaseHasALSSubtypeRelationship"]
    class_class_curie: ClassVar[str] = "alskg:DiseaseHasALSSubtypeRelationship"
    class_name: ClassVar[str] = "DiseaseHasALSSubtypeRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DiseaseHasALSSubtypeRelationship

    subject: Optional[Union[str, DiseaseId]] = None
    object: Optional[Union[str, ALSSubtypeId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DiseaseId):
            self.subject = DiseaseId(self.subject)

        if self.object is not None and not isinstance(self.object, ALSSubtypeId):
            self.object = ALSSubtypeId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ALSSubtypeIsSubtypeOfDiseaseRelationship(ALSSubtypeRelationship):
    """
    Subtype-to-disease relationship meaning the ALS subtype is a subtype of the disease.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["ALSSubtypeIsSubtypeOfDiseaseRelationship"]
    class_class_curie: ClassVar[str] = "alskg:ALSSubtypeIsSubtypeOfDiseaseRelationship"
    class_name: ClassVar[str] = "ALSSubtypeIsSubtypeOfDiseaseRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.ALSSubtypeIsSubtypeOfDiseaseRelationship

    subject: Optional[Union[str, ALSSubtypeId]] = None
    object: Optional[Union[str, DiseaseId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, ALSSubtypeId):
            self.subject = ALSSubtypeId(self.subject)

        if self.object is not None and not isinstance(self.object, DiseaseId):
            self.object = DiseaseId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ALSSubtypeHasSubtypeSchemeRelationship(ALSSubtypeRelationship):
    """
    Connects an ALS subtype to its subtype scheme or taxonomy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["ALSSubtypeHasSubtypeSchemeRelationship"]
    class_class_curie: ClassVar[str] = "alskg:ALSSubtypeHasSubtypeSchemeRelationship"
    class_name: ClassVar[str] = "ALSSubtypeHasSubtypeSchemeRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.ALSSubtypeHasSubtypeSchemeRelationship

    subject: Optional[Union[str, ALSSubtypeId]] = None
    object: Optional[Union[str, SubtypeSchemeId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, ALSSubtypeId):
            self.subject = ALSSubtypeId(self.subject)

        if self.object is not None and not isinstance(self.object, SubtypeSchemeId):
            self.object = SubtypeSchemeId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ALSSubtypeHasSubtypeCriterionRelationship(ALSSubtypeRelationship):
    """
    Connects an ALS subtype to a defining or assignment criterion.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["ALSSubtypeHasSubtypeCriterionRelationship"]
    class_class_curie: ClassVar[str] = "alskg:ALSSubtypeHasSubtypeCriterionRelationship"
    class_name: ClassVar[str] = "ALSSubtypeHasSubtypeCriterionRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.ALSSubtypeHasSubtypeCriterionRelationship

    subject: Optional[Union[str, ALSSubtypeId]] = None
    object: Optional[Union[str, SubtypeCriterionId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, ALSSubtypeId):
            self.subject = ALSSubtypeId(self.subject)

        if self.object is not None and not isinstance(self.object, SubtypeCriterionId):
            self.object = SubtypeCriterionId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ALSSubtypeDefinedByGeneRelationship(ALSSubtypeRelationship):
    """
    Connects an ALS subtype to a defining or characteristic gene.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["ALSSubtypeDefinedByGeneRelationship"]
    class_class_curie: ClassVar[str] = "alskg:ALSSubtypeDefinedByGeneRelationship"
    class_name: ClassVar[str] = "ALSSubtypeDefinedByGeneRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.ALSSubtypeDefinedByGeneRelationship

    subject: Optional[Union[str, ALSSubtypeId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, ALSSubtypeId):
            self.subject = ALSSubtypeId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ALSSubtypeDefinedByVariantRelationship(ALSSubtypeRelationship):
    """
    Connects an ALS subtype to a defining or characteristic variant.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["ALSSubtypeDefinedByVariantRelationship"]
    class_class_curie: ClassVar[str] = "alskg:ALSSubtypeDefinedByVariantRelationship"
    class_name: ClassVar[str] = "ALSSubtypeDefinedByVariantRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.ALSSubtypeDefinedByVariantRelationship

    subject: Optional[Union[str, ALSSubtypeId]] = None
    object: Optional[Union[str, SequenceVariantId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, ALSSubtypeId):
            self.subject = ALSSubtypeId(self.subject)

        if self.object is not None and not isinstance(self.object, SequenceVariantId):
            self.object = SequenceVariantId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ALSSubtypeHasPathogenicMechanismRelationship(ALSPathogenesisRelationship):
    """
    Connects an ALS subtype to a pathogenic mechanism implicated in that subtype.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["ALSSubtypeHasPathogenicMechanismRelationship"]
    class_class_curie: ClassVar[str] = "alskg:ALSSubtypeHasPathogenicMechanismRelationship"
    class_name: ClassVar[str] = "ALSSubtypeHasPathogenicMechanismRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.ALSSubtypeHasPathogenicMechanismRelationship

    subject: Optional[Union[str, ALSSubtypeId]] = None
    object: Optional[Union[str, PathogenicMechanismId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, ALSSubtypeId):
            self.subject = ALSSubtypeId(self.subject)

        if self.object is not None and not isinstance(self.object, PathogenicMechanismId):
            self.object = PathogenicMechanismId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ALSSubtypeAffectsAnatomyRelationship(ALSPathogenesisRelationship):
    """
    Connects an ALS subtype to an affected anatomical structure.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["ALSSubtypeAffectsAnatomyRelationship"]
    class_class_curie: ClassVar[str] = "alskg:ALSSubtypeAffectsAnatomyRelationship"
    class_name: ClassVar[str] = "ALSSubtypeAffectsAnatomyRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.ALSSubtypeAffectsAnatomyRelationship

    subject: Optional[Union[str, ALSSubtypeId]] = None
    object: Optional[Union[str, AnatomyId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, ALSSubtypeId):
            self.subject = ALSSubtypeId(self.subject)

        if self.object is not None and not isinstance(self.object, AnatomyId):
            self.object = AnatomyId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ALSSubtypeInvolvesCellTypeRelationship(ALSPathogenesisRelationship):
    """
    Connects an ALS subtype to a relevant or affected cell type.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["ALSSubtypeInvolvesCellTypeRelationship"]
    class_class_curie: ClassVar[str] = "alskg:ALSSubtypeInvolvesCellTypeRelationship"
    class_name: ClassVar[str] = "ALSSubtypeInvolvesCellTypeRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.ALSSubtypeInvolvesCellTypeRelationship

    subject: Optional[Union[str, ALSSubtypeId]] = None
    object: Optional[Union[str, CellTypeId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, ALSSubtypeId):
            self.subject = ALSSubtypeId(self.subject)

        if self.object is not None and not isinstance(self.object, CellTypeId):
            self.object = CellTypeId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ALSSubtypeHasPhenotypeObservationRelationship(ALSSubtypeRelationship):
    """
    Connects an ALS subtype to a contextual phenotype observation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["ALSSubtypeHasPhenotypeObservationRelationship"]
    class_class_curie: ClassVar[str] = "alskg:ALSSubtypeHasPhenotypeObservationRelationship"
    class_name: ClassVar[str] = "ALSSubtypeHasPhenotypeObservationRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.ALSSubtypeHasPhenotypeObservationRelationship

    subject: Optional[Union[str, ALSSubtypeId]] = None
    object: Optional[Union[str, PhenotypeObservationId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, ALSSubtypeId):
            self.subject = ALSSubtypeId(self.subject)

        if self.object is not None and not isinstance(self.object, PhenotypeObservationId):
            self.object = PhenotypeObservationId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneHasVariantRelationship(ALSPathogenesisRelationship):
    """
    Connects a gene to a sequence variant.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["GeneHasVariantRelationship"]
    class_class_curie: ClassVar[str] = "alskg:GeneHasVariantRelationship"
    class_name: ClassVar[str] = "GeneHasVariantRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.GeneHasVariantRelationship

    subject: Optional[Union[str, GeneId]] = None
    object: Optional[Union[str, SequenceVariantId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, GeneId):
            self.subject = GeneId(self.subject)

        if self.object is not None and not isinstance(self.object, SequenceVariantId):
            self.object = SequenceVariantId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VariantAffectsGeneRelationship(ALSPathogenesisRelationship):
    """
    Connects a sequence variant to the gene it affects.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["VariantAffectsGeneRelationship"]
    class_class_curie: ClassVar[str] = "alskg:VariantAffectsGeneRelationship"
    class_name: ClassVar[str] = "VariantAffectsGeneRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.VariantAffectsGeneRelationship

    subject: Optional[Union[str, SequenceVariantId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VariantAltersProteinRelationship(ALSPathogenesisRelationship):
    """
    Connects a sequence variant to a protein it alters.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["VariantAltersProteinRelationship"]
    class_class_curie: ClassVar[str] = "alskg:VariantAltersProteinRelationship"
    class_name: ClassVar[str] = "VariantAltersProteinRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.VariantAltersProteinRelationship

    subject: Optional[Union[str, SequenceVariantId]] = None
    object: Optional[Union[str, ProteinId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, SequenceVariantId):
            self.subject = SequenceVariantId(self.subject)

        if self.object is not None and not isinstance(self.object, ProteinId):
            self.object = ProteinId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneContributesToPathogenicMechanismRelationship(ALSPathogenesisRelationship):
    """
    Connects a gene to an ALS pathogenic mechanism it contributes to.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["GeneContributesToPathogenicMechanismRelationship"]
    class_class_curie: ClassVar[str] = "alskg:GeneContributesToPathogenicMechanismRelationship"
    class_name: ClassVar[str] = "GeneContributesToPathogenicMechanismRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.GeneContributesToPathogenicMechanismRelationship

    subject: Optional[Union[str, GeneId]] = None
    object: Optional[Union[str, PathogenicMechanismId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, GeneId):
            self.subject = GeneId(self.subject)

        if self.object is not None and not isinstance(self.object, PathogenicMechanismId):
            self.object = PathogenicMechanismId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProteinContributesToPathogenicMechanismRelationship(ALSPathogenesisRelationship):
    """
    Connects a protein to an ALS pathogenic mechanism it contributes to.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["ProteinContributesToPathogenicMechanismRelationship"]
    class_class_curie: ClassVar[str] = "alskg:ProteinContributesToPathogenicMechanismRelationship"
    class_name: ClassVar[str] = "ProteinContributesToPathogenicMechanismRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.ProteinContributesToPathogenicMechanismRelationship

    subject: Optional[Union[str, ProteinId]] = None
    object: Optional[Union[str, PathogenicMechanismId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, ProteinId):
            self.subject = ProteinId(self.subject)

        if self.object is not None and not isinstance(self.object, PathogenicMechanismId):
            self.object = PathogenicMechanismId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MolecularEventContributesToPathogenicMechanismRelationship(ALSPathogenesisRelationship):
    """
    Connects a molecular event to the pathogenic mechanism it contributes to.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["MolecularEventContributesToPathogenicMechanismRelationship"]
    class_class_curie: ClassVar[str] = "alskg:MolecularEventContributesToPathogenicMechanismRelationship"
    class_name: ClassVar[str] = "MolecularEventContributesToPathogenicMechanismRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.MolecularEventContributesToPathogenicMechanismRelationship

    subject: Optional[Union[str, MolecularEventId]] = None
    object: Optional[Union[str, PathogenicMechanismId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, MolecularEventId):
            self.subject = MolecularEventId(self.subject)

        if self.object is not None and not isinstance(self.object, PathogenicMechanismId):
            self.object = PathogenicMechanismId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PathogenicMechanismOccursInCellTypeRelationship(ALSPathogenesisRelationship):
    """
    Connects a pathogenic mechanism to the cell type where it occurs.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["PathogenicMechanismOccursInCellTypeRelationship"]
    class_class_curie: ClassVar[str] = "alskg:PathogenicMechanismOccursInCellTypeRelationship"
    class_name: ClassVar[str] = "PathogenicMechanismOccursInCellTypeRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.PathogenicMechanismOccursInCellTypeRelationship

    subject: Optional[Union[str, PathogenicMechanismId]] = None
    object: Optional[Union[str, CellTypeId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, PathogenicMechanismId):
            self.subject = PathogenicMechanismId(self.subject)

        if self.object is not None and not isinstance(self.object, CellTypeId):
            self.object = CellTypeId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PathogenicMechanismOccursInAnatomyRelationship(ALSPathogenesisRelationship):
    """
    Connects a pathogenic mechanism to the anatomy where it occurs.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["PathogenicMechanismOccursInAnatomyRelationship"]
    class_class_curie: ClassVar[str] = "alskg:PathogenicMechanismOccursInAnatomyRelationship"
    class_name: ClassVar[str] = "PathogenicMechanismOccursInAnatomyRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.PathogenicMechanismOccursInAnatomyRelationship

    subject: Optional[Union[str, PathogenicMechanismId]] = None
    object: Optional[Union[str, AnatomyId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, PathogenicMechanismId):
            self.subject = PathogenicMechanismId(self.subject)

        if self.object is not None and not isinstance(self.object, AnatomyId):
            self.object = AnatomyId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DifferentialExpressionMeasuresGeneRelationship(ALSExpressionRelationship):
    """
    Connects a differential expression statement to the gene measured.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["DifferentialExpressionMeasuresGeneRelationship"]
    class_class_curie: ClassVar[str] = "alskg:DifferentialExpressionMeasuresGeneRelationship"
    class_name: ClassVar[str] = "DifferentialExpressionMeasuresGeneRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DifferentialExpressionMeasuresGeneRelationship

    subject: Optional[Union[str, DifferentialExpressionStatementId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DifferentialExpressionStatementId):
            self.subject = DifferentialExpressionStatementId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DifferentialExpressionOccursInSubtypeRelationship(ALSExpressionRelationship):
    """
    Connects a differential expression result to its ALS subtype context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["DifferentialExpressionOccursInSubtypeRelationship"]
    class_class_curie: ClassVar[str] = "alskg:DifferentialExpressionOccursInSubtypeRelationship"
    class_name: ClassVar[str] = "DifferentialExpressionOccursInSubtypeRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DifferentialExpressionOccursInSubtypeRelationship

    subject: Optional[Union[str, DifferentialExpressionStatementId]] = None
    object: Optional[Union[str, ALSSubtypeId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DifferentialExpressionStatementId):
            self.subject = DifferentialExpressionStatementId(self.subject)

        if self.object is not None and not isinstance(self.object, ALSSubtypeId):
            self.object = ALSSubtypeId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DifferentialExpressionOccursInAnatomyRelationship(ALSExpressionRelationship):
    """
    Connects a differential expression result to its anatomical context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["DifferentialExpressionOccursInAnatomyRelationship"]
    class_class_curie: ClassVar[str] = "alskg:DifferentialExpressionOccursInAnatomyRelationship"
    class_name: ClassVar[str] = "DifferentialExpressionOccursInAnatomyRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DifferentialExpressionOccursInAnatomyRelationship

    subject: Optional[Union[str, DifferentialExpressionStatementId]] = None
    object: Optional[Union[str, AnatomyId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DifferentialExpressionStatementId):
            self.subject = DifferentialExpressionStatementId(self.subject)

        if self.object is not None and not isinstance(self.object, AnatomyId):
            self.object = AnatomyId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DifferentialExpressionOccursInCellTypeRelationship(ALSExpressionRelationship):
    """
    Connects a differential expression result to its cell type context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["DifferentialExpressionOccursInCellTypeRelationship"]
    class_class_curie: ClassVar[str] = "alskg:DifferentialExpressionOccursInCellTypeRelationship"
    class_name: ClassVar[str] = "DifferentialExpressionOccursInCellTypeRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DifferentialExpressionOccursInCellTypeRelationship

    subject: Optional[Union[str, DifferentialExpressionStatementId]] = None
    object: Optional[Union[str, CellTypeId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DifferentialExpressionStatementId):
            self.subject = DifferentialExpressionStatementId(self.subject)

        if self.object is not None and not isinstance(self.object, CellTypeId):
            self.object = CellTypeId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DifferentialExpressionMeasuredByAssayRelationship(ALSEvidenceRelationship):
    """
    Connects a differential expression result to the assay that measured it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["DifferentialExpressionMeasuredByAssayRelationship"]
    class_class_curie: ClassVar[str] = "alskg:DifferentialExpressionMeasuredByAssayRelationship"
    class_name: ClassVar[str] = "DifferentialExpressionMeasuredByAssayRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DifferentialExpressionMeasuredByAssayRelationship

    subject: Optional[Union[str, DifferentialExpressionStatementId]] = None
    object: Optional[Union[str, AssayId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DifferentialExpressionStatementId):
            self.subject = DifferentialExpressionStatementId(self.subject)

        if self.object is not None and not isinstance(self.object, AssayId):
            self.object = AssayId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DifferentialExpressionDerivedFromDatasetRelationship(ALSEvidenceRelationship):
    """
    Connects a differential expression result to the dataset from which it was derived.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["DifferentialExpressionDerivedFromDatasetRelationship"]
    class_class_curie: ClassVar[str] = "alskg:DifferentialExpressionDerivedFromDatasetRelationship"
    class_name: ClassVar[str] = "DifferentialExpressionDerivedFromDatasetRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DifferentialExpressionDerivedFromDatasetRelationship

    subject: Optional[Union[str, DifferentialExpressionStatementId]] = None
    object: Optional[Union[str, DatasetId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DifferentialExpressionStatementId):
            self.subject = DifferentialExpressionStatementId(self.subject)

        if self.object is not None and not isinstance(self.object, DatasetId):
            self.object = DatasetId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EvidenceStatementSupportedByEvidenceRelationship(ALSEvidenceRelationship):
    """
    Connects an evidence statement to supporting evidence.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["EvidenceStatementSupportedByEvidenceRelationship"]
    class_class_curie: ClassVar[str] = "alskg:EvidenceStatementSupportedByEvidenceRelationship"
    class_name: ClassVar[str] = "EvidenceStatementSupportedByEvidenceRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.EvidenceStatementSupportedByEvidenceRelationship

    subject: Optional[Union[str, EvidenceStatementId]] = None
    object: Optional[Union[str, EvidenceRecordId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, EvidenceStatementId):
            self.subject = EvidenceStatementId(self.subject)

        if self.object is not None and not isinstance(self.object, EvidenceRecordId):
            self.object = EvidenceRecordId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EvidenceStatementDerivedFromDatasetRelationship(ALSEvidenceRelationship):
    """
    Connects an evidence statement to the dataset from which it was derived.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["EvidenceStatementDerivedFromDatasetRelationship"]
    class_class_curie: ClassVar[str] = "alskg:EvidenceStatementDerivedFromDatasetRelationship"
    class_name: ClassVar[str] = "EvidenceStatementDerivedFromDatasetRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.EvidenceStatementDerivedFromDatasetRelationship

    subject: Optional[Union[str, EvidenceStatementId]] = None
    object: Optional[Union[str, DatasetId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, EvidenceStatementId):
            self.subject = EvidenceStatementId(self.subject)

        if self.object is not None and not isinstance(self.object, DatasetId):
            self.object = DatasetId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhenotypeObservationHasObservedPhenotypeRelationship(ALSSubtypeRelationship):
    """
    Connects a phenotype observation to the phenotype observed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["PhenotypeObservationHasObservedPhenotypeRelationship"]
    class_class_curie: ClassVar[str] = "alskg:PhenotypeObservationHasObservedPhenotypeRelationship"
    class_name: ClassVar[str] = "PhenotypeObservationHasObservedPhenotypeRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.PhenotypeObservationHasObservedPhenotypeRelationship

    subject: Optional[Union[str, PhenotypeObservationId]] = None
    object: Optional[Union[str, PhenotypeId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, PhenotypeObservationId):
            self.subject = PhenotypeObservationId(self.subject)

        if self.object is not None and not isinstance(self.object, PhenotypeId):
            self.object = PhenotypeId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhenotypeObservationOccursInSubtypeRelationship(ALSSubtypeRelationship):
    """
    Connects a phenotype observation to its subtype context.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["PhenotypeObservationOccursInSubtypeRelationship"]
    class_class_curie: ClassVar[str] = "alskg:PhenotypeObservationOccursInSubtypeRelationship"
    class_name: ClassVar[str] = "PhenotypeObservationOccursInSubtypeRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.PhenotypeObservationOccursInSubtypeRelationship

    subject: Optional[Union[str, PhenotypeObservationId]] = None
    object: Optional[Union[str, ALSSubtypeId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, PhenotypeObservationId):
            self.subject = PhenotypeObservationId(self.subject)

        if self.object is not None and not isinstance(self.object, ALSSubtypeId):
            self.object = ALSSubtypeId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiomarkerIndicatesPathogenicMechanismRelationship(ALSPathogenesisRelationship):
    """
    Connects a biomarker to a pathogenic mechanism it indicates.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["BiomarkerIndicatesPathogenicMechanismRelationship"]
    class_class_curie: ClassVar[str] = "alskg:BiomarkerIndicatesPathogenicMechanismRelationship"
    class_name: ClassVar[str] = "BiomarkerIndicatesPathogenicMechanismRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.BiomarkerIndicatesPathogenicMechanismRelationship

    subject: Optional[Union[str, BiomarkerId]] = None
    object: Optional[Union[str, PathogenicMechanismId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, BiomarkerId):
            self.subject = BiomarkerId(self.subject)

        if self.object is not None and not isinstance(self.object, PathogenicMechanismId):
            self.object = PathogenicMechanismId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugRepurposingHypothesisPrioritizesDrugRelationship(ALSTherapeuticRelationship):
    """
    Connects a drug repurposing hypothesis to the candidate drug being prioritized.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["DrugRepurposingHypothesisPrioritizesDrugRelationship"]
    class_class_curie: ClassVar[str] = "alskg:DrugRepurposingHypothesisPrioritizesDrugRelationship"
    class_name: ClassVar[str] = "DrugRepurposingHypothesisPrioritizesDrugRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugRepurposingHypothesisPrioritizesDrugRelationship

    subject: Optional[Union[str, DrugRepurposingHypothesisId]] = None
    object: Optional[Union[str, DrugId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugRepurposingHypothesisId):
            self.subject = DrugRepurposingHypothesisId(self.subject)

        if self.object is not None and not isinstance(self.object, DrugId):
            self.object = DrugId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugRepurposingHypothesisTargetsGeneRelationship(ALSTherapeuticRelationship):
    """
    Connects a drug repurposing hypothesis to an implicated target gene.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["DrugRepurposingHypothesisTargetsGeneRelationship"]
    class_class_curie: ClassVar[str] = "alskg:DrugRepurposingHypothesisTargetsGeneRelationship"
    class_name: ClassVar[str] = "DrugRepurposingHypothesisTargetsGeneRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugRepurposingHypothesisTargetsGeneRelationship

    subject: Optional[Union[str, DrugRepurposingHypothesisId]] = None
    object: Optional[Union[str, GeneId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugRepurposingHypothesisId):
            self.subject = DrugRepurposingHypothesisId(self.subject)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugRepurposingHypothesisModulatesPathogenicMechanismRelationship(ALSTherapeuticRelationship):
    """
    Connects a drug repurposing hypothesis to a pathogenic mechanism it proposes to modulate.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["DrugRepurposingHypothesisModulatesPathogenicMechanismRelationship"]
    class_class_curie: ClassVar[str] = "alskg:DrugRepurposingHypothesisModulatesPathogenicMechanismRelationship"
    class_name: ClassVar[str] = "DrugRepurposingHypothesisModulatesPathogenicMechanismRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.DrugRepurposingHypothesisModulatesPathogenicMechanismRelationship

    subject: Optional[Union[str, DrugRepurposingHypothesisId]] = None
    object: Optional[Union[str, PathogenicMechanismId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, DrugRepurposingHypothesisId):
            self.subject = DrugRepurposingHypothesisId(self.subject)

        if self.object is not None and not isinstance(self.object, PathogenicMechanismId):
            self.object = PathogenicMechanismId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TherapeuticInterventionTestedInClinicalTrialRelationship(ALSTherapeuticRelationship):
    """
    Connects a therapeutic intervention to a clinical trial that tests it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["TherapeuticInterventionTestedInClinicalTrialRelationship"]
    class_class_curie: ClassVar[str] = "alskg:TherapeuticInterventionTestedInClinicalTrialRelationship"
    class_name: ClassVar[str] = "TherapeuticInterventionTestedInClinicalTrialRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.TherapeuticInterventionTestedInClinicalTrialRelationship

    subject: Optional[Union[str, TherapeuticInterventionId]] = None
    object: Optional[Union[str, ClinicalTrialId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, TherapeuticInterventionId):
            self.subject = TherapeuticInterventionId(self.subject)

        if self.object is not None and not isinstance(self.object, ClinicalTrialId):
            self.object = ClinicalTrialId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ClinicalTrialEnrollsSubtypeRelationship(ALSTherapeuticRelationship):
    """
    Connects a clinical trial to an ALS subtype that it enrolls or targets.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["ClinicalTrialEnrollsSubtypeRelationship"]
    class_class_curie: ClassVar[str] = "alskg:ClinicalTrialEnrollsSubtypeRelationship"
    class_name: ClassVar[str] = "ClinicalTrialEnrollsSubtypeRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.ClinicalTrialEnrollsSubtypeRelationship

    subject: Optional[Union[str, ClinicalTrialId]] = None
    object: Optional[Union[str, ALSSubtypeId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, ClinicalTrialId):
            self.subject = ClinicalTrialId(self.subject)

        if self.object is not None and not isinstance(self.object, ALSSubtypeId):
            self.object = ALSSubtypeId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ModelSystemModelsSubtypeRelationship(ALSEvidenceRelationship):
    """
    Connects a model system to the ALS subtype it models.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["ModelSystemModelsSubtypeRelationship"]
    class_class_curie: ClassVar[str] = "alskg:ModelSystemModelsSubtypeRelationship"
    class_name: ClassVar[str] = "ModelSystemModelsSubtypeRelationship"
    class_model_uri: ClassVar[URIRef] = ALSKG.ModelSystemModelsSubtypeRelationship

    subject: Optional[Union[str, ModelSystemId]] = None
    object: Optional[Union[str, ALSSubtypeId]] = None
    original_optimus_relationship_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.subject is not None and not isinstance(self.subject, ModelSystemId):
            self.subject = ModelSystemId(self.subject)

        if self.object is not None and not isinstance(self.object, ALSSubtypeId):
            self.object = ALSSubtypeId(self.object)

        if self.original_optimus_relationship_type is not None and not isinstance(self.original_optimus_relationship_type, str):
            self.original_optimus_relationship_type = str(self.original_optimus_relationship_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ALSKGExtensionGraph(AnalyticalEntity):
    """
    Optional container class representing ALS-specific nodes and relationships added on top of an OptimusKG Neo4j
    graph.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["ALSKGExtensionGraph"]
    class_class_curie: ClassVar[str] = "alskg:ALSKGExtensionGraph"
    class_name: ClassVar[str] = "ALSKGExtensionGraph"
    class_model_uri: ClassVar[URIRef] = ALSKG.ALSKGExtensionGraph

    id: Union[str, ALSKGExtensionGraphId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ALSKGExtensionGraphId):
            self.id = ALSKGExtensionGraphId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExternalKnowledgeReference(ProvenanceEntity):
    """
    A reference to an entity, assertion, or record in an external knowledge graph or database, such as OptimusKG,
    PrimeKG, Open Targets, or a source dataset.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKG["ExternalKnowledgeReference"]
    class_class_curie: ClassVar[str] = "alskg:ExternalKnowledgeReference"
    class_name: ClassVar[str] = "ExternalKnowledgeReference"
    class_model_uri: ClassVar[URIRef] = ALSKG.ExternalKnowledgeReference

    id: Union[str, ExternalKnowledgeReferenceId] = None
    name: Optional[str] = None
    from_data_source: Optional[Union[str, DataSourceId]] = None
    url: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExternalKnowledgeReferenceId):
            self.id = ExternalKnowledgeReferenceId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.from_data_source is not None and not isinstance(self.from_data_source, DataSourceId):
            self.from_data_source = DataSourceId(self.from_data_source)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        super().__post_init__(**kwargs)


# Enumerations
class NodeLabelEnum(EnumDefinitionImpl):
    """
    Current three-letter OptimusKG Neo4j node labels.
    """
    ANA = PermissibleValue(
        text="ANA",
        description="Anatomy node label.")
    BPO = PermissibleValue(
        text="BPO",
        description="BiologicalProcess node label.")
    CCO = PermissibleValue(
        text="CCO",
        description="CellularComponent node label.")
    DIS = PermissibleValue(
        text="DIS",
        description="Disease node label.")
    DRG = PermissibleValue(
        text="DRG",
        description="Drug node label.")
    EXP = PermissibleValue(
        text="EXP",
        description="Exposure node label.")
    GEN = PermissibleValue(
        text="GEN",
        description="Gene node label.")
    MFN = PermissibleValue(
        text="MFN",
        description="MolecularFunction node label.")
    MST = PermissibleValue(
        text="MST",
        description="""MolecularSubtype node label. Represents transcriptome-derived molecular disease subtypes defined by unsupervised multi-omic clustering (e.g. ALS-Ox, ALS-Glia, ALS-TE from the NYGC ALS Consortium). Not an ontology-derived class; uses a synthetic ALSMS ID scheme.""")
    PHE = PermissibleValue(
        text="PHE",
        description="Phenotype node label.")
    PWY = PermissibleValue(
        text="PWY",
        description="Pathway node label.")
    ECX = PermissibleValue(
        text="ECX",
        description="""GeneExpressionContext node label. Represents reified gene expression context nodes linking a gene, molecular subtype, tissue/anatomy, expression direction, and provenance into a single semantic unit.""")
    ALS = PermissibleValue(
        text="ALS",
        description="""ALS focal disease node label used if materializing AmyotrophicLateralSclerosis separately from DIS.""")
    AST = PermissibleValue(
        text="AST",
        description="ALS subtype node.")
    CST = PermissibleValue(
        text="CST",
        description="Clinical subtype node.")
    GST = PermissibleValue(
        text="GST",
        description="Genetic subtype node.")
    PST = PermissibleValue(
        text="PST",
        description="""Pathology subtype or pathogenesis statement node depending on local implementation; prefer PSTMT for PathogenesisStatement to avoid collision.""")
    PGS = PermissibleValue(
        text="PGS",
        description="Progression subtype node.")
    SSC = PermissibleValue(
        text="SSC",
        description="Subtype scheme node.")
    SCR = PermissibleValue(
        text="SCR",
        description="Subtype criterion node.")
    VAR = PermissibleValue(
        text="VAR",
        description="Sequence variant node.")
    REX = PermissibleValue(
        text="REX",
        description="Repeat expansion node.")
    CLT = PermissibleValue(
        text="CLT",
        description="Cell type node.")
    PGM = PermissibleValue(
        text="PGM",
        description="Pathogenic mechanism node.")
    MEV = PermissibleValue(
        text="MEV",
        description="Molecular event node.")
    PAG = PermissibleValue(
        text="PAG",
        description="Protein aggregate node.")
    EST = PermissibleValue(
        text="EST",
        description="Evidence statement node.")
    PSTMT = PermissibleValue(
        text="PSTMT",
        description="Pathogenesis statement node.")
    DER = PermissibleValue(
        text="DER",
        description="Differential expression result node.")
    PAR = PermissibleValue(
        text="PAR",
        description="Protein abundance result node.")
    POB = PermissibleValue(
        text="POB",
        description="Phenotype observation node.")
    DST = PermissibleValue(
        text="DST",
        description="Disease stage node.")
    PRG = PermissibleValue(
        text="PRG",
        description="Progression pattern node.")
    BMK = PermissibleValue(
        text="BMK",
        description="Biomarker node.")
    STU = PermissibleValue(
        text="STU",
        description="Study node.")
    DAT = PermissibleValue(
        text="DAT",
        description="Dataset node.")
    COH = PermissibleValue(
        text="COH",
        description="Cohort node.")
    CMP = PermissibleValue(
        text="CMP",
        description="Comparator group node.")
    SMP = PermissibleValue(
        text="SMP",
        description="Sample node.")
    ASY = PermissibleValue(
        text="ASY",
        description="Assay node.")
    MOD = PermissibleValue(
        text="MOD",
        description="Model system node.")
    TX = PermissibleValue(
        text="TX",
        description="Therapeutic intervention node.")
    TRI = PermissibleValue(
        text="TRI",
        description="Clinical trial node.")
    DRH = PermissibleValue(
        text="DRH",
        description="Drug repurposing hypothesis node.")
    BAG = PermissibleValue(
        text="BAG",
        description="Biological agent node.")

    _defn = EnumDefinition(
        name="NodeLabelEnum",
        description="Current three-letter OptimusKG Neo4j node labels.",
    )

class RelationshipTypeEnum(EnumDefinitionImpl):
    """
    Current Neo4j relationship type strings observed in the installed OptimusKG graph.
    """
    ACTIVATOR = PermissibleValue(
        text="ACTIVATOR",
        description="Drug activates the gene product or target associated with the gene.")
    ADVERSE_DRUG_REACTION = PermissibleValue(
        text="ADVERSE_DRUG_REACTION",
        description="Drug-to-phenotype relationship indicating an adverse drug reaction.")
    AGONIST = PermissibleValue(
        text="AGONIST",
        description="Drug acts as an agonist of the gene product or target associated with the gene.")
    ALLOSTERIC_ANTAGONIST = PermissibleValue(
        text="ALLOSTERIC_ANTAGONIST",
        description="Drug acts as an allosteric antagonist of the gene product or target associated with the gene.")
    ANTAGONIST = PermissibleValue(
        text="ANTAGONIST",
        description="Drug acts as an antagonist of the gene product or target associated with the gene.")
    ASSOCIATED_WITH = PermissibleValue(
        text="ASSOCIATED_WITH",
        description="Association relationship; generally evidence-bearing but not necessarily causal.")
    BINDING_AGENT = PermissibleValue(
        text="BINDING_AGENT",
        description="Drug binds the gene product or target associated with the gene.")
    BLOCKER = PermissibleValue(
        text="BLOCKER",
        description="Drug blocks the gene product or target associated with the gene.")
    CARRIER = PermissibleValue(
        text="CARRIER",
        description="Drug-gene relationship where the gene product is a carrier in pharmacologic context.")
    CONTRAINDICATION = PermissibleValue(
        text="CONTRAINDICATION",
        description="Drug is contraindicated for a disease or phenotype context.")
    DEGRADER = PermissibleValue(
        text="DEGRADER",
        description="Drug degrades or induces degradation of the gene product or target.")
    ENZYME = PermissibleValue(
        text="ENZYME",
        description="""Drug-gene relationship where the gene product is an enzyme in drug metabolism or action context.""")
    EXPRESSION_ABSENT = PermissibleValue(
        text="EXPRESSION_ABSENT",
        description="Gene expression is reported absent in an anatomical context.")
    EXPRESSION_PRESENT = PermissibleValue(
        text="EXPRESSION_PRESENT",
        description="Gene expression is reported present in an anatomical context.")
    INDICATION = PermissibleValue(
        text="INDICATION",
        description="Drug has an indicated therapeutic use for a disease, phenotype, or biological process context.")
    INHIBITOR = PermissibleValue(
        text="INHIBITOR",
        description="Drug inhibits the gene product or target associated with the gene.")
    INTERACTS_WITH = PermissibleValue(
        text="INTERACTS_WITH",
        description="""Generic interaction or annotation-style relationship. Interpret according to the source and node pair; it may indicate interaction, membership, annotation, or functional context.""")
    INVERSE_AGONIST = PermissibleValue(
        text="INVERSE_AGONIST",
        description="Drug acts as an inverse agonist of the gene product or target.")
    IS_A = PermissibleValue(
        text="IS_A",
        description="Ontology subclass relationship indicating the source concept is a kind of the target concept.")
    LINKED_TO = PermissibleValue(
        text="LINKED_TO",
        description="""Generic linkage relation; interpret as associative rather than causal unless source evidence says otherwise.""")
    MODULATOR = PermissibleValue(
        text="MODULATOR",
        description="Drug modulates the gene product or target associated with the gene.")
    NEGATIVE_ALLOSTERIC_MODULATOR = PermissibleValue(
        text="NEGATIVE_ALLOSTERIC_MODULATOR",
        description="Drug acts as a negative allosteric modulator of the gene product or target.")
    NEGATIVE_MODULATOR = PermissibleValue(
        text="NEGATIVE_MODULATOR",
        description="Drug negatively modulates the gene product or target.")
    OFF_LABEL_USE = PermissibleValue(
        text="OFF_LABEL_USE",
        description="Drug has off-label use for a disease or phenotype context.")
    OPENER = PermissibleValue(
        text="OPENER",
        description="Drug opens the gene product or target, often a channel target.")
    PARENT = PermissibleValue(
        text="PARENT",
        description="""Parent-child hierarchy relationship from the source concept to a broader or parent concept in the same or related ontology.""")
    PARTIAL_AGONIST = PermissibleValue(
        text="PARTIAL_AGONIST",
        description="Drug acts as a partial agonist of the gene product or target.")
    HAS_MOLECULAR_SUBTYPE = PermissibleValue(
        text="HAS_MOLECULAR_SUBTYPE",
        description="""Disease-to-MolecularSubtype relationship indicating that a disease node is associated with or can present as a given molecular subtype. Direction is Disease -> MolecularSubtype. Not equivalent to ontological subclassing; represents a transcriptomic classification layer orthogonal to ontological disease hierarchy.""")
    DYSREGULATED_IN = PermissibleValue(
        text="DYSREGULATED_IN",
        description="""Gene-to-MolecularSubtype relationship indicating that a gene or genomic feature is differentially expressed (upregulated or downregulated) in a given molecular subtype relative to controls. Edge direction is Gene -> MolecularSubtype. Properties encode direction (UP/DOWN), tissue context (cortex or cord), and optionally cell model (e.g. iPSC motor neuron line).""")
    MEASURED_IN = PermissibleValue(
        text="MEASURED_IN",
        description="""MolecularSubtype-to-Anatomy relationship indicating the tissue or biological context in which the molecular subtype was characterized. Edge direction is MolecularSubtype -> Anatomy.""")
    PHENOTYPE_PRESENT = PermissibleValue(
        text="PHENOTYPE_PRESENT",
        description="Disease-to-phenotype relationship indicating the phenotype is present in the disease context.")
    POSITIVE_ALLOSTERIC_MODULATOR = PermissibleValue(
        text="POSITIVE_ALLOSTERIC_MODULATOR",
        description="Drug acts as a positive allosteric modulator of the gene product or target.")
    POSITIVE_MODULATOR = PermissibleValue(
        text="POSITIVE_MODULATOR",
        description="Drug positively modulates the gene product or target.")
    RELEASING_AGENT = PermissibleValue(
        text="RELEASING_AGENT",
        description="Drug acts as a releasing agent affecting the gene product or related target system.")
    STABILISER = PermissibleValue(
        text="STABILISER",
        description="Drug stabilizes the gene product or target.")
    SUBSTRATE = PermissibleValue(
        text="SUBSTRATE",
        description="Drug is a substrate of the gene product, often an enzyme or transporter.")
    SYNERGISTIC_INTERACTION = PermissibleValue(
        text="SYNERGISTIC_INTERACTION",
        description="Drug-drug relationship indicating synergistic interaction.")
    TARGET = PermissibleValue(
        text="TARGET",
        description="Drug targets the gene product associated with the gene.")
    TRANSPORTER = PermissibleValue(
        text="TRANSPORTER",
        description="Drug-gene relationship where the gene product is a transporter in pharmacologic context.")
    HAS_EXPRESSION_CONTEXT = PermissibleValue(
        text="HAS_EXPRESSION_CONTEXT",
        description="""Gene-to-GeneExpressionContext relationship. Links a gene to a reified expression context node that captures the molecular subtype, tissue/anatomy, expression direction, and provenance of a differential expression finding. Edge direction: Gene -> GeneExpressionContext.""")
    IN_ANATOMY = PermissibleValue(
        text="IN_ANATOMY",
        description="""GeneExpressionContext-to-Anatomy relationship. Links a reified expression context to the tissue or anatomical region in which the expression was measured. Optional: null when context is an iPSC cell model with no corresponding anatomy node. Edge direction: GeneExpressionContext -> Anatomy.""")
    HAS_ALS_SUBTYPE = PermissibleValue(
        text="HAS_ALS_SUBTYPE",
        description="ALS-KG extension relationship type for Neo4j materialization.")
    IS_SUBTYPE_OF = PermissibleValue(
        text="IS_SUBTYPE_OF",
        description="ALS-KG extension relationship type for Neo4j materialization.")
    HAS_SUBTYPE_SCHEME = PermissibleValue(
        text="HAS_SUBTYPE_SCHEME",
        description="ALS-KG extension relationship type for Neo4j materialization.")
    HAS_SUBTYPE_CRITERION = PermissibleValue(
        text="HAS_SUBTYPE_CRITERION",
        description="ALS-KG extension relationship type for Neo4j materialization.")
    DEFINED_BY_GENE = PermissibleValue(
        text="DEFINED_BY_GENE",
        description="ALS-KG extension relationship type for Neo4j materialization.")
    DEFINED_BY_VARIANT = PermissibleValue(
        text="DEFINED_BY_VARIANT",
        description="ALS-KG extension relationship type for Neo4j materialization.")
    HAS_PATHOGENIC_MECHANISM = PermissibleValue(
        text="HAS_PATHOGENIC_MECHANISM",
        description="ALS-KG extension relationship type for Neo4j materialization.")
    AFFECTS_ANATOMY = PermissibleValue(
        text="AFFECTS_ANATOMY",
        description="ALS-KG extension relationship type for Neo4j materialization.")
    INVOLVES_CELL_TYPE = PermissibleValue(
        text="INVOLVES_CELL_TYPE",
        description="ALS-KG extension relationship type for Neo4j materialization.")
    HAS_PHENOTYPE_OBSERVATION = PermissibleValue(
        text="HAS_PHENOTYPE_OBSERVATION",
        description="ALS-KG extension relationship type for Neo4j materialization.")
    HAS_VARIANT = PermissibleValue(
        text="HAS_VARIANT",
        description="ALS-KG extension relationship type for Neo4j materialization.")
    AFFECTS_GENE = PermissibleValue(
        text="AFFECTS_GENE",
        description="ALS-KG extension relationship type for Neo4j materialization.")
    ALTERS_PROTEIN = PermissibleValue(
        text="ALTERS_PROTEIN",
        description="ALS-KG extension relationship type for Neo4j materialization.")
    CONTRIBUTES_TO_PATHOGENIC_MECHANISM = PermissibleValue(
        text="CONTRIBUTES_TO_PATHOGENIC_MECHANISM",
        description="ALS-KG extension relationship type for Neo4j materialization.")
    OCCURS_IN_CELL_TYPE = PermissibleValue(
        text="OCCURS_IN_CELL_TYPE",
        description="ALS-KG extension relationship type for Neo4j materialization.")
    OCCURS_IN_ANATOMY = PermissibleValue(
        text="OCCURS_IN_ANATOMY",
        description="ALS-KG extension relationship type for Neo4j materialization.")
    MEASURES_GENE_EXPRESSION_OF = PermissibleValue(
        text="MEASURES_GENE_EXPRESSION_OF",
        description="ALS-KG extension relationship type for Neo4j materialization.")
    OCCURS_IN_SUBTYPE_CONTEXT = PermissibleValue(
        text="OCCURS_IN_SUBTYPE_CONTEXT",
        description="ALS-KG extension relationship type for Neo4j materialization.")
    MEASURED_BY_ASSAY = PermissibleValue(
        text="MEASURED_BY_ASSAY",
        description="ALS-KG extension relationship type for Neo4j materialization.")
    DERIVES_FROM_DATASET = PermissibleValue(
        text="DERIVES_FROM_DATASET",
        description="ALS-KG extension relationship type for Neo4j materialization.")
    SUPPORTED_BY = PermissibleValue(
        text="SUPPORTED_BY",
        description="ALS-KG extension relationship type for Neo4j materialization.")
    HAS_OBSERVED_PHENOTYPE = PermissibleValue(
        text="HAS_OBSERVED_PHENOTYPE",
        description="ALS-KG extension relationship type for Neo4j materialization.")
    INDICATES_PATHOGENIC_MECHANISM = PermissibleValue(
        text="INDICATES_PATHOGENIC_MECHANISM",
        description="ALS-KG extension relationship type for Neo4j materialization.")
    PRIORITIZES_DRUG = PermissibleValue(
        text="PRIORITIZES_DRUG",
        description="ALS-KG extension relationship type for Neo4j materialization.")
    TARGETS_GENE = PermissibleValue(
        text="TARGETS_GENE",
        description="ALS-KG extension relationship type for Neo4j materialization.")
    MODULATES_PATHOGENIC_MECHANISM = PermissibleValue(
        text="MODULATES_PATHOGENIC_MECHANISM",
        description="ALS-KG extension relationship type for Neo4j materialization.")
    TESTED_IN_CLINICAL_TRIAL = PermissibleValue(
        text="TESTED_IN_CLINICAL_TRIAL",
        description="ALS-KG extension relationship type for Neo4j materialization.")
    ENROLLS_SUBTYPE = PermissibleValue(
        text="ENROLLS_SUBTYPE",
        description="ALS-KG extension relationship type for Neo4j materialization.")
    MODELS_SUBTYPE = PermissibleValue(
        text="MODELS_SUBTYPE",
        description="ALS-KG extension relationship type for Neo4j materialization.")

    _defn = EnumDefinition(
        name="RelationshipTypeEnum",
        description="Current Neo4j relationship type strings observed in the installed OptimusKG graph.",
    )

class GeneBiotypeEnum(EnumDefinitionImpl):
    """
    Gene biotype classifications from HGNC/Ensembl, stored on Gene nodes.
    """
    protein_coding = PermissibleValue(
        text="protein_coding",
        description="Protein-coding gene")
    lncRNA = PermissibleValue(
        text="lncRNA",
        description="Long non-coding RNA")
    miRNA = PermissibleValue(
        text="miRNA",
        description="MicroRNA")
    snRNA = PermissibleValue(
        text="snRNA",
        description="Small nuclear RNA")
    snoRNA = PermissibleValue(
        text="snoRNA",
        description="Small nucleolar RNA")
    rRNA = PermissibleValue(
        text="rRNA",
        description="Ribosomal RNA")
    tRNA = PermissibleValue(
        text="tRNA",
        description="Transfer RNA")
    pseudogene = PermissibleValue(
        text="pseudogene",
        description="Pseudogene")
    misc_RNA = PermissibleValue(
        text="misc_RNA",
        description="Miscellaneous RNA")
    other = PermissibleValue(
        text="other",
        description="Other or unclassified biotype")

    _defn = EnumDefinition(
        name="GeneBiotypeEnum",
        description="Gene biotype classifications from HGNC/Ensembl, stored on Gene nodes.",
    )

class ExpressionCallQualityEnum(EnumDefinitionImpl):
    """
    Bgee expression call quality levels for ANA-GEN edges. Reflects confidence in gene expression calls derived from
    curated RNA-seq data.
    """
    gold = PermissibleValue(
        text="gold",
        description="High-confidence expression call (multiple concordant evidence types)")
    silver = PermissibleValue(
        text="silver",
        description="Moderate-confidence expression call")

    _defn = EnumDefinition(
        name="ExpressionCallQualityEnum",
        description="""Bgee expression call quality levels for ANA-GEN edges. Reflects confidence in gene expression calls derived from curated RNA-seq data.""",
    )

class DrugTractabilityModalityEnum(EnumDefinitionImpl):
    """
    Drug discovery modality categories for tractability assessments on Gene nodes. Sourced from Open Targets
    tractability pipeline.
    """
    sm = PermissibleValue(
        text="sm",
        description="Small molecule modality")
    ab = PermissibleValue(
        text="ab",
        description="Antibody modality")
    pr = PermissibleValue(
        text="pr",
        description="PROTAC (protein degrader) modality")
    oc = PermissibleValue(
        text="oc",
        description="Other clinical modality")

    _defn = EnumDefinition(
        name="DrugTractabilityModalityEnum",
        description="""Drug discovery modality categories for tractability assessments on Gene nodes. Sourced from Open Targets tractability pipeline.""",
    )

class HomologyTypeEnum(EnumDefinitionImpl):
    """
    Types of homology relationships in gene homologue annotations on Gene nodes.
    """
    ortholog_one2one = PermissibleValue(
        text="ortholog_one2one",
        description="One-to-one ortholog (single copy in both species)")
    ortholog_one2many = PermissibleValue(
        text="ortholog_one2many",
        description="One-to-many ortholog")
    ortholog_many2many = PermissibleValue(
        text="ortholog_many2many",
        description="Many-to-many ortholog")
    within_species_paralog = PermissibleValue(
        text="within_species_paralog",
        description="Paralog within the same species")
    other_paralog = PermissibleValue(
        text="other_paralog",
        description="Other paralogous relationship")
    gene_split = PermissibleValue(
        text="gene_split",
        description="Split gene (fragment)")

    _defn = EnumDefinition(
        name="HomologyTypeEnum",
        description="Types of homology relationships in gene homologue annotations on Gene nodes.",
    )

class ExpressionDirectionEnum(EnumDefinitionImpl):
    """
    Direction of differential expression relative to a comparator. Includes legacy OptimusKG values UP/DOWN and
    semantic ALS-KG values increased/decreased/unchanged/mixed/unknown.
    """
    UP = PermissibleValue(
        text="UP",
        description="""Gene or feature is upregulated (higher expression) in the molecular subtype compared to non-ALS controls.""")
    DOWN = PermissibleValue(
        text="DOWN",
        description="""Gene or feature is downregulated (lower expression) in the molecular subtype compared to non-ALS controls.""")
    increased = PermissibleValue(
        text="increased",
        description="Expression is higher in the case or condition group than in the comparator group.")
    decreased = PermissibleValue(
        text="decreased",
        description="Expression is lower in the case or condition group than in the comparator group.")
    unchanged = PermissibleValue(
        text="unchanged",
        description="No statistically meaningful expression change is observed.")
    mixed = PermissibleValue(
        text="mixed",
        description="Direction differs across cohorts, cell types, tissues, assays, or analytical methods.")
    unknown = PermissibleValue(
        text="unknown",
        description="Direction is not specified or cannot be determined.")

    _defn = EnumDefinition(
        name="ExpressionDirectionEnum",
        description="""Direction of differential expression relative to a comparator. Includes legacy OptimusKG values UP/DOWN and semantic ALS-KG values increased/decreased/unchanged/mixed/unknown.""",
    )

class BiologicalContextTypeEnum(EnumDefinitionImpl):
    """
    Type of biological context (tissue or cell model) in which molecular subtype gene expression was measured. Used on
    DYSREGULATED_IN edges.
    """
    postmortem_cortex = PermissibleValue(
        text="postmortem_cortex",
        description="Human postmortem motor cortex tissue sample.")
    postmortem_cord = PermissibleValue(
        text="postmortem_cord",
        description="Human postmortem spinal cord tissue sample.")
    iPSC_motor_neuron = PermissibleValue(
        text="iPSC_motor_neuron",
        description="iPSC-derived induced motor neuron cell model.")
    C9orf72_motor_neuron = PermissibleValue(
        text="C9orf72_motor_neuron",
        description="iPSC motor neuron model carrying C9orf72 repeat expansion mutation.")
    FUS_motor_neuron = PermissibleValue(
        text="FUS_motor_neuron",
        description="iPSC motor neuron model carrying FUS mutation.")
    TDP43_motor_neuron = PermissibleValue(
        text="TDP43_motor_neuron",
        description="iPSC motor neuron model carrying TARDBP/TDP-43 mutation.")
    spinal_cord_cervical = PermissibleValue(
        text="spinal_cord_cervical",
        description="Human postmortem cervical spinal cord tissue sample.")
    spinal_cord_thoracic = PermissibleValue(
        text="spinal_cord_thoracic",
        description="Human postmortem thoracic spinal cord tissue sample.")
    spinal_cord_lumbar = PermissibleValue(
        text="spinal_cord_lumbar",
        description="Human postmortem lumbar spinal cord tissue sample.")

    _defn = EnumDefinition(
        name="BiologicalContextTypeEnum",
        description="""Type of biological context (tissue or cell model) in which molecular subtype gene expression was measured. Used on DYSREGULATED_IN edges.""",
    )

class MolecularSubtypeClassificationBasisEnum(EnumDefinitionImpl):
    """
    Computational or experimental basis used to define and assign molecular subtypes. Describes how the subtype was
    derived from raw data.
    """
    unsupervised_transcriptomics = PermissibleValue(
        text="unsupervised_transcriptomics",
        description="""Molecular subtype derived by unsupervised clustering of postmortem transcriptomes (e.g. k-means, hierarchical clustering, NMF).""")
    deep_multiomics_classifier = PermissibleValue(
        text="deep_multiomics_classifier",
        description="""Molecular subtype assigned by a deep learning multi-omics classifier (e.g. the DANCer neural network from the NYGC ALS Consortium, Cell Reports 2025).""")
    bootstrap_clustering = PermissibleValue(
        text="bootstrap_clustering",
        description="Subtype assigned via bootstrap-based resampling and clustering stability analysis.")

    _defn = EnumDefinition(
        name="MolecularSubtypeClassificationBasisEnum",
        description="""Computational or experimental basis used to define and assign molecular subtypes. Describes how the subtype was derived from raw data.""",
    )

class SubtypeAxisEnum(EnumDefinitionImpl):
    """
    Axes along which ALS subtypes may be defined.
    """
    clinical_onset = PermissibleValue(
        text="clinical_onset",
        description="Subtype based on site or pattern of clinical onset, such as bulbar-onset or limb-onset ALS.")
    motor_neuron_involvement = PermissibleValue(
        text="motor_neuron_involvement",
        description="Subtype based on upper and lower motor neuron involvement pattern.")
    genetic = PermissibleValue(
        text="genetic",
        description="Subtype based on a gene, variant, repeat expansion, or inherited/genetic cause.")
    molecular = PermissibleValue(
        text="molecular",
        description="""Subtype derived from molecular data such as transcriptomics, proteomics, epigenomics, or multi-omics.""")
    pathology = PermissibleValue(
        text="pathology",
        description="Subtype based on pathological findings such as TDP-43, SOD1, or FUS proteinopathy.")
    cognitive_behavioral = PermissibleValue(
        text="cognitive_behavioral",
        description="Subtype based on cognitive or behavioral features such as ALS-FTD.")
    progression = PermissibleValue(
        text="progression",
        description="Subtype based on progression speed, survival, or functional decline.")
    anatomical = PermissibleValue(
        text="anatomical",
        description="Subtype based on dominant anatomical system or region affected.")
    model_system = PermissibleValue(
        text="model_system",
        description="Subtype or disease model defined in an experimental model system.")

    _defn = EnumDefinition(
        name="SubtypeAxisEnum",
        description="Axes along which ALS subtypes may be defined.",
    )

class EvidenceStrengthEnum(EnumDefinitionImpl):
    """
    Qualitative evidence strength for a scientific assertion.
    """
    definitive = PermissibleValue(
        text="definitive",
        description="Strongly supported by replicated, high-quality evidence or accepted clinical/genetic evidence.")
    strong = PermissibleValue(
        text="strong",
        description="Supported by substantial evidence from curated, experimental, or replicated sources.")
    moderate = PermissibleValue(
        text="moderate",
        description="Supported by some evidence, but with limitations or limited replication.")
    weak = PermissibleValue(
        text="weak",
        description="Supported by limited or preliminary evidence.")
    conflicting = PermissibleValue(
        text="conflicting",
        description="Evidence is inconsistent across studies or modalities.")
    unknown = PermissibleValue(
        text="unknown",
        description="Evidence strength has not been assessed.")

    _defn = EnumDefinition(
        name="EvidenceStrengthEnum",
        description="Qualitative evidence strength for a scientific assertion.",
    )

class EvidenceModalityEnum(EnumDefinitionImpl):
    """
    Modality or source type of evidence supporting a statement.
    """
    clinical = PermissibleValue(
        text="clinical",
        description="Evidence from clinical observations, examinations, diagnostic records, or clinical cohorts.")
    genetic = PermissibleValue(
        text="genetic",
        description="Evidence from genetic association, segregation, variant interpretation, or sequencing studies.")
    transcriptomic = PermissibleValue(
        text="transcriptomic",
        description="""Evidence from RNA-seq, single-cell RNA-seq, spatial transcriptomics, microarray, or related assays.""")
    proteomic = PermissibleValue(
        text="proteomic",
        description="""Evidence from protein abundance, localization, aggregation, or post-translational modification assays.""")
    pathology = PermissibleValue(
        text="pathology",
        description="Evidence from histology, immunostaining, digital pathology, or neuropathological assessment.")
    biomarker = PermissibleValue(
        text="biomarker",
        description="Evidence from molecular, imaging, electrophysiological, or clinical biomarkers.")
    experimental_model = PermissibleValue(
        text="experimental_model",
        description="Evidence from animal, cell, iPSC, organoid, or other model systems.")
    literature_curated = PermissibleValue(
        text="literature_curated",
        description="Evidence curated from scientific literature.")
    database_curated = PermissibleValue(
        text="database_curated",
        description="Evidence curated from a database or knowledge base.")
    computational_prediction = PermissibleValue(
        text="computational_prediction",
        description="""Evidence generated by computational model, embedding, machine learning, or algorithmic inference.""")

    _defn = EnumDefinition(
        name="EvidenceModalityEnum",
        description="Modality or source type of evidence supporting a statement.",
    )

class VariantConsequenceEnum(EnumDefinitionImpl):
    """
    Broad variant consequence categories relevant to ALS.
    """
    repeat_expansion = PermissibleValue(
        text="repeat_expansion",
        description="Pathogenic or potentially pathogenic repeat expansion.")
    missense_variant = PermissibleValue(
        text="missense_variant",
        description="Variant causing an amino-acid substitution.")
    nonsense_variant = PermissibleValue(
        text="nonsense_variant",
        description="Variant introducing a premature stop codon.")
    frameshift_variant = PermissibleValue(
        text="frameshift_variant",
        description="Insertion/deletion that shifts the coding frame.")
    splice_region_variant = PermissibleValue(
        text="splice_region_variant",
        description="Variant affecting splice region or splicing.")
    noncoding_variant = PermissibleValue(
        text="noncoding_variant",
        description="Variant located outside coding sequence.")
    structural_variant = PermissibleValue(
        text="structural_variant",
        description="Larger deletion, duplication, inversion, insertion, or translocation.")
    copy_number_variant = PermissibleValue(
        text="copy_number_variant",
        description="Copy number gain or loss.")
    unknown = PermissibleValue(
        text="unknown",
        description="Consequence is not known.")

    _defn = EnumDefinition(
        name="VariantConsequenceEnum",
        description="Broad variant consequence categories relevant to ALS.",
    )

class PathogenicityEnum(EnumDefinitionImpl):
    """
    Clinical or research pathogenicity interpretation of a genetic variant.
    """
    pathogenic = PermissibleValue(
        text="pathogenic",
        description="Variant is interpreted as disease-causing.")
    likely_pathogenic = PermissibleValue(
        text="likely_pathogenic",
        description="Variant is likely disease-causing.")
    risk_factor = PermissibleValue(
        text="risk_factor",
        description="""Variant is associated with increased disease risk but may not be fully penetrant or causal alone.""")
    uncertain_significance = PermissibleValue(
        text="uncertain_significance",
        description="Variant has uncertain pathogenic significance.")
    likely_benign = PermissibleValue(
        text="likely_benign",
        description="Variant is likely benign.")
    benign = PermissibleValue(
        text="benign",
        description="Variant is benign.")
    unknown = PermissibleValue(
        text="unknown",
        description="Pathogenicity is not known.")

    _defn = EnumDefinition(
        name="PathogenicityEnum",
        description="Clinical or research pathogenicity interpretation of a genetic variant.",
    )

class PathogenicMechanismEnum(EnumDefinitionImpl):
    """
    Major ALS pathogenic mechanism categories.
    """
    TDP43_proteinopathy = PermissibleValue(
        text="TDP43_proteinopathy",
        description="TDP-43 mislocalization, aggregation, loss of nuclear function, or gain of toxic function.")
    SOD1_toxicity = PermissibleValue(
        text="SOD1_toxicity",
        description="Toxic gain of function, aggregation, or dysfunction related to SOD1.")
    FUS_proteinopathy = PermissibleValue(
        text="FUS_proteinopathy",
        description="FUS mislocalization, aggregation, or RNA-binding dysfunction.")
    C9orf72_repeat_toxicity = PermissibleValue(
        text="C9orf72_repeat_toxicity",
        description="Toxicity related to C9orf72 repeat expansion, RNA foci, DPR proteins, or haploinsufficiency.")
    RNA_processing_dysfunction = PermissibleValue(
        text="RNA_processing_dysfunction",
        description="Disrupted RNA splicing, transport, stability, translation, or RNA granule biology.")
    impaired_proteostasis = PermissibleValue(
        text="impaired_proteostasis",
        description="Protein quality control, ubiquitin-proteasome, autophagy, or lysosomal dysfunction.")
    mitochondrial_dysfunction = PermissibleValue(
        text="mitochondrial_dysfunction",
        description="Mitochondrial impairment, energy metabolism dysfunction, or mitochondrial stress.")
    oxidative_stress = PermissibleValue(
        text="oxidative_stress",
        description="Oxidative damage or disrupted redox homeostasis.")
    neuroinflammation = PermissibleValue(
        text="neuroinflammation",
        description="""Inflammatory processes involving microglia, astrocytes, peripheral immune cells, complement, or cytokines.""")
    glutamate_excitotoxicity = PermissibleValue(
        text="glutamate_excitotoxicity",
        description="Excitotoxic injury involving glutamate signaling or uptake.")
    axonal_transport_defect = PermissibleValue(
        text="axonal_transport_defect",
        description="Defect in axonal transport, cytoskeletal dynamics, or neuromuscular connectivity.")
    nucleocytoplasmic_transport_defect = PermissibleValue(
        text="nucleocytoplasmic_transport_defect",
        description="Disrupted nuclear-cytoplasmic transport or nuclear pore biology.")
    DNA_repair_defect = PermissibleValue(
        text="DNA_repair_defect",
        description="Defect in DNA damage response or genome maintenance.")
    metabolic_dysfunction = PermissibleValue(
        text="metabolic_dysfunction",
        description="Altered metabolic state, lipid metabolism, or energy homeostasis.")
    neuromuscular_junction_dysfunction = PermissibleValue(
        text="neuromuscular_junction_dysfunction",
        description="Pathological change at the neuromuscular junction.")
    other = PermissibleValue(
        text="other",
        description="Other pathogenic mechanism not covered by the listed categories.")

    _defn = EnumDefinition(
        name="PathogenicMechanismEnum",
        description="Major ALS pathogenic mechanism categories.",
    )

class DrugActionDirectionEnum(EnumDefinitionImpl):
    """
    Direction or mechanism of a drug action on a target or biological process.
    """
    inhibits = PermissibleValue(
        text="inhibits",
        description="Drug decreases activity or function of the target.")
    activates = PermissibleValue(
        text="activates",
        description="Drug increases activity or function of the target.")
    antagonizes = PermissibleValue(
        text="antagonizes",
        description="Drug blocks receptor or target activation.")
    agonizes = PermissibleValue(
        text="agonizes",
        description="Drug activates receptor or target signaling.")
    modulates = PermissibleValue(
        text="modulates",
        description="Drug modulates the target without specifying direction.")
    degrades = PermissibleValue(
        text="degrades",
        description="Drug promotes degradation of the target.")
    stabilizes = PermissibleValue(
        text="stabilizes",
        description="Drug stabilizes the target, complex, or functional state.")
    binds = PermissibleValue(
        text="binds",
        description="Drug binds the target, direction not specified.")
    unknown = PermissibleValue(
        text="unknown",
        description="Drug action is not specified.")

    _defn = EnumDefinition(
        name="DrugActionDirectionEnum",
        description="Direction or mechanism of a drug action on a target or biological process.",
    )

class RepurposingStatusEnum(EnumDefinitionImpl):
    """
    Status of a drug repurposing hypothesis.
    """
    proposed = PermissibleValue(
        text="proposed",
        description="Hypothesis is proposed based on KG, literature, omics, or computational evidence.")
    prioritized = PermissibleValue(
        text="prioritized",
        description="Hypothesis has been ranked or prioritized for further study.")
    experimentally_supported = PermissibleValue(
        text="experimentally_supported",
        description="Hypothesis has supporting experimental-model evidence.")
    clinically_tested = PermissibleValue(
        text="clinically_tested",
        description="Hypothesis has been evaluated in a clinical trial or observational clinical study.")
    deprioritized = PermissibleValue(
        text="deprioritized",
        description="""Hypothesis is deprioritized because of weak evidence, wrong direction, toxicity, or lack of feasibility.""")
    rejected = PermissibleValue(
        text="rejected",
        description="Hypothesis is rejected based on negative or contradictory evidence.")

    _defn = EnumDefinition(
        name="RepurposingStatusEnum",
        description="Status of a drug repurposing hypothesis.",
    )

class SexEnum(EnumDefinitionImpl):
    """
    Biological sex or sex category used in a study or observation when reported.
    """
    female = PermissibleValue(
        text="female",
        description="Female.")
    male = PermissibleValue(
        text="male",
        description="Male.")
    mixed = PermissibleValue(
        text="mixed",
        description="Mixed or combined sex groups.")
    unknown = PermissibleValue(
        text="unknown",
        description="Sex not reported or unknown.")

    _defn = EnumDefinition(
        name="SexEnum",
        description="Biological sex or sex category used in a study or observation when reported.",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=ALSKG.id, domain=None, range=URIRef)

slots.original_optimus_label = Slot(uri=ALSKG.original_optimus_label, name="original_optimus_label", curie=ALSKG.curie('original_optimus_label'),
                   model_uri=ALSKG.original_optimus_label, domain=None, range=Optional[str])

slots.original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.original_optimus_relationship_type, domain=None, range=Optional[str])

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=ALSKG.name, domain=None, range=Optional[str])

slots.symbol = Slot(uri=ALSKG.symbol, name="symbol", curie=ALSKG.curie('symbol'),
                   model_uri=ALSKG.symbol, domain=None, range=Optional[str])

slots.source = Slot(uri=ALSKG.source, name="source", curie=ALSKG.curie('source'),
                   model_uri=ALSKG.source, domain=None, range=Optional[str])

slots.direct_sources = Slot(uri=ALSKG.direct_sources, name="direct_sources", curie=ALSKG.curie('direct_sources'),
                   model_uri=ALSKG.direct_sources, domain=None, range=Optional[Union[str, list[str]]])

slots.indirect_sources = Slot(uri=ALSKG.indirect_sources, name="indirect_sources", curie=ALSKG.curie('indirect_sources'),
                   model_uri=ALSKG.indirect_sources, domain=None, range=Optional[Union[str, list[str]]])

slots.subject = Slot(uri=ALSKG.subject, name="subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.subject, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.object = Slot(uri=ALSKG.object, name="object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.object, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.undirected = Slot(uri=ALSKG.undirected, name="undirected", curie=ALSKG.curie('undirected'),
                   model_uri=ALSKG.undirected, domain=None, range=Optional[Union[bool, Bool]])

slots.disease_has_molecular_subtype = Slot(uri=OKG.has_molecular_subtype, name="disease_has_molecular_subtype", curie=OKG.curie('has_molecular_subtype'),
                   model_uri=ALSKG.disease_has_molecular_subtype, domain=Disease, range=Optional[Union[str, MolecularSubtypeId]])

slots.molecular_subtype_has_parent_disease = Slot(uri=RDFS.subClassOf, name="molecular_subtype_has_parent_disease", curie=RDFS.curie('subClassOf'),
                   model_uri=ALSKG.molecular_subtype_has_parent_disease, domain=MolecularSubtype, range=Optional[Union[str, DiseaseId]])

slots.molecular_subtype_measured_in_anatomy = Slot(uri=OKG.measured_in, name="molecular_subtype_measured_in_anatomy", curie=OKG.curie('measured_in'),
                   model_uri=ALSKG.molecular_subtype_measured_in_anatomy, domain=MolecularSubtype, range=Optional[Union[str, AnatomyId]])

slots.anatomy_has_parent_anatomy = Slot(uri=RDFS.subClassOf, name="anatomy_has_parent_anatomy", curie=RDFS.curie('subClassOf'),
                   model_uri=ALSKG.anatomy_has_parent_anatomy, domain=Anatomy, range=Optional[Union[str, AnatomyId]])

slots.anatomy_has_gene_expression_absent = Slot(uri=OKG.expression_absent, name="anatomy_has_gene_expression_absent", curie=OKG.curie('expression_absent'),
                   model_uri=ALSKG.anatomy_has_gene_expression_absent, domain=Anatomy, range=Optional[Union[str, GeneId]])

slots.anatomy_has_gene_expression_present = Slot(uri=RO['0002206'], name="anatomy_has_gene_expression_present", curie=RO.curie('0002206'),
                   model_uri=ALSKG.anatomy_has_gene_expression_present, domain=Anatomy, range=Optional[Union[str, GeneId]])

slots.biological_process_is_subclass_of = Slot(uri=RDFS.subClassOf, name="biological_process_is_subclass_of", curie=RDFS.curie('subClassOf'),
                   model_uri=ALSKG.biological_process_is_subclass_of, domain=BiologicalProcess, range=Optional[Union[str, BiologicalProcessId]])

slots.biological_process_has_participating_gene = Slot(uri=BIOLINK.interacts_with, name="biological_process_has_participating_gene", curie=BIOLINK.curie('interacts_with'),
                   model_uri=ALSKG.biological_process_has_participating_gene, domain=BiologicalProcess, range=Optional[Union[str, GeneId]])

slots.cellular_component_is_subclass_of = Slot(uri=RDFS.subClassOf, name="cellular_component_is_subclass_of", curie=RDFS.curie('subClassOf'),
                   model_uri=ALSKG.cellular_component_is_subclass_of, domain=CellularComponent, range=Optional[Union[str, CellularComponentId]])

slots.cellular_component_has_located_gene = Slot(uri=BIOLINK.interacts_with, name="cellular_component_has_located_gene", curie=BIOLINK.curie('interacts_with'),
                   model_uri=ALSKG.cellular_component_has_located_gene, domain=CellularComponent, range=Optional[Union[str, GeneId]])

slots.disease_has_parent_disease = Slot(uri=RDFS.subClassOf, name="disease_has_parent_disease", curie=RDFS.curie('subClassOf'),
                   model_uri=ALSKG.disease_has_parent_disease, domain=Disease, range=Optional[Union[str, DiseaseId]])

slots.disease_associated_with_gene = Slot(uri=BIOLINK.associated_with, name="disease_associated_with_gene", curie=BIOLINK.curie('associated_with'),
                   model_uri=ALSKG.disease_associated_with_gene, domain=Disease, range=Optional[Union[str, GeneId]])

slots.disease_has_phenotype = Slot(uri=BIOLINK.has_phenotype, name="disease_has_phenotype", curie=BIOLINK.curie('has_phenotype'),
                   model_uri=ALSKG.disease_has_phenotype, domain=Disease, range=Optional[Union[str, PhenotypeId]])

slots.drug_has_indication_for_biological_process = Slot(uri=BIOLINK.treats, name="drug_has_indication_for_biological_process", curie=BIOLINK.curie('treats'),
                   model_uri=ALSKG.drug_has_indication_for_biological_process, domain=Drug, range=Optional[Union[str, BiologicalProcessId]])

slots.drug_contraindicated_for_disease = Slot(uri=BIOLINK.contraindicated_for, name="drug_contraindicated_for_disease", curie=BIOLINK.curie('contraindicated_for'),
                   model_uri=ALSKG.drug_contraindicated_for_disease, domain=Drug, range=Optional[Union[str, DiseaseId]])

slots.drug_indicated_for_disease = Slot(uri=BIOLINK.treats, name="drug_indicated_for_disease", curie=BIOLINK.curie('treats'),
                   model_uri=ALSKG.drug_indicated_for_disease, domain=Drug, range=Optional[Union[str, DiseaseId]])

slots.drug_used_off_label_for_disease = Slot(uri=OKG.off_label_use, name="drug_used_off_label_for_disease", curie=OKG.curie('off_label_use'),
                   model_uri=ALSKG.drug_used_off_label_for_disease, domain=Drug, range=Optional[Union[str, DiseaseId]])

slots.drug_has_parent_drug = Slot(uri=RDFS.subClassOf, name="drug_has_parent_drug", curie=RDFS.curie('subClassOf'),
                   model_uri=ALSKG.drug_has_parent_drug, domain=Drug, range=Optional[Union[str, DrugId]])

slots.drug_has_synergistic_interaction_with_drug = Slot(uri=BIOLINK.interacts_with, name="drug_has_synergistic_interaction_with_drug", curie=BIOLINK.curie('interacts_with'),
                   model_uri=ALSKG.drug_has_synergistic_interaction_with_drug, domain=Drug, range=Optional[Union[str, DrugId]])

slots.drug_activates_gene_product = Slot(uri=BIOLINK.increases_activity_of, name="drug_activates_gene_product", curie=BIOLINK.curie('increases_activity_of'),
                   model_uri=ALSKG.drug_activates_gene_product, domain=Drug, range=Optional[Union[str, GeneId]])

slots.drug_agonist_of_gene_product = Slot(uri=BIOLINK.affects_activity_of, name="drug_agonist_of_gene_product", curie=BIOLINK.curie('affects_activity_of'),
                   model_uri=ALSKG.drug_agonist_of_gene_product, domain=Drug, range=Optional[Union[str, GeneId]])

slots.drug_allosteric_antagonist_of_gene_product = Slot(uri=BIOLINK.decreases_activity_of, name="drug_allosteric_antagonist_of_gene_product", curie=BIOLINK.curie('decreases_activity_of'),
                   model_uri=ALSKG.drug_allosteric_antagonist_of_gene_product, domain=Drug, range=Optional[Union[str, GeneId]])

slots.drug_antagonist_of_gene_product = Slot(uri=BIOLINK.decreases_activity_of, name="drug_antagonist_of_gene_product", curie=BIOLINK.curie('decreases_activity_of'),
                   model_uri=ALSKG.drug_antagonist_of_gene_product, domain=Drug, range=Optional[Union[str, GeneId]])

slots.drug_binds_gene_product = Slot(uri=BIOLINK.physically_interacts_with, name="drug_binds_gene_product", curie=BIOLINK.curie('physically_interacts_with'),
                   model_uri=ALSKG.drug_binds_gene_product, domain=Drug, range=Optional[Union[str, GeneId]])

slots.drug_blocks_gene_product = Slot(uri=BIOLINK.decreases_activity_of, name="drug_blocks_gene_product", curie=BIOLINK.curie('decreases_activity_of'),
                   model_uri=ALSKG.drug_blocks_gene_product, domain=Drug, range=Optional[Union[str, GeneId]])

slots.drug_has_carrier_gene_product = Slot(uri=BIOLINK.related_to, name="drug_has_carrier_gene_product", curie=BIOLINK.curie('related_to'),
                   model_uri=ALSKG.drug_has_carrier_gene_product, domain=Drug, range=Optional[Union[str, GeneId]])

slots.drug_degrades_gene_product = Slot(uri=BIOLINK.decreases_abundance_of, name="drug_degrades_gene_product", curie=BIOLINK.curie('decreases_abundance_of'),
                   model_uri=ALSKG.drug_degrades_gene_product, domain=Drug, range=Optional[Union[str, GeneId]])

slots.drug_has_metabolizing_enzyme_gene_product = Slot(uri=BIOLINK.related_to, name="drug_has_metabolizing_enzyme_gene_product", curie=BIOLINK.curie('related_to'),
                   model_uri=ALSKG.drug_has_metabolizing_enzyme_gene_product, domain=Drug, range=Optional[Union[str, GeneId]])

slots.drug_inhibits_gene_product = Slot(uri=BIOLINK.decreases_activity_of, name="drug_inhibits_gene_product", curie=BIOLINK.curie('decreases_activity_of'),
                   model_uri=ALSKG.drug_inhibits_gene_product, domain=Drug, range=Optional[Union[str, GeneId]])

slots.drug_inverse_agonist_of_gene_product = Slot(uri=BIOLINK.decreases_activity_of, name="drug_inverse_agonist_of_gene_product", curie=BIOLINK.curie('decreases_activity_of'),
                   model_uri=ALSKG.drug_inverse_agonist_of_gene_product, domain=Drug, range=Optional[Union[str, GeneId]])

slots.drug_modulates_gene_product = Slot(uri=BIOLINK.affects_activity_of, name="drug_modulates_gene_product", curie=BIOLINK.curie('affects_activity_of'),
                   model_uri=ALSKG.drug_modulates_gene_product, domain=Drug, range=Optional[Union[str, GeneId]])

slots.drug_negative_allosteric_modulator_of_gene_product = Slot(uri=BIOLINK.decreases_activity_of, name="drug_negative_allosteric_modulator_of_gene_product", curie=BIOLINK.curie('decreases_activity_of'),
                   model_uri=ALSKG.drug_negative_allosteric_modulator_of_gene_product, domain=Drug, range=Optional[Union[str, GeneId]])

slots.drug_negatively_modulates_gene_product = Slot(uri=BIOLINK.decreases_activity_of, name="drug_negatively_modulates_gene_product", curie=BIOLINK.curie('decreases_activity_of'),
                   model_uri=ALSKG.drug_negatively_modulates_gene_product, domain=Drug, range=Optional[Union[str, GeneId]])

slots.drug_opens_gene_product = Slot(uri=BIOLINK.increases_activity_of, name="drug_opens_gene_product", curie=BIOLINK.curie('increases_activity_of'),
                   model_uri=ALSKG.drug_opens_gene_product, domain=Drug, range=Optional[Union[str, GeneId]])

slots.drug_partial_agonist_of_gene_product = Slot(uri=BIOLINK.affects_activity_of, name="drug_partial_agonist_of_gene_product", curie=BIOLINK.curie('affects_activity_of'),
                   model_uri=ALSKG.drug_partial_agonist_of_gene_product, domain=Drug, range=Optional[Union[str, GeneId]])

slots.drug_positive_allosteric_modulator_of_gene_product = Slot(uri=BIOLINK.increases_activity_of, name="drug_positive_allosteric_modulator_of_gene_product", curie=BIOLINK.curie('increases_activity_of'),
                   model_uri=ALSKG.drug_positive_allosteric_modulator_of_gene_product, domain=Drug, range=Optional[Union[str, GeneId]])

slots.drug_positively_modulates_gene_product = Slot(uri=BIOLINK.increases_activity_of, name="drug_positively_modulates_gene_product", curie=BIOLINK.curie('increases_activity_of'),
                   model_uri=ALSKG.drug_positively_modulates_gene_product, domain=Drug, range=Optional[Union[str, GeneId]])

slots.drug_releasing_agent_of_gene_product = Slot(uri=BIOLINK.affects, name="drug_releasing_agent_of_gene_product", curie=BIOLINK.curie('affects'),
                   model_uri=ALSKG.drug_releasing_agent_of_gene_product, domain=Drug, range=Optional[Union[str, GeneId]])

slots.drug_stabilizes_gene_product = Slot(uri=BIOLINK.affects_stability_of, name="drug_stabilizes_gene_product", curie=BIOLINK.curie('affects_stability_of'),
                   model_uri=ALSKG.drug_stabilizes_gene_product, domain=Drug, range=Optional[Union[str, GeneId]])

slots.drug_is_substrate_of_gene_product = Slot(uri=BIOLINK.related_to, name="drug_is_substrate_of_gene_product", curie=BIOLINK.curie('related_to'),
                   model_uri=ALSKG.drug_is_substrate_of_gene_product, domain=Drug, range=Optional[Union[str, GeneId]])

slots.drug_targets_gene_product = Slot(uri=BIOLINK.affects, name="drug_targets_gene_product", curie=BIOLINK.curie('affects'),
                   model_uri=ALSKG.drug_targets_gene_product, domain=Drug, range=Optional[Union[str, GeneId]])

slots.drug_has_transporter_gene_product = Slot(uri=BIOLINK.related_to, name="drug_has_transporter_gene_product", curie=BIOLINK.curie('related_to'),
                   model_uri=ALSKG.drug_has_transporter_gene_product, domain=Drug, range=Optional[Union[str, GeneId]])

slots.drug_has_adverse_phenotype = Slot(uri=BIOLINK.has_adverse_event, name="drug_has_adverse_phenotype", curie=BIOLINK.curie('has_adverse_event'),
                   model_uri=ALSKG.drug_has_adverse_phenotype, domain=Drug, range=Optional[Union[str, PhenotypeId]])

slots.drug_associated_with_phenotype = Slot(uri=BIOLINK.associated_with, name="drug_associated_with_phenotype", curie=BIOLINK.curie('associated_with'),
                   model_uri=ALSKG.drug_associated_with_phenotype, domain=Drug, range=Optional[Union[str, PhenotypeId]])

slots.drug_contraindicated_for_phenotype = Slot(uri=BIOLINK.contraindicated_for, name="drug_contraindicated_for_phenotype", curie=BIOLINK.curie('contraindicated_for'),
                   model_uri=ALSKG.drug_contraindicated_for_phenotype, domain=Drug, range=Optional[Union[str, PhenotypeId]])

slots.drug_indicated_for_phenotype = Slot(uri=BIOLINK.treats, name="drug_indicated_for_phenotype", curie=BIOLINK.curie('treats'),
                   model_uri=ALSKG.drug_indicated_for_phenotype, domain=Drug, range=Optional[Union[str, PhenotypeId]])

slots.drug_used_off_label_for_phenotype = Slot(uri=OKG.off_label_use, name="drug_used_off_label_for_phenotype", curie=OKG.curie('off_label_use'),
                   model_uri=ALSKG.drug_used_off_label_for_phenotype, domain=Drug, range=Optional[Union[str, PhenotypeId]])

slots.exposure_associated_with_biological_process = Slot(uri=BIOLINK.interacts_with, name="exposure_associated_with_biological_process", curie=BIOLINK.curie('interacts_with'),
                   model_uri=ALSKG.exposure_associated_with_biological_process, domain=Exposure, range=Optional[Union[str, BiologicalProcessId]])

slots.exposure_associated_with_cellular_component = Slot(uri=BIOLINK.interacts_with, name="exposure_associated_with_cellular_component", curie=BIOLINK.curie('interacts_with'),
                   model_uri=ALSKG.exposure_associated_with_cellular_component, domain=Exposure, range=Optional[Union[str, CellularComponentId]])

slots.exposure_linked_to_disease = Slot(uri=BIOLINK.related_to, name="exposure_linked_to_disease", curie=BIOLINK.curie('related_to'),
                   model_uri=ALSKG.exposure_linked_to_disease, domain=Exposure, range=Optional[Union[str, DiseaseId]])

slots.exposure_has_parent_exposure = Slot(uri=RDFS.subClassOf, name="exposure_has_parent_exposure", curie=RDFS.curie('subClassOf'),
                   model_uri=ALSKG.exposure_has_parent_exposure, domain=Exposure, range=Optional[Union[str, ExposureId]])

slots.exposure_associated_with_gene = Slot(uri=BIOLINK.interacts_with, name="exposure_associated_with_gene", curie=BIOLINK.curie('interacts_with'),
                   model_uri=ALSKG.exposure_associated_with_gene, domain=Exposure, range=Optional[Union[str, GeneId]])

slots.exposure_associated_with_molecular_function = Slot(uri=BIOLINK.interacts_with, name="exposure_associated_with_molecular_function", curie=BIOLINK.curie('interacts_with'),
                   model_uri=ALSKG.exposure_associated_with_molecular_function, domain=Exposure, range=Optional[Union[str, MolecularFunctionId]])

slots.gene_interacts_with_gene = Slot(uri=BIOLINK.interacts_with, name="gene_interacts_with_gene", curie=BIOLINK.curie('interacts_with'),
                   model_uri=ALSKG.gene_interacts_with_gene, domain=Gene, range=Optional[Union[str, GeneId]])

slots.molecular_function_enabled_by_gene = Slot(uri=BIOLINK.interacts_with, name="molecular_function_enabled_by_gene", curie=BIOLINK.curie('interacts_with'),
                   model_uri=ALSKG.molecular_function_enabled_by_gene, domain=MolecularFunction, range=Optional[Union[str, GeneId]])

slots.molecular_function_is_subclass_of = Slot(uri=RDFS.subClassOf, name="molecular_function_is_subclass_of", curie=RDFS.curie('subClassOf'),
                   model_uri=ALSKG.molecular_function_is_subclass_of, domain=MolecularFunction, range=Optional[Union[str, MolecularFunctionId]])

slots.phenotype_has_parent_disease = Slot(uri=RDFS.subClassOf, name="phenotype_has_parent_disease", curie=RDFS.curie('subClassOf'),
                   model_uri=ALSKG.phenotype_has_parent_disease, domain=Phenotype, range=Optional[Union[str, DiseaseId]])

slots.phenotype_associated_with_gene = Slot(uri=BIOLINK.associated_with, name="phenotype_associated_with_gene", curie=BIOLINK.curie('associated_with'),
                   model_uri=ALSKG.phenotype_associated_with_gene, domain=Phenotype, range=Optional[Union[str, GeneId]])

slots.phenotype_has_parent_phenotype = Slot(uri=RDFS.subClassOf, name="phenotype_has_parent_phenotype", curie=RDFS.curie('subClassOf'),
                   model_uri=ALSKG.phenotype_has_parent_phenotype, domain=Phenotype, range=Optional[Union[str, PhenotypeId]])

slots.pathway_has_member_gene = Slot(uri=BIOLINK.interacts_with, name="pathway_has_member_gene", curie=BIOLINK.curie('interacts_with'),
                   model_uri=ALSKG.pathway_has_member_gene, domain=Pathway, range=Optional[Union[str, GeneId]])

slots.pathway_has_parent_pathway = Slot(uri=RDFS.subClassOf, name="pathway_has_parent_pathway", curie=RDFS.curie('subClassOf'),
                   model_uri=ALSKG.pathway_has_parent_pathway, domain=Pathway, range=Optional[Union[str, PathwayId]])

slots.encodes = Slot(uri=RO['0002205'], name="encodes", curie=RO.curie('0002205'),
                   model_uri=ALSKG.encodes, domain=Gene, range=Optional[Union[Union[str, ProteinId], list[Union[str, ProteinId]]]])

slots.has_isoform = Slot(uri=ALSKG.has_isoform, name="has_isoform", curie=ALSKG.curie('has_isoform'),
                   model_uri=ALSKG.has_isoform, domain=Protein, range=Optional[Union[Union[str, ProteinIsoformId], list[Union[str, ProteinIsoformId]]]])

slots.has_database_accession = Slot(uri=ALSKG.has_database_accession, name="has_database_accession", curie=ALSKG.curie('has_database_accession'),
                   model_uri=ALSKG.has_database_accession, domain=None, range=Optional[Union[Union[str, DatabaseAccessionId], list[Union[str, DatabaseAccessionId]]]])

slots.from_data_source = Slot(uri=PROV.wasDerivedFrom, name="from_data_source", curie=PROV.curie('wasDerivedFrom'),
                   model_uri=ALSKG.from_data_source, domain=None, range=Optional[Union[str, DataSourceId]])

slots.accession = Slot(uri=ALSKG.accession, name="accession", curie=ALSKG.curie('accession'),
                   model_uri=ALSKG.accession, domain=None, range=Optional[str])

slots.version = Slot(uri=PAV.version, name="version", curie=PAV.curie('version'),
                   model_uri=ALSKG.version, domain=None, range=Optional[str])

slots.status = Slot(uri=ALSKG.status, name="status", curie=ALSKG.curie('status'),
                   model_uri=ALSKG.status, domain=None, range=Optional[str])

slots.source_type = Slot(uri=ALSKG.source_type, name="source_type", curie=ALSKG.curie('source_type'),
                   model_uri=ALSKG.source_type, domain=None, range=Optional[str])

slots.url = Slot(uri=SCHEMA.url, name="url", curie=SCHEMA.curie('url'),
                   model_uri=ALSKG.url, domain=None, range=Optional[str])

slots.pmid = Slot(uri=BIOLINK.pmid, name="pmid", curie=BIOLINK.curie('pmid'),
                   model_uri=ALSKG.pmid, domain=None, range=Optional[str])

slots.doi = Slot(uri=BIOLINK.doi, name="doi", curie=BIOLINK.curie('doi'),
                   model_uri=ALSKG.doi, domain=None, range=Optional[str])

slots.has_publication = Slot(uri=BIOLINK.publications, name="has_publication", curie=BIOLINK.curie('publications'),
                   model_uri=ALSKG.has_publication, domain=None, range=Optional[Union[Union[str, PublicationId], list[Union[str, PublicationId]]]])

slots.evidence_type = Slot(uri=BIOLINK.has_evidence, name="evidence_type", curie=BIOLINK.curie('has_evidence'),
                   model_uri=ALSKG.evidence_type, domain=None, range=Optional[str])

slots.confidence_score = Slot(uri=ALSKG.confidence_score, name="confidence_score", curie=ALSKG.curie('confidence_score'),
                   model_uri=ALSKG.confidence_score, domain=None, range=Optional[float])

slots.synonym_scope = Slot(uri=ALSKG.synonym_scope, name="synonym_scope", curie=ALSKG.curie('synonym_scope'),
                   model_uri=ALSKG.synonym_scope, domain=None, range=Optional[str])

slots.has_synonym = Slot(uri=SKOS.altLabel, name="has_synonym", curie=SKOS.curie('altLabel'),
                   model_uri=ALSKG.has_synonym, domain=None, range=Optional[Union[Union[str, SynonymId], list[Union[str, SynonymId]]]])

slots.has_cross_reference = Slot(uri=BIOLINK.xref, name="has_cross_reference", curie=BIOLINK.curie('xref'),
                   model_uri=ALSKG.has_cross_reference, domain=None, range=Optional[Union[Union[str, DatabaseAccessionId], list[Union[str, DatabaseAccessionId]]]])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=ALSKG.description, domain=None, range=Optional[str])

slots.definition = Slot(uri=IAO['0000115'], name="definition", curie=IAO.curie('0000115'),
                   model_uri=ALSKG.definition, domain=None, range=Optional[str])

slots.synonyms = Slot(uri=SKOS.altLabel, name="synonyms", curie=SKOS.curie('altLabel'),
                   model_uri=ALSKG.synonyms, domain=None, range=Optional[Union[str, list[str]]])

slots.xrefs = Slot(uri=BIOLINK.xref, name="xrefs", curie=BIOLINK.curie('xref'),
                   model_uri=ALSKG.xrefs, domain=None, range=Optional[Union[str, list[str]]])

slots.ontology = Slot(uri=ALSKG.ontology, name="ontology", curie=ALSKG.curie('ontology'),
                   model_uri=ALSKG.ontology, domain=None, range=Optional[Union[str, OntologyMetadataId]])

slots.code = Slot(uri=ALSKG.code, name="code", curie=ALSKG.curie('code'),
                   model_uri=ALSKG.code, domain=None, range=Optional[str])

slots.type = Slot(uri=ALSKG.type, name="type", curie=ALSKG.curie('type'),
                   model_uri=ALSKG.type, domain=None, range=Optional[str])

slots.parents = Slot(uri=ALSKG.parents, name="parents", curie=ALSKG.curie('parents'),
                   model_uri=ALSKG.parents, domain=None, range=Optional[Union[str, list[str]]])

slots.children = Slot(uri=ALSKG.children, name="children", curie=ALSKG.curie('children'),
                   model_uri=ALSKG.children, domain=None, range=Optional[Union[str, list[str]]])

slots.ancestors = Slot(uri=ALSKG.ancestors, name="ancestors", curie=ALSKG.curie('ancestors'),
                   model_uri=ALSKG.ancestors, domain=None, range=Optional[Union[str, list[str]]])

slots.descendants = Slot(uri=ALSKG.descendants, name="descendants", curie=ALSKG.curie('descendants'),
                   model_uri=ALSKG.descendants, domain=None, range=Optional[Union[str, list[str]]])

slots.is_leaf = Slot(uri=ALSKG.is_leaf, name="is_leaf", curie=ALSKG.curie('is_leaf'),
                   model_uri=ALSKG.is_leaf, domain=None, range=Optional[Union[bool, Bool]])

slots.exact_synonyms = Slot(uri=ALSKG.exact_synonyms, name="exact_synonyms", curie=ALSKG.curie('exact_synonyms'),
                   model_uri=ALSKG.exact_synonyms, domain=None, range=Optional[Union[str, list[str]]])

slots.related_synonyms = Slot(uri=ALSKG.related_synonyms, name="related_synonyms", curie=ALSKG.curie('related_synonyms'),
                   model_uri=ALSKG.related_synonyms, domain=None, range=Optional[Union[str, list[str]]])

slots.narrow_synonyms = Slot(uri=ALSKG.narrow_synonyms, name="narrow_synonyms", curie=ALSKG.curie('narrow_synonyms'),
                   model_uri=ALSKG.narrow_synonyms, domain=None, range=Optional[Union[str, list[str]]])

slots.broad_synonyms = Slot(uri=ALSKG.broad_synonyms, name="broad_synonyms", curie=ALSKG.curie('broad_synonyms'),
                   model_uri=ALSKG.broad_synonyms, domain=None, range=Optional[Union[str, list[str]]])

slots.obsolete_terms = Slot(uri=ALSKG.obsolete_terms, name="obsolete_terms", curie=ALSKG.curie('obsolete_terms'),
                   model_uri=ALSKG.obsolete_terms, domain=None, range=Optional[Union[str, list[str]]])

slots.obsolete_xrefs = Slot(uri=ALSKG.obsolete_xrefs, name="obsolete_xrefs", curie=ALSKG.curie('obsolete_xrefs'),
                   model_uri=ALSKG.obsolete_xrefs, domain=None, range=Optional[Union[str, list[str]]])

slots.concept_ids = Slot(uri=ALSKG.concept_ids, name="concept_ids", curie=ALSKG.curie('concept_ids'),
                   model_uri=ALSKG.concept_ids, domain=None, range=Optional[Union[str, list[str]]])

slots.concept_names = Slot(uri=ALSKG.concept_names, name="concept_names", curie=ALSKG.curie('concept_names'),
                   model_uri=ALSKG.concept_names, domain=None, range=Optional[Union[str, list[str]]])

slots.umls_cui = Slot(uri=ALSKG.umls_cui, name="umls_cui", curie=ALSKG.curie('umls_cui'),
                   model_uri=ALSKG.umls_cui, domain=None, range=Optional[str])

slots.snomed_full_names = Slot(uri=ALSKG.snomed_full_names, name="snomed_full_names", curie=ALSKG.curie('snomed_full_names'),
                   model_uri=ALSKG.snomed_full_names, domain=None, range=Optional[Union[str, list[str]]])

slots.snomed_concept_ids = Slot(uri=ALSKG.snomed_concept_ids, name="snomed_concept_ids", curie=ALSKG.curie('snomed_concept_ids'),
                   model_uri=ALSKG.snomed_concept_ids, domain=None, range=Optional[Union[str, list[str]]])

slots.cui_semantic_type = Slot(uri=ALSKG.cui_semantic_type, name="cui_semantic_type", curie=ALSKG.curie('cui_semantic_type'),
                   model_uri=ALSKG.cui_semantic_type, domain=None, range=Optional[str])

slots.highest_clinical_trial_phase = Slot(uri=ALSKG.highest_clinical_trial_phase, name="highest_clinical_trial_phase", curie=ALSKG.curie('highest_clinical_trial_phase'),
                   model_uri=ALSKG.highest_clinical_trial_phase, domain=None, range=Optional[float])

slots.reference_ids = Slot(uri=ALSKG.reference_ids, name="reference_ids", curie=ALSKG.curie('reference_ids'),
                   model_uri=ALSKG.reference_ids, domain=None, range=Optional[Union[str, list[str]]])

slots.structure_id = Slot(uri=ALSKG.structure_id, name="structure_id", curie=ALSKG.curie('structure_id'),
                   model_uri=ALSKG.structure_id, domain=None, range=Optional[str])

slots.drug_disease_id = Slot(uri=ALSKG.drug_disease_id, name="drug_disease_id", curie=ALSKG.curie('drug_disease_id'),
                   model_uri=ALSKG.drug_disease_id, domain=None, range=Optional[str])

slots.source_ids = Slot(uri=ALSKG.source_ids, name="source_ids", curie=ALSKG.curie('source_ids'),
                   model_uri=ALSKG.source_ids, domain=None, range=Optional[Union[str, list[str]]])

slots.has_evidence_record = Slot(uri=BIOLINK.has_evidence, name="has_evidence_record", curie=BIOLINK.curie('has_evidence'),
                   model_uri=ALSKG.has_evidence_record, domain=None, range=Optional[Union[Union[str, EvidenceRecordId], list[Union[str, EvidenceRecordId]]]])

slots.gene_has_expression_context = Slot(uri=OKG.has_expression_context, name="gene_has_expression_context", curie=OKG.curie('has_expression_context'),
                   model_uri=ALSKG.gene_has_expression_context, domain=Gene, range=Optional[Union[str, GeneExpressionContextId]])

slots.expression_context_in_anatomy = Slot(uri=OKG.in_anatomy, name="expression_context_in_anatomy", curie=OKG.curie('in_anatomy'),
                   model_uri=ALSKG.expression_context_in_anatomy, domain=GeneExpressionContext, range=Optional[Union[str, AnatomyId]])

slots.expression_context_in_molecular_subtype = Slot(uri=OKG.in_molecular_subtype, name="expression_context_in_molecular_subtype", curie=OKG.curie('in_molecular_subtype'),
                   model_uri=ALSKG.expression_context_in_molecular_subtype, domain=GeneExpressionContext, range=Optional[Union[str, MolecularSubtypeId]])

slots.has_source = Slot(uri=PROV.wasDerivedFrom, name="has_source", curie=PROV.curie('wasDerivedFrom'),
                   model_uri=ALSKG.has_source, domain=None, range=Optional[Union[Union[str, DataSourceId], list[Union[str, DataSourceId]]]])

slots.is_supported_by = Slot(uri=RO['0002558'], name="is_supported_by", curie=RO.curie('0002558'),
                   model_uri=ALSKG.is_supported_by, domain=None, range=Optional[Union[Union[str, EvidenceRecordId], list[Union[str, EvidenceRecordId]]]])

slots.has_evidence_strength = Slot(uri=ALSKG.has_evidence_strength, name="has_evidence_strength", curie=ALSKG.curie('has_evidence_strength'),
                   model_uri=ALSKG.has_evidence_strength, domain=None, range=Optional[Union[str, "EvidenceStrengthEnum"]])

slots.has_confidence_score = Slot(uri=ALSKG.has_confidence_score, name="has_confidence_score", curie=ALSKG.curie('has_confidence_score'),
                   model_uri=ALSKG.has_confidence_score, domain=None, range=Optional[Union[float, Probability]])

slots.has_subject = Slot(uri=RDF.subject, name="has_subject", curie=RDF.curie('subject'),
                   model_uri=ALSKG.has_subject, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.has_predicate = Slot(uri=RDF.predicate, name="has_predicate", curie=RDF.curie('predicate'),
                   model_uri=ALSKG.has_predicate, domain=None, range=Optional[str])

slots.has_object = Slot(uri=RDF.object, name="has_object", curie=RDF.curie('object'),
                   model_uri=ALSKG.has_object, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.has_subtype = Slot(uri=BIOLINK.has_subclass, name="has_subtype", curie=BIOLINK.curie('has_subclass'),
                   model_uri=ALSKG.has_subtype, domain=None, range=Optional[Union[Union[str, ALSSubtypeId], list[Union[str, ALSSubtypeId]]]])

slots.is_subtype_of = Slot(uri=ALSKG.is_subtype_of, name="is_subtype_of", curie=ALSKG.curie('is_subtype_of'),
                   model_uri=ALSKG.is_subtype_of, domain=None, range=Optional[Union[str, DiseaseId]])

slots.has_subtype_axis = Slot(uri=ALSKG.has_subtype_axis, name="has_subtype_axis", curie=ALSKG.curie('has_subtype_axis'),
                   model_uri=ALSKG.has_subtype_axis, domain=None, range=Optional[Union[str, "SubtypeAxisEnum"]])

slots.has_subtype_scheme = Slot(uri=ALSKG.has_subtype_scheme, name="has_subtype_scheme", curie=ALSKG.curie('has_subtype_scheme'),
                   model_uri=ALSKG.has_subtype_scheme, domain=None, range=Optional[Union[Union[str, SubtypeSchemeId], list[Union[str, SubtypeSchemeId]]]])

slots.has_subtype_criterion = Slot(uri=ALSKG.has_subtype_criterion, name="has_subtype_criterion", curie=ALSKG.curie('has_subtype_criterion'),
                   model_uri=ALSKG.has_subtype_criterion, domain=None, range=Optional[Union[Union[str, SubtypeCriterionId], list[Union[str, SubtypeCriterionId]]]])

slots.is_defined_by_gene = Slot(uri=ALSKG.is_defined_by_gene, name="is_defined_by_gene", curie=ALSKG.curie('is_defined_by_gene'),
                   model_uri=ALSKG.is_defined_by_gene, domain=None, range=Optional[Union[Union[str, GeneId], list[Union[str, GeneId]]]])

slots.is_defined_by_variant = Slot(uri=ALSKG.is_defined_by_variant, name="is_defined_by_variant", curie=ALSKG.curie('is_defined_by_variant'),
                   model_uri=ALSKG.is_defined_by_variant, domain=None, range=Optional[Union[Union[str, SequenceVariantId], list[Union[str, SequenceVariantId]]]])

slots.is_defined_by_phenotype = Slot(uri=ALSKG.is_defined_by_phenotype, name="is_defined_by_phenotype", curie=ALSKG.curie('is_defined_by_phenotype'),
                   model_uri=ALSKG.is_defined_by_phenotype, domain=None, range=Optional[Union[Union[str, PhenotypeId], list[Union[str, PhenotypeId]]]])

slots.is_defined_by_pathogenic_mechanism = Slot(uri=ALSKG.is_defined_by_pathogenic_mechanism, name="is_defined_by_pathogenic_mechanism", curie=ALSKG.curie('is_defined_by_pathogenic_mechanism'),
                   model_uri=ALSKG.is_defined_by_pathogenic_mechanism, domain=None, range=Optional[Union[Union[str, PathogenicMechanismId], list[Union[str, PathogenicMechanismId]]]])

slots.affects_anatomy = Slot(uri=RO['0002131'], name="affects_anatomy", curie=RO.curie('0002131'),
                   model_uri=ALSKG.affects_anatomy, domain=None, range=Optional[Union[Union[str, AnatomyId], list[Union[str, AnatomyId]]]])

slots.involves_cell_type = Slot(uri=ALSKG.involves_cell_type, name="involves_cell_type", curie=ALSKG.curie('involves_cell_type'),
                   model_uri=ALSKG.involves_cell_type, domain=None, range=Optional[Union[Union[str, CellTypeId], list[Union[str, CellTypeId]]]])

slots.occurs_in_anatomy = Slot(uri=ALSKG.occurs_in_anatomy, name="occurs_in_anatomy", curie=ALSKG.curie('occurs_in_anatomy'),
                   model_uri=ALSKG.occurs_in_anatomy, domain=None, range=Optional[Union[Union[str, AnatomyId], list[Union[str, AnatomyId]]]])

slots.occurs_in_cell_type = Slot(uri=ALSKG.occurs_in_cell_type, name="occurs_in_cell_type", curie=ALSKG.curie('occurs_in_cell_type'),
                   model_uri=ALSKG.occurs_in_cell_type, domain=None, range=Optional[Union[Union[str, CellTypeId], list[Union[str, CellTypeId]]]])

slots.occurs_in_disease_context = Slot(uri=ALSKG.occurs_in_disease_context, name="occurs_in_disease_context", curie=ALSKG.curie('occurs_in_disease_context'),
                   model_uri=ALSKG.occurs_in_disease_context, domain=None, range=Optional[Union[str, DiseaseId]])

slots.occurs_in_subtype_context = Slot(uri=ALSKG.occurs_in_subtype_context, name="occurs_in_subtype_context", curie=ALSKG.curie('occurs_in_subtype_context'),
                   model_uri=ALSKG.occurs_in_subtype_context, domain=None, range=Optional[Union[str, ALSSubtypeId]])

slots.occurs_in_cohort = Slot(uri=ALSKG.occurs_in_cohort, name="occurs_in_cohort", curie=ALSKG.curie('occurs_in_cohort'),
                   model_uri=ALSKG.occurs_in_cohort, domain=None, range=Optional[Union[str, CohortId]])

slots.has_gene = Slot(uri=RO['0004001'], name="has_gene", curie=RO.curie('0004001'),
                   model_uri=ALSKG.has_gene, domain=None, range=Optional[Union[Union[str, GeneId], list[Union[str, GeneId]]]])

slots.encodes_protein = Slot(uri=RO['0002205'], name="encodes_protein", curie=RO.curie('0002205'),
                   model_uri=ALSKG.encodes_protein, domain=None, range=Optional[Union[Union[str, ProteinId], list[Union[str, ProteinId]]]])

slots.comes_from_data_source = Slot(uri=PROV.wasAttributedTo, name="comes_from_data_source", curie=PROV.curie('wasAttributedTo'),
                   model_uri=ALSKG.comes_from_data_source, domain=None, range=Optional[Union[str, DataSourceId]])

slots.has_variant = Slot(uri=ALSKG.has_variant, name="has_variant", curie=ALSKG.curie('has_variant'),
                   model_uri=ALSKG.has_variant, domain=None, range=Optional[Union[Union[str, SequenceVariantId], list[Union[str, SequenceVariantId]]]])

slots.affects_gene = Slot(uri=RO['0004020'], name="affects_gene", curie=RO.curie('0004020'),
                   model_uri=ALSKG.affects_gene, domain=None, range=Optional[Union[Union[str, GeneId], list[Union[str, GeneId]]]])

slots.alters_protein = Slot(uri=ALSKG.alters_protein, name="alters_protein", curie=ALSKG.curie('alters_protein'),
                   model_uri=ALSKG.alters_protein, domain=None, range=Optional[Union[Union[str, ProteinId], list[Union[str, ProteinId]]]])

slots.has_variant_consequence = Slot(uri=SO['0001537'], name="has_variant_consequence", curie=SO.curie('0001537'),
                   model_uri=ALSKG.has_variant_consequence, domain=None, range=Optional[Union[str, "VariantConsequenceEnum"]])

slots.has_pathogenicity = Slot(uri=ALSKG.has_pathogenicity, name="has_pathogenicity", curie=ALSKG.curie('has_pathogenicity'),
                   model_uri=ALSKG.has_pathogenicity, domain=None, range=Optional[Union[str, "PathogenicityEnum"]])

slots.has_repeat_motif = Slot(uri=ALSKG.has_repeat_motif, name="has_repeat_motif", curie=ALSKG.curie('has_repeat_motif'),
                   model_uri=ALSKG.has_repeat_motif, domain=None, range=Optional[str])

slots.has_repeat_count = Slot(uri=ALSKG.has_repeat_count, name="has_repeat_count", curie=ALSKG.curie('has_repeat_count'),
                   model_uri=ALSKG.has_repeat_count, domain=None, range=Optional[int])

slots.has_pathogenic_mechanism = Slot(uri=ALSKG.has_pathogenic_mechanism, name="has_pathogenic_mechanism", curie=ALSKG.curie('has_pathogenic_mechanism'),
                   model_uri=ALSKG.has_pathogenic_mechanism, domain=None, range=Optional[Union[Union[str, PathogenicMechanismId], list[Union[str, PathogenicMechanismId]]]])

slots.contributes_to_pathogenic_mechanism = Slot(uri=ALSKG.contributes_to_pathogenic_mechanism, name="contributes_to_pathogenic_mechanism", curie=ALSKG.curie('contributes_to_pathogenic_mechanism'),
                   model_uri=ALSKG.contributes_to_pathogenic_mechanism, domain=None, range=Optional[Union[Union[str, PathogenicMechanismId], list[Union[str, PathogenicMechanismId]]]])

slots.has_mechanism_category = Slot(uri=ALSKG.has_mechanism_category, name="has_mechanism_category", curie=ALSKG.curie('has_mechanism_category'),
                   model_uri=ALSKG.has_mechanism_category, domain=None, range=Optional[Union[str, "PathogenicMechanismEnum"]])

slots.involves_biological_process = Slot(uri=RO['0000056'], name="involves_biological_process", curie=RO.curie('0000056'),
                   model_uri=ALSKG.involves_biological_process, domain=None, range=Optional[Union[Union[str, BiologicalProcessId], list[Union[str, BiologicalProcessId]]]])

slots.involves_molecular_function = Slot(uri=ALSKG.involves_molecular_function, name="involves_molecular_function", curie=ALSKG.curie('involves_molecular_function'),
                   model_uri=ALSKG.involves_molecular_function, domain=None, range=Optional[Union[Union[str, MolecularFunctionId], list[Union[str, MolecularFunctionId]]]])

slots.involves_pathway = Slot(uri=ALSKG.involves_pathway, name="involves_pathway", curie=ALSKG.curie('involves_pathway'),
                   model_uri=ALSKG.involves_pathway, domain=None, range=Optional[Union[Union[str, PathwayId], list[Union[str, PathwayId]]]])

slots.has_molecular_event = Slot(uri=ALSKG.has_molecular_event, name="has_molecular_event", curie=ALSKG.curie('has_molecular_event'),
                   model_uri=ALSKG.has_molecular_event, domain=None, range=Optional[Union[Union[str, MolecularEventId], list[Union[str, MolecularEventId]]]])

slots.forms_protein_aggregate = Slot(uri=ALSKG.forms_protein_aggregate, name="forms_protein_aggregate", curie=ALSKG.curie('forms_protein_aggregate'),
                   model_uri=ALSKG.forms_protein_aggregate, domain=None, range=Optional[Union[Union[str, ProteinAggregateId], list[Union[str, ProteinAggregateId]]]])

slots.has_phenotype = Slot(uri=RO['0002200'], name="has_phenotype", curie=RO.curie('0002200'),
                   model_uri=ALSKG.has_phenotype, domain=None, range=Optional[Union[Union[str, PhenotypeId], list[Union[str, PhenotypeId]]]])

slots.has_phenotype_observation = Slot(uri=ALSKG.has_phenotype_observation, name="has_phenotype_observation", curie=ALSKG.curie('has_phenotype_observation'),
                   model_uri=ALSKG.has_phenotype_observation, domain=None, range=Optional[Union[Union[str, PhenotypeObservationId], list[Union[str, PhenotypeObservationId]]]])

slots.observes_phenotype = Slot(uri=ALSKG.observes_phenotype, name="observes_phenotype", curie=ALSKG.curie('observes_phenotype'),
                   model_uri=ALSKG.observes_phenotype, domain=None, range=Optional[Union[str, PhenotypeId]])

slots.has_frequency = Slot(uri=ALSKG.has_frequency, name="has_frequency", curie=ALSKG.curie('has_frequency'),
                   model_uri=ALSKG.has_frequency, domain=None, range=Optional[str])

slots.has_onset_stage = Slot(uri=ALSKG.has_onset_stage, name="has_onset_stage", curie=ALSKG.curie('has_onset_stage'),
                   model_uri=ALSKG.has_onset_stage, domain=None, range=Optional[Union[str, DiseaseStageId]])

slots.has_progression_pattern = Slot(uri=ALSKG.has_progression_pattern, name="has_progression_pattern", curie=ALSKG.curie('has_progression_pattern'),
                   model_uri=ALSKG.has_progression_pattern, domain=None, range=Optional[Union[str, ProgressionPatternId]])

slots.measures_gene_expression_of = Slot(uri=ALSKG.measures_gene_expression_of, name="measures_gene_expression_of", curie=ALSKG.curie('measures_gene_expression_of'),
                   model_uri=ALSKG.measures_gene_expression_of, domain=None, range=Optional[Union[str, GeneId]])

slots.has_expression_result = Slot(uri=ALSKG.has_expression_result, name="has_expression_result", curie=ALSKG.curie('has_expression_result'),
                   model_uri=ALSKG.has_expression_result, domain=None, range=Optional[Union[Union[str, DifferentialExpressionStatementId], list[Union[str, DifferentialExpressionStatementId]]]])

slots.has_expression_direction = Slot(uri=ALSKG.has_expression_direction, name="has_expression_direction", curie=ALSKG.curie('has_expression_direction'),
                   model_uri=ALSKG.has_expression_direction, domain=None, range=Optional[Union[str, "ExpressionDirectionEnum"]])

slots.has_log_fold_change = Slot(uri=ALSKG.has_log_fold_change, name="has_log_fold_change", curie=ALSKG.curie('has_log_fold_change'),
                   model_uri=ALSKG.has_log_fold_change, domain=None, range=Optional[float])

slots.has_p_value = Slot(uri=ALSKG.has_p_value, name="has_p_value", curie=ALSKG.curie('has_p_value'),
                   model_uri=ALSKG.has_p_value, domain=None, range=Optional[float])

slots.has_adjusted_p_value = Slot(uri=ALSKG.has_adjusted_p_value, name="has_adjusted_p_value", curie=ALSKG.curie('has_adjusted_p_value'),
                   model_uri=ALSKG.has_adjusted_p_value, domain=None, range=Optional[float])

slots.has_false_discovery_rate = Slot(uri=ALSKG.has_false_discovery_rate, name="has_false_discovery_rate", curie=ALSKG.curie('has_false_discovery_rate'),
                   model_uri=ALSKG.has_false_discovery_rate, domain=None, range=Optional[float])

slots.compares_against = Slot(uri=ALSKG.compares_against, name="compares_against", curie=ALSKG.curie('compares_against'),
                   model_uri=ALSKG.compares_against, domain=None, range=Optional[Union[str, ComparatorGroupId]])

slots.measured_in_sample = Slot(uri=ALSKG.measured_in_sample, name="measured_in_sample", curie=ALSKG.curie('measured_in_sample'),
                   model_uri=ALSKG.measured_in_sample, domain=None, range=Optional[Union[str, SampleId]])

slots.measured_by_assay = Slot(uri=OBI['0000293'], name="measured_by_assay", curie=OBI.curie('0000293'),
                   model_uri=ALSKG.measured_by_assay, domain=None, range=Optional[Union[str, AssayId]])

slots.derives_from_dataset = Slot(uri=PROV.wasDerivedFrom, name="derives_from_dataset", curie=PROV.curie('wasDerivedFrom'),
                   model_uri=ALSKG.derives_from_dataset, domain=None, range=Optional[Union[str, DatasetId]])

slots.has_sample_type = Slot(uri=ALSKG.has_sample_type, name="has_sample_type", curie=ALSKG.curie('has_sample_type'),
                   model_uri=ALSKG.has_sample_type, domain=None, range=Optional[str])

slots.is_sample_from = Slot(uri=ALSKG.is_sample_from, name="is_sample_from", curie=ALSKG.curie('is_sample_from'),
                   model_uri=ALSKG.is_sample_from, domain=None, range=Optional[Union[str, CohortId]])

slots.is_sampled_from_anatomy = Slot(uri=RO['0001000'], name="is_sampled_from_anatomy", curie=RO.curie('0001000'),
                   model_uri=ALSKG.is_sampled_from_anatomy, domain=None, range=Optional[Union[str, AnatomyId]])

slots.is_sampled_from_cell_type = Slot(uri=ALSKG.is_sampled_from_cell_type, name="is_sampled_from_cell_type", curie=ALSKG.curie('is_sampled_from_cell_type'),
                   model_uri=ALSKG.is_sampled_from_cell_type, domain=None, range=Optional[Union[str, CellTypeId]])

slots.has_biomarker = Slot(uri=ALSKG.has_biomarker, name="has_biomarker", curie=ALSKG.curie('has_biomarker'),
                   model_uri=ALSKG.has_biomarker, domain=None, range=Optional[Union[Union[str, BiomarkerId], list[Union[str, BiomarkerId]]]])

slots.is_biomarker_for = Slot(uri=ALSKG.is_biomarker_for, name="is_biomarker_for", curie=ALSKG.curie('is_biomarker_for'),
                   model_uri=ALSKG.is_biomarker_for, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.measures_protein_abundance_of = Slot(uri=ALSKG.measures_protein_abundance_of, name="measures_protein_abundance_of", curie=ALSKG.curie('measures_protein_abundance_of'),
                   model_uri=ALSKG.measures_protein_abundance_of, domain=None, range=Optional[Union[str, ProteinId]])

slots.has_abundance_direction = Slot(uri=ALSKG.has_abundance_direction, name="has_abundance_direction", curie=ALSKG.curie('has_abundance_direction'),
                   model_uri=ALSKG.has_abundance_direction, domain=None, range=Optional[Union[str, "ExpressionDirectionEnum"]])

slots.treats_disease = Slot(uri=BIOLINK.treats, name="treats_disease", curie=BIOLINK.curie('treats'),
                   model_uri=ALSKG.treats_disease, domain=None, range=Optional[Union[Union[str, DiseaseId], list[Union[str, DiseaseId]]]])

slots.is_indicated_for_subtype = Slot(uri=ALSKG.is_indicated_for_subtype, name="is_indicated_for_subtype", curie=ALSKG.curie('is_indicated_for_subtype'),
                   model_uri=ALSKG.is_indicated_for_subtype, domain=None, range=Optional[Union[Union[str, ALSSubtypeId], list[Union[str, ALSSubtypeId]]]])

slots.targets_gene = Slot(uri=ALSKG.targets_gene, name="targets_gene", curie=ALSKG.curie('targets_gene'),
                   model_uri=ALSKG.targets_gene, domain=None, range=Optional[Union[Union[str, GeneId], list[Union[str, GeneId]]]])

slots.targets_protein = Slot(uri=ALSKG.targets_protein, name="targets_protein", curie=ALSKG.curie('targets_protein'),
                   model_uri=ALSKG.targets_protein, domain=None, range=Optional[Union[Union[str, ProteinId], list[Union[str, ProteinId]]]])

slots.has_drug_action_direction = Slot(uri=ALSKG.has_drug_action_direction, name="has_drug_action_direction", curie=ALSKG.curie('has_drug_action_direction'),
                   model_uri=ALSKG.has_drug_action_direction, domain=None, range=Optional[Union[str, "DrugActionDirectionEnum"]])

slots.modulates_pathogenic_mechanism = Slot(uri=ALSKG.modulates_pathogenic_mechanism, name="modulates_pathogenic_mechanism", curie=ALSKG.curie('modulates_pathogenic_mechanism'),
                   model_uri=ALSKG.modulates_pathogenic_mechanism, domain=None, range=Optional[Union[Union[str, PathogenicMechanismId], list[Union[str, PathogenicMechanismId]]]])

slots.tested_in_trial = Slot(uri=ALSKG.tested_in_trial, name="tested_in_trial", curie=ALSKG.curie('tested_in_trial'),
                   model_uri=ALSKG.tested_in_trial, domain=None, range=Optional[Union[Union[str, ClinicalTrialId], list[Union[str, ClinicalTrialId]]]])

slots.has_repurposing_status = Slot(uri=ALSKG.has_repurposing_status, name="has_repurposing_status", curie=ALSKG.curie('has_repurposing_status'),
                   model_uri=ALSKG.has_repurposing_status, domain=None, range=Optional[Union[str, "RepurposingStatusEnum"]])

slots.has_rationale = Slot(uri=ALSKG.has_rationale, name="has_rationale", curie=ALSKG.curie('has_rationale'),
                   model_uri=ALSKG.has_rationale, domain=None, range=Optional[str])

slots.has_dataset = Slot(uri=ALSKG.has_dataset, name="has_dataset", curie=ALSKG.curie('has_dataset'),
                   model_uri=ALSKG.has_dataset, domain=None, range=Optional[Union[Union[str, DatasetId], list[Union[str, DatasetId]]]])

slots.has_cohort = Slot(uri=ALSKG.has_cohort, name="has_cohort", curie=ALSKG.curie('has_cohort'),
                   model_uri=ALSKG.has_cohort, domain=None, range=Optional[Union[Union[str, CohortId], list[Union[str, CohortId]]]])

slots.has_sample = Slot(uri=ALSKG.has_sample, name="has_sample", curie=ALSKG.curie('has_sample'),
                   model_uri=ALSKG.has_sample, domain=None, range=Optional[Union[Union[str, SampleId], list[Union[str, SampleId]]]])

slots.has_assay = Slot(uri=OBI['0000295'], name="has_assay", curie=OBI.curie('0000295'),
                   model_uri=ALSKG.has_assay, domain=None, range=Optional[Union[Union[str, AssayId], list[Union[str, AssayId]]]])

slots.has_evidence_modality = Slot(uri=ALSKG.has_evidence_modality, name="has_evidence_modality", curie=ALSKG.curie('has_evidence_modality'),
                   model_uri=ALSKG.has_evidence_modality, domain=None, range=Optional[Union[str, "EvidenceModalityEnum"]])

slots.has_publication_identifier = Slot(uri=DCTERMS.identifier, name="has_publication_identifier", curie=DCTERMS.curie('identifier'),
                   model_uri=ALSKG.has_publication_identifier, domain=None, range=Optional[Union[str, list[str]]])

slots.has_title = Slot(uri=DCTERMS.title, name="has_title", curie=DCTERMS.curie('title'),
                   model_uri=ALSKG.has_title, domain=None, range=Optional[str])

slots.has_year = Slot(uri=DCTERMS.issued, name="has_year", curie=DCTERMS.curie('issued'),
                   model_uri=ALSKG.has_year, domain=None, range=Optional[int])

slots.has_url = Slot(uri=DCTERMS.source, name="has_url", curie=DCTERMS.curie('source'),
                   model_uri=ALSKG.has_url, domain=None, range=Optional[str])

slots.has_license = Slot(uri=DCTERMS.license, name="has_license", curie=DCTERMS.curie('license'),
                   model_uri=ALSKG.has_license, domain=None, range=Optional[str])

slots.has_species = Slot(uri=RO['0002162'], name="has_species", curie=RO.curie('0002162'),
                   model_uri=ALSKG.has_species, domain=None, range=Optional[str])

slots.has_sex = Slot(uri=ALSKG.has_sex, name="has_sex", curie=ALSKG.curie('has_sex'),
                   model_uri=ALSKG.has_sex, domain=None, range=Optional[Union[str, "SexEnum"]])

slots.has_case_count = Slot(uri=ALSKG.has_case_count, name="has_case_count", curie=ALSKG.curie('has_case_count'),
                   model_uri=ALSKG.has_case_count, domain=None, range=Optional[int])

slots.has_control_count = Slot(uri=ALSKG.has_control_count, name="has_control_count", curie=ALSKG.curie('has_control_count'),
                   model_uri=ALSKG.has_control_count, domain=None, range=Optional[int])

slots.has_model_system = Slot(uri=ALSKG.has_model_system, name="has_model_system", curie=ALSKG.curie('has_model_system'),
                   model_uri=ALSKG.has_model_system, domain=None, range=Optional[Union[Union[str, ModelSystemId], list[Union[str, ModelSystemId]]]])

slots.models_disease = Slot(uri=ALSKG.models_disease, name="models_disease", curie=ALSKG.curie('models_disease'),
                   model_uri=ALSKG.models_disease, domain=None, range=Optional[Union[str, DiseaseId]])

slots.models_subtype = Slot(uri=ALSKG.models_subtype, name="models_subtype", curie=ALSKG.curie('models_subtype'),
                   model_uri=ALSKG.models_subtype, domain=None, range=Optional[Union[str, ALSSubtypeId]])

slots.has_external_reference = Slot(uri=DCTERMS.references, name="has_external_reference", curie=DCTERMS.curie('references'),
                   model_uri=ALSKG.has_external_reference, domain=None, range=Optional[Union[Union[str, ExternalKnowledgeReferenceId], list[Union[str, ExternalKnowledgeReferenceId]]]])

slots.has_als_subtype = Slot(uri=ALSKG.has_subtype, name="has_als_subtype", curie=ALSKG.curie('has_subtype'),
                   model_uri=ALSKG.has_als_subtype, domain=None, range=Optional[Union[Union[str, ALSSubtypeId], list[Union[str, ALSSubtypeId]]]])

slots.has_observed_phenotype = Slot(uri=ALSKG.has_observed_phenotype, name="has_observed_phenotype", curie=ALSKG.curie('has_observed_phenotype'),
                   model_uri=ALSKG.has_observed_phenotype, domain=None, range=Optional[Union[str, PhenotypeId]])

slots.has_pathogenic_mechanism_category = Slot(uri=ALSKG.has_pathogenic_mechanism_category, name="has_pathogenic_mechanism_category", curie=ALSKG.curie('has_pathogenic_mechanism_category'),
                   model_uri=ALSKG.has_pathogenic_mechanism_category, domain=None, range=Optional[Union[str, "PathogenicMechanismEnum"]])

slots.has_variant_type = Slot(uri=SO['0001060'], name="has_variant_type", curie=SO.curie('0001060'),
                   model_uri=ALSKG.has_variant_type, domain=None, range=Optional[str])

slots.has_protein_component = Slot(uri=RO['0002180'], name="has_protein_component", curie=RO.curie('0002180'),
                   model_uri=ALSKG.has_protein_component, domain=None, range=Optional[Union[Union[str, ProteinId], list[Union[str, ProteinId]]]])

slots.has_disease_stage = Slot(uri=ALSKG.has_disease_stage, name="has_disease_stage", curie=ALSKG.curie('has_disease_stage'),
                   model_uri=ALSKG.has_disease_stage, domain=None, range=Optional[Union[str, DiseaseStageId]])

slots.biomarker_for_disease = Slot(uri=BIOLINK.biomarker_for, name="biomarker_for_disease", curie=BIOLINK.curie('biomarker_for'),
                   model_uri=ALSKG.biomarker_for_disease, domain=None, range=Optional[Union[Union[str, DiseaseId], list[Union[str, DiseaseId]]]])

slots.biomarker_for_subtype = Slot(uri=ALSKG.biomarker_for_subtype, name="biomarker_for_subtype", curie=ALSKG.curie('biomarker_for_subtype'),
                   model_uri=ALSKG.biomarker_for_subtype, domain=None, range=Optional[Union[Union[str, ALSSubtypeId], list[Union[str, ALSSubtypeId]]]])

slots.indicates_pathogenic_mechanism = Slot(uri=ALSKG.indicates_pathogenic_mechanism, name="indicates_pathogenic_mechanism", curie=ALSKG.curie('indicates_pathogenic_mechanism'),
                   model_uri=ALSKG.indicates_pathogenic_mechanism, domain=None, range=Optional[Union[Union[str, PathogenicMechanismId], list[Union[str, PathogenicMechanismId]]]])

slots.derived_from_anatomy = Slot(uri=RO['0001000'], name="derived_from_anatomy", curie=RO.curie('0001000'),
                   model_uri=ALSKG.derived_from_anatomy, domain=None, range=Optional[Union[str, AnatomyId]])

slots.has_cell_type = Slot(uri=ALSKG.has_cell_type, name="has_cell_type", curie=ALSKG.curie('has_cell_type'),
                   model_uri=ALSKG.has_cell_type, domain=None, range=Optional[Union[Union[str, CellTypeId], list[Union[str, CellTypeId]]]])

slots.has_genetic_perturbation = Slot(uri=ALSKG.has_genetic_perturbation, name="has_genetic_perturbation", curie=ALSKG.curie('has_genetic_perturbation'),
                   model_uri=ALSKG.has_genetic_perturbation, domain=None, range=Optional[Union[Union[str, NamedEntityId], list[Union[str, NamedEntityId]]]])

slots.tested_in_clinical_trial = Slot(uri=ALSKG.tested_in_clinical_trial, name="tested_in_clinical_trial", curie=ALSKG.curie('tested_in_clinical_trial'),
                   model_uri=ALSKG.tested_in_clinical_trial, domain=None, range=Optional[Union[Union[str, ClinicalTrialId], list[Union[str, ClinicalTrialId]]]])

slots.tests_intervention = Slot(uri=ALSKG.tests_intervention, name="tests_intervention", curie=ALSKG.curie('tests_intervention'),
                   model_uri=ALSKG.tests_intervention, domain=None, range=Optional[Union[Union[str, TherapeuticInterventionId], list[Union[str, TherapeuticInterventionId]]]])

slots.enrolls_subtype = Slot(uri=ALSKG.enrolls_subtype, name="enrolls_subtype", curie=ALSKG.curie('enrolls_subtype'),
                   model_uri=ALSKG.enrolls_subtype, domain=None, range=Optional[Union[Union[str, ALSSubtypeId], list[Union[str, ALSSubtypeId]]]])

slots.has_outcome_measure = Slot(uri=ALSKG.has_outcome_measure, name="has_outcome_measure", curie=ALSKG.curie('has_outcome_measure'),
                   model_uri=ALSKG.has_outcome_measure, domain=None, range=Optional[Union[Union[str, NamedEntityId], list[Union[str, NamedEntityId]]]])

slots.prioritizes_drug = Slot(uri=ALSKG.prioritizes_drug, name="prioritizes_drug", curie=ALSKG.curie('prioritizes_drug'),
                   model_uri=ALSKG.prioritizes_drug, domain=None, range=Optional[Union[str, DrugId]])

slots.has_evidence_basis = Slot(uri=ALSKG.has_evidence_basis, name="has_evidence_basis", curie=ALSKG.curie('has_evidence_basis'),
                   model_uri=ALSKG.has_evidence_basis, domain=None, range=Optional[Union[Union[str, EvidenceStatementId], list[Union[str, EvidenceStatementId]]]])

slots.disease_has_als_subtype = Slot(uri=ALSKG.disease_has_als_subtype, name="disease_has_als_subtype", curie=ALSKG.curie('disease_has_als_subtype'),
                   model_uri=ALSKG.disease_has_als_subtype, domain=None, range=Optional[Union[str, ALSSubtypeId]])

slots.als_subtype_is_subtype_of_disease = Slot(uri=ALSKG.als_subtype_is_subtype_of_disease, name="als_subtype_is_subtype_of_disease", curie=ALSKG.curie('als_subtype_is_subtype_of_disease'),
                   model_uri=ALSKG.als_subtype_is_subtype_of_disease, domain=None, range=Optional[Union[str, DiseaseId]])

slots.als_subtype_has_subtype_scheme = Slot(uri=ALSKG.als_subtype_has_subtype_scheme, name="als_subtype_has_subtype_scheme", curie=ALSKG.curie('als_subtype_has_subtype_scheme'),
                   model_uri=ALSKG.als_subtype_has_subtype_scheme, domain=None, range=Optional[Union[str, SubtypeSchemeId]])

slots.als_subtype_has_subtype_criterion = Slot(uri=ALSKG.als_subtype_has_subtype_criterion, name="als_subtype_has_subtype_criterion", curie=ALSKG.curie('als_subtype_has_subtype_criterion'),
                   model_uri=ALSKG.als_subtype_has_subtype_criterion, domain=None, range=Optional[Union[str, SubtypeCriterionId]])

slots.als_subtype_defined_by_gene = Slot(uri=ALSKG.als_subtype_defined_by_gene, name="als_subtype_defined_by_gene", curie=ALSKG.curie('als_subtype_defined_by_gene'),
                   model_uri=ALSKG.als_subtype_defined_by_gene, domain=None, range=Optional[Union[str, GeneId]])

slots.als_subtype_defined_by_variant = Slot(uri=ALSKG.als_subtype_defined_by_variant, name="als_subtype_defined_by_variant", curie=ALSKG.curie('als_subtype_defined_by_variant'),
                   model_uri=ALSKG.als_subtype_defined_by_variant, domain=None, range=Optional[Union[str, SequenceVariantId]])

slots.als_subtype_has_pathogenic_mechanism = Slot(uri=ALSKG.als_subtype_has_pathogenic_mechanism, name="als_subtype_has_pathogenic_mechanism", curie=ALSKG.curie('als_subtype_has_pathogenic_mechanism'),
                   model_uri=ALSKG.als_subtype_has_pathogenic_mechanism, domain=None, range=Optional[Union[str, PathogenicMechanismId]])

slots.als_subtype_affects_anatomy = Slot(uri=ALSKG.als_subtype_affects_anatomy, name="als_subtype_affects_anatomy", curie=ALSKG.curie('als_subtype_affects_anatomy'),
                   model_uri=ALSKG.als_subtype_affects_anatomy, domain=None, range=Optional[Union[str, AnatomyId]])

slots.als_subtype_involves_cell_type = Slot(uri=ALSKG.als_subtype_involves_cell_type, name="als_subtype_involves_cell_type", curie=ALSKG.curie('als_subtype_involves_cell_type'),
                   model_uri=ALSKG.als_subtype_involves_cell_type, domain=None, range=Optional[Union[str, CellTypeId]])

slots.als_subtype_has_phenotype_observation = Slot(uri=ALSKG.als_subtype_has_phenotype_observation, name="als_subtype_has_phenotype_observation", curie=ALSKG.curie('als_subtype_has_phenotype_observation'),
                   model_uri=ALSKG.als_subtype_has_phenotype_observation, domain=None, range=Optional[Union[str, PhenotypeObservationId]])

slots.gene_has_variant = Slot(uri=ALSKG.gene_has_variant, name="gene_has_variant", curie=ALSKG.curie('gene_has_variant'),
                   model_uri=ALSKG.gene_has_variant, domain=None, range=Optional[Union[str, SequenceVariantId]])

slots.variant_affects_gene = Slot(uri=ALSKG.variant_affects_gene, name="variant_affects_gene", curie=ALSKG.curie('variant_affects_gene'),
                   model_uri=ALSKG.variant_affects_gene, domain=None, range=Optional[Union[str, GeneId]])

slots.variant_alters_protein = Slot(uri=ALSKG.variant_alters_protein, name="variant_alters_protein", curie=ALSKG.curie('variant_alters_protein'),
                   model_uri=ALSKG.variant_alters_protein, domain=None, range=Optional[Union[str, ProteinId]])

slots.gene_contributes_to_pathogenic_mechanism = Slot(uri=ALSKG.gene_contributes_to_pathogenic_mechanism, name="gene_contributes_to_pathogenic_mechanism", curie=ALSKG.curie('gene_contributes_to_pathogenic_mechanism'),
                   model_uri=ALSKG.gene_contributes_to_pathogenic_mechanism, domain=None, range=Optional[Union[str, PathogenicMechanismId]])

slots.protein_contributes_to_pathogenic_mechanism = Slot(uri=ALSKG.protein_contributes_to_pathogenic_mechanism, name="protein_contributes_to_pathogenic_mechanism", curie=ALSKG.curie('protein_contributes_to_pathogenic_mechanism'),
                   model_uri=ALSKG.protein_contributes_to_pathogenic_mechanism, domain=None, range=Optional[Union[str, PathogenicMechanismId]])

slots.molecular_event_contributes_to_pathogenic_mechanism = Slot(uri=ALSKG.molecular_event_contributes_to_pathogenic_mechanism, name="molecular_event_contributes_to_pathogenic_mechanism", curie=ALSKG.curie('molecular_event_contributes_to_pathogenic_mechanism'),
                   model_uri=ALSKG.molecular_event_contributes_to_pathogenic_mechanism, domain=None, range=Optional[Union[str, PathogenicMechanismId]])

slots.pathogenic_mechanism_occurs_in_cell_type = Slot(uri=ALSKG.pathogenic_mechanism_occurs_in_cell_type, name="pathogenic_mechanism_occurs_in_cell_type", curie=ALSKG.curie('pathogenic_mechanism_occurs_in_cell_type'),
                   model_uri=ALSKG.pathogenic_mechanism_occurs_in_cell_type, domain=None, range=Optional[Union[str, CellTypeId]])

slots.pathogenic_mechanism_occurs_in_anatomy = Slot(uri=ALSKG.pathogenic_mechanism_occurs_in_anatomy, name="pathogenic_mechanism_occurs_in_anatomy", curie=ALSKG.curie('pathogenic_mechanism_occurs_in_anatomy'),
                   model_uri=ALSKG.pathogenic_mechanism_occurs_in_anatomy, domain=None, range=Optional[Union[str, AnatomyId]])

slots.differential_expression_measures_gene = Slot(uri=ALSKG.differential_expression_measures_gene, name="differential_expression_measures_gene", curie=ALSKG.curie('differential_expression_measures_gene'),
                   model_uri=ALSKG.differential_expression_measures_gene, domain=None, range=Optional[Union[str, GeneId]])

slots.differential_expression_occurs_in_subtype = Slot(uri=ALSKG.differential_expression_occurs_in_subtype, name="differential_expression_occurs_in_subtype", curie=ALSKG.curie('differential_expression_occurs_in_subtype'),
                   model_uri=ALSKG.differential_expression_occurs_in_subtype, domain=None, range=Optional[Union[str, ALSSubtypeId]])

slots.differential_expression_occurs_in_anatomy = Slot(uri=ALSKG.differential_expression_occurs_in_anatomy, name="differential_expression_occurs_in_anatomy", curie=ALSKG.curie('differential_expression_occurs_in_anatomy'),
                   model_uri=ALSKG.differential_expression_occurs_in_anatomy, domain=None, range=Optional[Union[str, AnatomyId]])

slots.differential_expression_occurs_in_cell_type = Slot(uri=ALSKG.differential_expression_occurs_in_cell_type, name="differential_expression_occurs_in_cell_type", curie=ALSKG.curie('differential_expression_occurs_in_cell_type'),
                   model_uri=ALSKG.differential_expression_occurs_in_cell_type, domain=None, range=Optional[Union[str, CellTypeId]])

slots.differential_expression_measured_by_assay = Slot(uri=ALSKG.differential_expression_measured_by_assay, name="differential_expression_measured_by_assay", curie=ALSKG.curie('differential_expression_measured_by_assay'),
                   model_uri=ALSKG.differential_expression_measured_by_assay, domain=None, range=Optional[Union[str, AssayId]])

slots.differential_expression_derives_from_dataset = Slot(uri=ALSKG.differential_expression_derives_from_dataset, name="differential_expression_derives_from_dataset", curie=ALSKG.curie('differential_expression_derives_from_dataset'),
                   model_uri=ALSKG.differential_expression_derives_from_dataset, domain=None, range=Optional[Union[str, DatasetId]])

slots.evidence_statement_supported_by_evidence = Slot(uri=ALSKG.evidence_statement_supported_by_evidence, name="evidence_statement_supported_by_evidence", curie=ALSKG.curie('evidence_statement_supported_by_evidence'),
                   model_uri=ALSKG.evidence_statement_supported_by_evidence, domain=None, range=Optional[Union[str, EvidenceRecordId]])

slots.evidence_statement_derives_from_dataset = Slot(uri=ALSKG.evidence_statement_derives_from_dataset, name="evidence_statement_derives_from_dataset", curie=ALSKG.curie('evidence_statement_derives_from_dataset'),
                   model_uri=ALSKG.evidence_statement_derives_from_dataset, domain=None, range=Optional[Union[str, DatasetId]])

slots.phenotype_observation_has_observed_phenotype = Slot(uri=ALSKG.phenotype_observation_has_observed_phenotype, name="phenotype_observation_has_observed_phenotype", curie=ALSKG.curie('phenotype_observation_has_observed_phenotype'),
                   model_uri=ALSKG.phenotype_observation_has_observed_phenotype, domain=None, range=Optional[Union[str, PhenotypeId]])

slots.phenotype_observation_occurs_in_subtype = Slot(uri=ALSKG.phenotype_observation_occurs_in_subtype, name="phenotype_observation_occurs_in_subtype", curie=ALSKG.curie('phenotype_observation_occurs_in_subtype'),
                   model_uri=ALSKG.phenotype_observation_occurs_in_subtype, domain=None, range=Optional[Union[str, ALSSubtypeId]])

slots.biomarker_indicates_pathogenic_mechanism = Slot(uri=ALSKG.biomarker_indicates_pathogenic_mechanism, name="biomarker_indicates_pathogenic_mechanism", curie=ALSKG.curie('biomarker_indicates_pathogenic_mechanism'),
                   model_uri=ALSKG.biomarker_indicates_pathogenic_mechanism, domain=None, range=Optional[Union[str, PathogenicMechanismId]])

slots.drug_repurposing_hypothesis_prioritizes_drug = Slot(uri=ALSKG.drug_repurposing_hypothesis_prioritizes_drug, name="drug_repurposing_hypothesis_prioritizes_drug", curie=ALSKG.curie('drug_repurposing_hypothesis_prioritizes_drug'),
                   model_uri=ALSKG.drug_repurposing_hypothesis_prioritizes_drug, domain=None, range=Optional[Union[str, DrugId]])

slots.drug_repurposing_hypothesis_targets_gene = Slot(uri=ALSKG.drug_repurposing_hypothesis_targets_gene, name="drug_repurposing_hypothesis_targets_gene", curie=ALSKG.curie('drug_repurposing_hypothesis_targets_gene'),
                   model_uri=ALSKG.drug_repurposing_hypothesis_targets_gene, domain=None, range=Optional[Union[str, GeneId]])

slots.drug_repurposing_hypothesis_modulates_pathogenic_mechanism = Slot(uri=ALSKG.drug_repurposing_hypothesis_modulates_pathogenic_mechanism, name="drug_repurposing_hypothesis_modulates_pathogenic_mechanism", curie=ALSKG.curie('drug_repurposing_hypothesis_modulates_pathogenic_mechanism'),
                   model_uri=ALSKG.drug_repurposing_hypothesis_modulates_pathogenic_mechanism, domain=None, range=Optional[Union[str, PathogenicMechanismId]])

slots.therapeutic_intervention_tested_in_clinical_trial = Slot(uri=ALSKG.therapeutic_intervention_tested_in_clinical_trial, name="therapeutic_intervention_tested_in_clinical_trial", curie=ALSKG.curie('therapeutic_intervention_tested_in_clinical_trial'),
                   model_uri=ALSKG.therapeutic_intervention_tested_in_clinical_trial, domain=None, range=Optional[Union[str, ClinicalTrialId]])

slots.clinical_trial_enrolls_subtype = Slot(uri=ALSKG.clinical_trial_enrolls_subtype, name="clinical_trial_enrolls_subtype", curie=ALSKG.curie('clinical_trial_enrolls_subtype'),
                   model_uri=ALSKG.clinical_trial_enrolls_subtype, domain=None, range=Optional[Union[str, ALSSubtypeId]])

slots.model_system_models_subtype = Slot(uri=ALSKG.model_system_models_subtype, name="model_system_models_subtype", curie=ALSKG.curie('model_system_models_subtype'),
                   model_uri=ALSKG.model_system_models_subtype, domain=None, range=Optional[Union[str, ALSSubtypeId]])

slots.disease__therapeutic_areas = Slot(uri=ALSKG.therapeutic_areas, name="disease__therapeutic_areas", curie=ALSKG.curie('therapeutic_areas'),
                   model_uri=ALSKG.disease__therapeutic_areas, domain=None, range=Optional[Union[str, list[str]]])

slots.drug__trade_names = Slot(uri=ALSKG.trade_names, name="drug__trade_names", curie=ALSKG.curie('trade_names'),
                   model_uri=ALSKG.drug__trade_names, domain=None, range=Optional[Union[str, list[str]]])

slots.drug__accession_numbers = Slot(uri=ALSKG.accession_numbers, name="drug__accession_numbers", curie=ALSKG.curie('accession_numbers'),
                   model_uri=ALSKG.drug__accession_numbers, domain=None, range=Optional[Union[str, list[str]]])

slots.drug__inchi_key = Slot(uri=ALSKG.inchi_key, name="drug__inchi_key", curie=ALSKG.curie('inchi_key'),
                   model_uri=ALSKG.drug__inchi_key, domain=None, range=Optional[str])

slots.drug__cd_formula = Slot(uri=ALSKG.cd_formula, name="drug__cd_formula", curie=ALSKG.curie('cd_formula'),
                   model_uri=ALSKG.drug__cd_formula, domain=None, range=Optional[str])

slots.drug__is_approved = Slot(uri=ALSKG.is_approved, name="drug__is_approved", curie=ALSKG.curie('is_approved'),
                   model_uri=ALSKG.drug__is_approved, domain=None, range=Optional[Union[bool, Bool]])

slots.drug__has_been_withdrawn = Slot(uri=ALSKG.has_been_withdrawn, name="drug__has_been_withdrawn", curie=ALSKG.curie('has_been_withdrawn'),
                   model_uri=ALSKG.drug__has_been_withdrawn, domain=None, range=Optional[Union[bool, Bool]])

slots.drug__black_box_warning = Slot(uri=ALSKG.black_box_warning, name="drug__black_box_warning", curie=ALSKG.curie('black_box_warning'),
                   model_uri=ALSKG.drug__black_box_warning, domain=None, range=Optional[Union[bool, Bool]])

slots.drug__year_of_first_approval = Slot(uri=ALSKG.year_of_first_approval, name="drug__year_of_first_approval", curie=ALSKG.curie('year_of_first_approval'),
                   model_uri=ALSKG.drug__year_of_first_approval, domain=None, range=Optional[int])

slots.drug__maximum_clinical_trial_phase = Slot(uri=ALSKG.maximum_clinical_trial_phase, name="drug__maximum_clinical_trial_phase", curie=ALSKG.curie('maximum_clinical_trial_phase'),
                   model_uri=ALSKG.drug__maximum_clinical_trial_phase, domain=None, range=Optional[float])

slots.drug__status = Slot(uri=ALSKG.status, name="drug__status", curie=ALSKG.curie('status'),
                   model_uri=ALSKG.drug__status, domain=None, range=Optional[str])

slots.drug__chemical_abstracts_service_number = Slot(uri=ALSKG.chemical_abstracts_service_number, name="drug__chemical_abstracts_service_number", curie=ALSKG.curie('chemical_abstracts_service_number'),
                   model_uri=ALSKG.drug__chemical_abstracts_service_number, domain=None, range=Optional[str])

slots.drug__unique_ingredient_identifier = Slot(uri=ALSKG.unique_ingredient_identifier, name="drug__unique_ingredient_identifier", curie=ALSKG.curie('unique_ingredient_identifier'),
                   model_uri=ALSKG.drug__unique_ingredient_identifier, domain=None, range=Optional[str])

slots.exposure__source_categories = Slot(uri=ALSKG.source_categories, name="exposure__source_categories", curie=ALSKG.curie('source_categories'),
                   model_uri=ALSKG.exposure__source_categories, domain=None, range=Optional[Union[str, list[str]]])

slots.exposure__source_details = Slot(uri=ALSKG.source_details, name="exposure__source_details", curie=ALSKG.curie('source_details'),
                   model_uri=ALSKG.exposure__source_details, domain=None, range=Optional[str])

slots.gene__biotype = Slot(uri=ALSKG.biotype, name="gene__biotype", curie=ALSKG.curie('biotype'),
                   model_uri=ALSKG.gene__biotype, domain=None, range=Optional[Union[str, "GeneBiotypeEnum"]])

slots.pathway__species = Slot(uri=ALSKG.species, name="pathway__species", curie=ALSKG.curie('species'),
                   model_uri=ALSKG.pathway__species, domain=None, range=Optional[str])

slots.molecularSubtype__full_name = Slot(uri=ALSKG.full_name, name="molecularSubtype__full_name", curie=ALSKG.curie('full_name'),
                   model_uri=ALSKG.molecularSubtype__full_name, domain=None, range=Optional[str])

slots.molecularSubtype__defining_mechanism = Slot(uri=ALSKG.defining_mechanism, name="molecularSubtype__defining_mechanism", curie=ALSKG.curie('defining_mechanism'),
                   model_uri=ALSKG.molecularSubtype__defining_mechanism, domain=None, range=Optional[str])

slots.molecularSubtype__key_pathways = Slot(uri=ALSKG.key_pathways, name="molecularSubtype__key_pathways", curie=ALSKG.curie('key_pathways'),
                   model_uri=ALSKG.molecularSubtype__key_pathways, domain=None, range=Optional[Union[str, list[str]]])

slots.molecularSubtype__classification_basis = Slot(uri=ALSKG.classification_basis, name="molecularSubtype__classification_basis", curie=ALSKG.curie('classification_basis'),
                   model_uri=ALSKG.molecularSubtype__classification_basis, domain=None, range=Optional[Union[str, "MolecularSubtypeClassificationBasisEnum"]])

slots.molecularSubtype__tissue_origin = Slot(uri=ALSKG.tissue_origin, name="molecularSubtype__tissue_origin", curie=ALSKG.curie('tissue_origin'),
                   model_uri=ALSKG.molecularSubtype__tissue_origin, domain=None, range=Optional[Union[str, list[str]]])

slots.molecularSubtype__prevalence_pct = Slot(uri=ALSKG.prevalence_pct, name="molecularSubtype__prevalence_pct", curie=ALSKG.curie('prevalence_pct'),
                   model_uri=ALSKG.molecularSubtype__prevalence_pct, domain=None, range=Optional[float])

slots.molecularSubtype__survival_months_median = Slot(uri=ALSKG.survival_months_median, name="molecularSubtype__survival_months_median", curie=ALSKG.curie('survival_months_median'),
                   model_uri=ALSKG.molecularSubtype__survival_months_median, domain=None, range=Optional[float])

slots.molecularSubtype__onset_age_mean = Slot(uri=ALSKG.onset_age_mean, name="molecularSubtype__onset_age_mean", curie=ALSKG.curie('onset_age_mean'),
                   model_uri=ALSKG.molecularSubtype__onset_age_mean, domain=None, range=Optional[float])

slots.molecularSubtype__prognosis_note = Slot(uri=ALSKG.prognosis_note, name="molecularSubtype__prognosis_note", curie=ALSKG.curie('prognosis_note'),
                   model_uri=ALSKG.molecularSubtype__prognosis_note, domain=None, range=Optional[str])

slots.molecularSubtype__cohort = Slot(uri=ALSKG.cohort, name="molecularSubtype__cohort", curie=ALSKG.curie('cohort'),
                   model_uri=ALSKG.molecularSubtype__cohort, domain=None, range=Optional[str])

slots.molecularSubtype__pubmed_id = Slot(uri=ALSKG.pubmed_id, name="molecularSubtype__pubmed_id", curie=ALSKG.curie('pubmed_id'),
                   model_uri=ALSKG.molecularSubtype__pubmed_id, domain=None, range=Optional[str])

slots.molecularSubtype__label_color = Slot(uri=ALSKG.label_color, name="molecularSubtype__label_color", curie=ALSKG.curie('label_color'),
                   model_uri=ALSKG.molecularSubtype__label_color, domain=None, range=Optional[str])

slots.anatomyGeneExpressionRelationship__expression_rank = Slot(uri=ALSKG.expression_rank, name="anatomyGeneExpressionRelationship__expression_rank", curie=ALSKG.curie('expression_rank'),
                   model_uri=ALSKG.anatomyGeneExpressionRelationship__expression_rank, domain=None, range=Optional[int])

slots.anatomyGeneExpressionRelationship__call_quality = Slot(uri=ALSKG.call_quality, name="anatomyGeneExpressionRelationship__call_quality", curie=ALSKG.curie('call_quality'),
                   model_uri=ALSKG.anatomyGeneExpressionRelationship__call_quality, domain=None, range=Optional[Union[str, "ExpressionCallQualityEnum"]])

slots.diseasePhenotypeRelationship__aspect = Slot(uri=ALSKG.aspect, name="diseasePhenotypeRelationship__aspect", curie=ALSKG.curie('aspect'),
                   model_uri=ALSKG.diseasePhenotypeRelationship__aspect, domain=None, range=Optional[Union[str, list[str]]])

slots.diseasePhenotypeRelationship__evidence_type = Slot(uri=ALSKG.evidence_type, name="diseasePhenotypeRelationship__evidence_type", curie=ALSKG.curie('evidence_type'),
                   model_uri=ALSKG.diseasePhenotypeRelationship__evidence_type, domain=None, range=Optional[Union[str, list[str]]])

slots.diseasePhenotypeRelationship__frequency = Slot(uri=ALSKG.frequency, name="diseasePhenotypeRelationship__frequency", curie=ALSKG.curie('frequency'),
                   model_uri=ALSKG.diseasePhenotypeRelationship__frequency, domain=None, range=Optional[Union[str, list[str]]])

slots.diseasePhenotypeRelationship__onset = Slot(uri=ALSKG.onset, name="diseasePhenotypeRelationship__onset", curie=ALSKG.curie('onset'),
                   model_uri=ALSKG.diseasePhenotypeRelationship__onset, domain=None, range=Optional[Union[str, list[str]]])

slots.diseasePhenotypeRelationship__modifiers = Slot(uri=ALSKG.modifiers, name="diseasePhenotypeRelationship__modifiers", curie=ALSKG.curie('modifiers'),
                   model_uri=ALSKG.diseasePhenotypeRelationship__modifiers, domain=None, range=Optional[Union[str, list[str]]])

slots.diseasePhenotypeRelationship__sexes = Slot(uri=ALSKG.sexes, name="diseasePhenotypeRelationship__sexes", curie=ALSKG.curie('sexes'),
                   model_uri=ALSKG.diseasePhenotypeRelationship__sexes, domain=None, range=Optional[Union[str, list[str]]])

slots.diseasePhenotypeRelationship__qualifier_not = Slot(uri=ALSKG.qualifier_not, name="diseasePhenotypeRelationship__qualifier_not", curie=ALSKG.curie('qualifier_not'),
                   model_uri=ALSKG.diseasePhenotypeRelationship__qualifier_not, domain=None, range=Optional[Union[bool, Bool]])

slots.diseasePhenotypeRelationship__bio_curation = Slot(uri=ALSKG.bio_curation, name="diseasePhenotypeRelationship__bio_curation", curie=ALSKG.curie('bio_curation'),
                   model_uri=ALSKG.diseasePhenotypeRelationship__bio_curation, domain=None, range=Optional[Union[str, list[str]]])

slots.diseasePhenotypeRelationship__references = Slot(uri=ALSKG.references, name="diseasePhenotypeRelationship__references", curie=ALSKG.curie('references'),
                   model_uri=ALSKG.diseasePhenotypeRelationship__references, domain=None, range=Optional[Union[str, list[str]]])

slots.drugDrugRelationship__interaction_description = Slot(uri=ALSKG.interaction_description, name="drugDrugRelationship__interaction_description", curie=ALSKG.curie('interaction_description'),
                   model_uri=ALSKG.drugDrugRelationship__interaction_description, domain=None, range=Optional[str])

slots.drugGeneRelationship__mechanisms_of_action = Slot(uri=ALSKG.mechanisms_of_action, name="drugGeneRelationship__mechanisms_of_action", curie=ALSKG.curie('mechanisms_of_action'),
                   model_uri=ALSKG.drugGeneRelationship__mechanisms_of_action, domain=None, range=Optional[Union[str, list[str]]])

slots.drugGeneRelationship__source_urls = Slot(uri=ALSKG.source_urls, name="drugGeneRelationship__source_urls", curie=ALSKG.curie('source_urls'),
                   model_uri=ALSKG.drugGeneRelationship__source_urls, domain=None, range=Optional[Union[str, list[str]]])

slots.sources__direct = Slot(uri=ALSKG.direct, name="sources__direct", curie=ALSKG.curie('direct'),
                   model_uri=ALSKG.sources__direct, domain=None, range=Optional[Union[str, list[str]]])

slots.sources__indirect = Slot(uri=ALSKG.indirect, name="sources__indirect", curie=ALSKG.curie('indirect'),
                   model_uri=ALSKG.sources__indirect, domain=None, range=Optional[Union[str, list[str]]])

slots.ontologyMetadata__title = Slot(uri=ALSKG.title, name="ontologyMetadata__title", curie=ALSKG.curie('title'),
                   model_uri=ALSKG.ontologyMetadata__title, domain=None, range=Optional[str])

slots.ontologyMetadata__description = Slot(uri=ALSKG.description, name="ontologyMetadata__description", curie=ALSKG.curie('description'),
                   model_uri=ALSKG.ontologyMetadata__description, domain=None, range=Optional[str])

slots.ontologyMetadata__license = Slot(uri=ALSKG.license, name="ontologyMetadata__license", curie=ALSKG.curie('license'),
                   model_uri=ALSKG.ontologyMetadata__license, domain=None, range=Optional[str])

slots.ontologyMetadata__version = Slot(uri=ALSKG.version, name="ontologyMetadata__version", curie=ALSKG.curie('version'),
                   model_uri=ALSKG.ontologyMetadata__version, domain=None, range=Optional[str])

slots.geneExpressionContext__gene = Slot(uri=RO['0002206'], name="geneExpressionContext__gene", curie=RO.curie('0002206'),
                   model_uri=ALSKG.geneExpressionContext__gene, domain=None, range=Union[str, GeneId])

slots.geneExpressionContext__molecular_subtype = Slot(uri=OKG.in_molecular_subtype, name="geneExpressionContext__molecular_subtype", curie=OKG.curie('in_molecular_subtype'),
                   model_uri=ALSKG.geneExpressionContext__molecular_subtype, domain=None, range=Union[str, MolecularSubtypeId])

slots.geneExpressionContext__anatomy = Slot(uri=OKG.in_anatomy, name="geneExpressionContext__anatomy", curie=OKG.curie('in_anatomy'),
                   model_uri=ALSKG.geneExpressionContext__anatomy, domain=None, range=Optional[Union[str, AnatomyId]])

slots.geneExpressionContext__direction = Slot(uri=ALSKG.direction, name="geneExpressionContext__direction", curie=ALSKG.curie('direction'),
                   model_uri=ALSKG.geneExpressionContext__direction, domain=None, range=Union[str, "ExpressionDirectionEnum"])

slots.geneExpressionContext__biological_context_type = Slot(uri=ALSKG.biological_context_type, name="geneExpressionContext__biological_context_type", curie=ALSKG.curie('biological_context_type'),
                   model_uri=ALSKG.geneExpressionContext__biological_context_type, domain=None, range=Optional[Union[str, "BiologicalContextTypeEnum"]])

slots.geneExpressionContext__cell_model = Slot(uri=ALSKG.cell_model, name="geneExpressionContext__cell_model", curie=ALSKG.curie('cell_model'),
                   model_uri=ALSKG.geneExpressionContext__cell_model, domain=None, range=Optional[str])

slots.geneExpressionContext__year = Slot(uri=ALSKG.year, name="geneExpressionContext__year", curie=ALSKG.curie('year'),
                   model_uri=ALSKG.geneExpressionContext__year, domain=None, range=Optional[int])

slots.geneExpressionContext__validated_in = Slot(uri=ALSKG.validated_in, name="geneExpressionContext__validated_in", curie=ALSKG.curie('validated_in'),
                   model_uri=ALSKG.geneExpressionContext__validated_in, domain=None, range=Optional[Union[str, list[str]]])

slots.geneExpressionContext__biological_note = Slot(uri=ALSKG.biological_note, name="geneExpressionContext__biological_note", curie=ALSKG.curie('biological_note'),
                   model_uri=ALSKG.geneExpressionContext__biological_note, domain=None, range=Optional[str])

slots.Anatomy_name = Slot(uri=RDFS.label, name="Anatomy_name", curie=RDFS.curie('label'),
                   model_uri=ALSKG.Anatomy_name, domain=Anatomy, range=Optional[str])

slots.Anatomy_definition = Slot(uri=IAO['0000115'], name="Anatomy_definition", curie=IAO.curie('0000115'),
                   model_uri=ALSKG.Anatomy_definition, domain=Anatomy, range=Optional[str])

slots.Anatomy_synonyms = Slot(uri=SKOS.altLabel, name="Anatomy_synonyms", curie=SKOS.curie('altLabel'),
                   model_uri=ALSKG.Anatomy_synonyms, domain=Anatomy, range=Optional[Union[str, list[str]]])

slots.Anatomy_xrefs = Slot(uri=BIOLINK.xref, name="Anatomy_xrefs", curie=BIOLINK.curie('xref'),
                   model_uri=ALSKG.Anatomy_xrefs, domain=Anatomy, range=Optional[Union[str, list[str]]])

slots.Anatomy_ontology = Slot(uri=ALSKG.ontology, name="Anatomy_ontology", curie=ALSKG.curie('ontology'),
                   model_uri=ALSKG.Anatomy_ontology, domain=Anatomy, range=Optional[Union[str, OntologyMetadataId]])

slots.BiologicalProcess_name = Slot(uri=RDFS.label, name="BiologicalProcess_name", curie=RDFS.curie('label'),
                   model_uri=ALSKG.BiologicalProcess_name, domain=BiologicalProcess, range=Optional[str])

slots.BiologicalProcess_definition = Slot(uri=IAO['0000115'], name="BiologicalProcess_definition", curie=IAO.curie('0000115'),
                   model_uri=ALSKG.BiologicalProcess_definition, domain=BiologicalProcess, range=Optional[str])

slots.BiologicalProcess_synonyms = Slot(uri=SKOS.altLabel, name="BiologicalProcess_synonyms", curie=SKOS.curie('altLabel'),
                   model_uri=ALSKG.BiologicalProcess_synonyms, domain=BiologicalProcess, range=Optional[Union[str, list[str]]])

slots.BiologicalProcess_xrefs = Slot(uri=BIOLINK.xref, name="BiologicalProcess_xrefs", curie=BIOLINK.curie('xref'),
                   model_uri=ALSKG.BiologicalProcess_xrefs, domain=BiologicalProcess, range=Optional[Union[str, list[str]]])

slots.BiologicalProcess_ontology = Slot(uri=ALSKG.ontology, name="BiologicalProcess_ontology", curie=ALSKG.curie('ontology'),
                   model_uri=ALSKG.BiologicalProcess_ontology, domain=BiologicalProcess, range=Optional[Union[str, OntologyMetadataId]])

slots.CellularComponent_name = Slot(uri=RDFS.label, name="CellularComponent_name", curie=RDFS.curie('label'),
                   model_uri=ALSKG.CellularComponent_name, domain=CellularComponent, range=Optional[str])

slots.CellularComponent_definition = Slot(uri=IAO['0000115'], name="CellularComponent_definition", curie=IAO.curie('0000115'),
                   model_uri=ALSKG.CellularComponent_definition, domain=CellularComponent, range=Optional[str])

slots.CellularComponent_synonyms = Slot(uri=SKOS.altLabel, name="CellularComponent_synonyms", curie=SKOS.curie('altLabel'),
                   model_uri=ALSKG.CellularComponent_synonyms, domain=CellularComponent, range=Optional[Union[str, list[str]]])

slots.CellularComponent_xrefs = Slot(uri=BIOLINK.xref, name="CellularComponent_xrefs", curie=BIOLINK.curie('xref'),
                   model_uri=ALSKG.CellularComponent_xrefs, domain=CellularComponent, range=Optional[Union[str, list[str]]])

slots.CellularComponent_ontology = Slot(uri=ALSKG.ontology, name="CellularComponent_ontology", curie=ALSKG.curie('ontology'),
                   model_uri=ALSKG.CellularComponent_ontology, domain=CellularComponent, range=Optional[Union[str, OntologyMetadataId]])

slots.Disease_name = Slot(uri=RDFS.label, name="Disease_name", curie=RDFS.curie('label'),
                   model_uri=ALSKG.Disease_name, domain=Disease, range=Optional[str])

slots.Disease_description = Slot(uri=DCTERMS.description, name="Disease_description", curie=DCTERMS.curie('description'),
                   model_uri=ALSKG.Disease_description, domain=Disease, range=Optional[str])

slots.Disease_code = Slot(uri=ALSKG.code, name="Disease_code", curie=ALSKG.curie('code'),
                   model_uri=ALSKG.Disease_code, domain=Disease, range=Optional[str])

slots.Disease_parents = Slot(uri=ALSKG.parents, name="Disease_parents", curie=ALSKG.curie('parents'),
                   model_uri=ALSKG.Disease_parents, domain=Disease, range=Optional[Union[str, list[str]]])

slots.Disease_children = Slot(uri=ALSKG.children, name="Disease_children", curie=ALSKG.curie('children'),
                   model_uri=ALSKG.Disease_children, domain=Disease, range=Optional[Union[str, list[str]]])

slots.Disease_ancestors = Slot(uri=ALSKG.ancestors, name="Disease_ancestors", curie=ALSKG.curie('ancestors'),
                   model_uri=ALSKG.Disease_ancestors, domain=Disease, range=Optional[Union[str, list[str]]])

slots.Disease_descendants = Slot(uri=ALSKG.descendants, name="Disease_descendants", curie=ALSKG.curie('descendants'),
                   model_uri=ALSKG.Disease_descendants, domain=Disease, range=Optional[Union[str, list[str]]])

slots.Disease_is_leaf = Slot(uri=ALSKG.is_leaf, name="Disease_is_leaf", curie=ALSKG.curie('is_leaf'),
                   model_uri=ALSKG.Disease_is_leaf, domain=Disease, range=Optional[Union[bool, Bool]])

slots.Disease_exact_synonyms = Slot(uri=ALSKG.exact_synonyms, name="Disease_exact_synonyms", curie=ALSKG.curie('exact_synonyms'),
                   model_uri=ALSKG.Disease_exact_synonyms, domain=Disease, range=Optional[Union[str, list[str]]])

slots.Disease_related_synonyms = Slot(uri=ALSKG.related_synonyms, name="Disease_related_synonyms", curie=ALSKG.curie('related_synonyms'),
                   model_uri=ALSKG.Disease_related_synonyms, domain=Disease, range=Optional[Union[str, list[str]]])

slots.Disease_narrow_synonyms = Slot(uri=ALSKG.narrow_synonyms, name="Disease_narrow_synonyms", curie=ALSKG.curie('narrow_synonyms'),
                   model_uri=ALSKG.Disease_narrow_synonyms, domain=Disease, range=Optional[Union[str, list[str]]])

slots.Disease_broad_synonyms = Slot(uri=ALSKG.broad_synonyms, name="Disease_broad_synonyms", curie=ALSKG.curie('broad_synonyms'),
                   model_uri=ALSKG.Disease_broad_synonyms, domain=Disease, range=Optional[Union[str, list[str]]])

slots.Disease_obsolete_terms = Slot(uri=ALSKG.obsolete_terms, name="Disease_obsolete_terms", curie=ALSKG.curie('obsolete_terms'),
                   model_uri=ALSKG.Disease_obsolete_terms, domain=Disease, range=Optional[Union[str, list[str]]])

slots.Disease_obsolete_xrefs = Slot(uri=ALSKG.obsolete_xrefs, name="Disease_obsolete_xrefs", curie=ALSKG.curie('obsolete_xrefs'),
                   model_uri=ALSKG.Disease_obsolete_xrefs, domain=Disease, range=Optional[Union[str, list[str]]])

slots.Disease_xrefs = Slot(uri=BIOLINK.xref, name="Disease_xrefs", curie=BIOLINK.curie('xref'),
                   model_uri=ALSKG.Disease_xrefs, domain=Disease, range=Optional[Union[str, list[str]]])

slots.Disease_concept_ids = Slot(uri=ALSKG.concept_ids, name="Disease_concept_ids", curie=ALSKG.curie('concept_ids'),
                   model_uri=ALSKG.Disease_concept_ids, domain=Disease, range=Optional[Union[str, list[str]]])

slots.Disease_concept_names = Slot(uri=ALSKG.concept_names, name="Disease_concept_names", curie=ALSKG.curie('concept_names'),
                   model_uri=ALSKG.Disease_concept_names, domain=Disease, range=Optional[Union[str, list[str]]])

slots.Disease_umls_cui = Slot(uri=ALSKG.umls_cui, name="Disease_umls_cui", curie=ALSKG.curie('umls_cui'),
                   model_uri=ALSKG.Disease_umls_cui, domain=Disease, range=Optional[str])

slots.Disease_snomed_full_names = Slot(uri=ALSKG.snomed_full_names, name="Disease_snomed_full_names", curie=ALSKG.curie('snomed_full_names'),
                   model_uri=ALSKG.Disease_snomed_full_names, domain=Disease, range=Optional[Union[str, list[str]]])

slots.Disease_snomed_concept_ids = Slot(uri=ALSKG.snomed_concept_ids, name="Disease_snomed_concept_ids", curie=ALSKG.curie('snomed_concept_ids'),
                   model_uri=ALSKG.Disease_snomed_concept_ids, domain=Disease, range=Optional[Union[str, list[str]]])

slots.Disease_cui_semantic_type = Slot(uri=ALSKG.cui_semantic_type, name="Disease_cui_semantic_type", curie=ALSKG.curie('cui_semantic_type'),
                   model_uri=ALSKG.Disease_cui_semantic_type, domain=Disease, range=Optional[str])

slots.Drug_name = Slot(uri=RDFS.label, name="Drug_name", curie=RDFS.curie('label'),
                   model_uri=ALSKG.Drug_name, domain=Drug, range=Optional[str])

slots.Drug_type = Slot(uri=ALSKG.type, name="Drug_type", curie=ALSKG.curie('type'),
                   model_uri=ALSKG.Drug_type, domain=Drug, range=Optional[str])

slots.Drug_description = Slot(uri=DCTERMS.description, name="Drug_description", curie=DCTERMS.curie('description'),
                   model_uri=ALSKG.Drug_description, domain=Drug, range=Optional[str])

slots.Drug_synonyms = Slot(uri=SKOS.altLabel, name="Drug_synonyms", curie=SKOS.curie('altLabel'),
                   model_uri=ALSKG.Drug_synonyms, domain=Drug, range=Optional[Union[str, list[str]]])

slots.Drug_source_ids = Slot(uri=ALSKG.source_ids, name="Drug_source_ids", curie=ALSKG.curie('source_ids'),
                   model_uri=ALSKG.Drug_source_ids, domain=Drug, range=Optional[Union[str, list[str]]])

slots.Exposure_name = Slot(uri=RDFS.label, name="Exposure_name", curie=RDFS.curie('label'),
                   model_uri=ALSKG.Exposure_name, domain=Exposure, range=Optional[str])

slots.Gene_symbol = Slot(uri=ALSKG.symbol, name="Gene_symbol", curie=ALSKG.curie('symbol'),
                   model_uri=ALSKG.Gene_symbol, domain=Gene, range=Optional[str])

slots.Gene_name = Slot(uri=RDFS.label, name="Gene_name", curie=RDFS.curie('label'),
                   model_uri=ALSKG.Gene_name, domain=Gene, range=Optional[str])

slots.MolecularFunction_name = Slot(uri=RDFS.label, name="MolecularFunction_name", curie=RDFS.curie('label'),
                   model_uri=ALSKG.MolecularFunction_name, domain=MolecularFunction, range=Optional[str])

slots.MolecularFunction_definition = Slot(uri=IAO['0000115'], name="MolecularFunction_definition", curie=IAO.curie('0000115'),
                   model_uri=ALSKG.MolecularFunction_definition, domain=MolecularFunction, range=Optional[str])

slots.MolecularFunction_synonyms = Slot(uri=SKOS.altLabel, name="MolecularFunction_synonyms", curie=SKOS.curie('altLabel'),
                   model_uri=ALSKG.MolecularFunction_synonyms, domain=MolecularFunction, range=Optional[Union[str, list[str]]])

slots.MolecularFunction_xrefs = Slot(uri=BIOLINK.xref, name="MolecularFunction_xrefs", curie=BIOLINK.curie('xref'),
                   model_uri=ALSKG.MolecularFunction_xrefs, domain=MolecularFunction, range=Optional[Union[str, list[str]]])

slots.MolecularFunction_ontology = Slot(uri=ALSKG.ontology, name="MolecularFunction_ontology", curie=ALSKG.curie('ontology'),
                   model_uri=ALSKG.MolecularFunction_ontology, domain=MolecularFunction, range=Optional[Union[str, OntologyMetadataId]])

slots.Phenotype_name = Slot(uri=RDFS.label, name="Phenotype_name", curie=RDFS.curie('label'),
                   model_uri=ALSKG.Phenotype_name, domain=Phenotype, range=Optional[str])

slots.Phenotype_description = Slot(uri=DCTERMS.description, name="Phenotype_description", curie=DCTERMS.curie('description'),
                   model_uri=ALSKG.Phenotype_description, domain=Phenotype, range=Optional[str])

slots.Phenotype_code = Slot(uri=ALSKG.code, name="Phenotype_code", curie=ALSKG.curie('code'),
                   model_uri=ALSKG.Phenotype_code, domain=Phenotype, range=Optional[str])

slots.Phenotype_type = Slot(uri=ALSKG.type, name="Phenotype_type", curie=ALSKG.curie('type'),
                   model_uri=ALSKG.Phenotype_type, domain=Phenotype, range=Optional[str])

slots.Phenotype_parents = Slot(uri=ALSKG.parents, name="Phenotype_parents", curie=ALSKG.curie('parents'),
                   model_uri=ALSKG.Phenotype_parents, domain=Phenotype, range=Optional[Union[str, list[str]]])

slots.Phenotype_children = Slot(uri=ALSKG.children, name="Phenotype_children", curie=ALSKG.curie('children'),
                   model_uri=ALSKG.Phenotype_children, domain=Phenotype, range=Optional[Union[str, list[str]]])

slots.Phenotype_ancestors = Slot(uri=ALSKG.ancestors, name="Phenotype_ancestors", curie=ALSKG.curie('ancestors'),
                   model_uri=ALSKG.Phenotype_ancestors, domain=Phenotype, range=Optional[Union[str, list[str]]])

slots.Phenotype_descendants = Slot(uri=ALSKG.descendants, name="Phenotype_descendants", curie=ALSKG.curie('descendants'),
                   model_uri=ALSKG.Phenotype_descendants, domain=Phenotype, range=Optional[Union[str, list[str]]])

slots.Phenotype_is_leaf = Slot(uri=ALSKG.is_leaf, name="Phenotype_is_leaf", curie=ALSKG.curie('is_leaf'),
                   model_uri=ALSKG.Phenotype_is_leaf, domain=Phenotype, range=Optional[Union[bool, Bool]])

slots.Phenotype_exact_synonyms = Slot(uri=ALSKG.exact_synonyms, name="Phenotype_exact_synonyms", curie=ALSKG.curie('exact_synonyms'),
                   model_uri=ALSKG.Phenotype_exact_synonyms, domain=Phenotype, range=Optional[Union[str, list[str]]])

slots.Phenotype_related_synonyms = Slot(uri=ALSKG.related_synonyms, name="Phenotype_related_synonyms", curie=ALSKG.curie('related_synonyms'),
                   model_uri=ALSKG.Phenotype_related_synonyms, domain=Phenotype, range=Optional[Union[str, list[str]]])

slots.Phenotype_narrow_synonyms = Slot(uri=ALSKG.narrow_synonyms, name="Phenotype_narrow_synonyms", curie=ALSKG.curie('narrow_synonyms'),
                   model_uri=ALSKG.Phenotype_narrow_synonyms, domain=Phenotype, range=Optional[Union[str, list[str]]])

slots.Phenotype_broad_synonyms = Slot(uri=ALSKG.broad_synonyms, name="Phenotype_broad_synonyms", curie=ALSKG.curie('broad_synonyms'),
                   model_uri=ALSKG.Phenotype_broad_synonyms, domain=Phenotype, range=Optional[Union[str, list[str]]])

slots.Phenotype_obsolete_terms = Slot(uri=ALSKG.obsolete_terms, name="Phenotype_obsolete_terms", curie=ALSKG.curie('obsolete_terms'),
                   model_uri=ALSKG.Phenotype_obsolete_terms, domain=Phenotype, range=Optional[Union[str, list[str]]])

slots.Phenotype_obsolete_xrefs = Slot(uri=ALSKG.obsolete_xrefs, name="Phenotype_obsolete_xrefs", curie=ALSKG.curie('obsolete_xrefs'),
                   model_uri=ALSKG.Phenotype_obsolete_xrefs, domain=Phenotype, range=Optional[Union[str, list[str]]])

slots.Phenotype_xrefs = Slot(uri=BIOLINK.xref, name="Phenotype_xrefs", curie=BIOLINK.curie('xref'),
                   model_uri=ALSKG.Phenotype_xrefs, domain=Phenotype, range=Optional[Union[str, list[str]]])

slots.Phenotype_concept_ids = Slot(uri=ALSKG.concept_ids, name="Phenotype_concept_ids", curie=ALSKG.curie('concept_ids'),
                   model_uri=ALSKG.Phenotype_concept_ids, domain=Phenotype, range=Optional[Union[str, list[str]]])

slots.Phenotype_concept_names = Slot(uri=ALSKG.concept_names, name="Phenotype_concept_names", curie=ALSKG.curie('concept_names'),
                   model_uri=ALSKG.Phenotype_concept_names, domain=Phenotype, range=Optional[Union[str, list[str]]])

slots.Phenotype_umls_cui = Slot(uri=ALSKG.umls_cui, name="Phenotype_umls_cui", curie=ALSKG.curie('umls_cui'),
                   model_uri=ALSKG.Phenotype_umls_cui, domain=Phenotype, range=Optional[str])

slots.Phenotype_snomed_full_names = Slot(uri=ALSKG.snomed_full_names, name="Phenotype_snomed_full_names", curie=ALSKG.curie('snomed_full_names'),
                   model_uri=ALSKG.Phenotype_snomed_full_names, domain=Phenotype, range=Optional[Union[str, list[str]]])

slots.Phenotype_snomed_concept_ids = Slot(uri=ALSKG.snomed_concept_ids, name="Phenotype_snomed_concept_ids", curie=ALSKG.curie('snomed_concept_ids'),
                   model_uri=ALSKG.Phenotype_snomed_concept_ids, domain=Phenotype, range=Optional[Union[str, list[str]]])

slots.Phenotype_cui_semantic_type = Slot(uri=ALSKG.cui_semantic_type, name="Phenotype_cui_semantic_type", curie=ALSKG.curie('cui_semantic_type'),
                   model_uri=ALSKG.Phenotype_cui_semantic_type, domain=Phenotype, range=Optional[str])

slots.Phenotype_ontology = Slot(uri=ALSKG.ontology, name="Phenotype_ontology", curie=ALSKG.curie('ontology'),
                   model_uri=ALSKG.Phenotype_ontology, domain=Phenotype, range=Optional[Union[str, OntologyMetadataId]])

slots.Pathway_name = Slot(uri=RDFS.label, name="Pathway_name", curie=RDFS.curie('label'),
                   model_uri=ALSKG.Pathway_name, domain=Pathway, range=Optional[str])

slots.MolecularSubtype_name = Slot(uri=RDFS.label, name="MolecularSubtype_name", curie=RDFS.curie('label'),
                   model_uri=ALSKG.MolecularSubtype_name, domain=MolecularSubtype, range=Optional[str])

slots.MolecularSubtype_original_optimus_label = Slot(uri=ALSKG.original_optimus_label, name="MolecularSubtype_original_optimus_label", curie=ALSKG.curie('original_optimus_label'),
                   model_uri=ALSKG.MolecularSubtype_original_optimus_label, domain=MolecularSubtype, range=Optional[str])

slots.PharmacologicalRelationship_subject = Slot(uri=ALSKG.subject, name="PharmacologicalRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.PharmacologicalRelationship_subject, domain=PharmacologicalRelationship, range=Optional[Union[str, DrugId]])

slots.ExposureEntityRelationship_subject = Slot(uri=ALSKG.subject, name="ExposureEntityRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.ExposureEntityRelationship_subject, domain=ExposureEntityRelationship, range=Optional[Union[str, ExposureId]])

slots.PhenotypeHierarchyRelationship_subject = Slot(uri=ALSKG.subject, name="PhenotypeHierarchyRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.PhenotypeHierarchyRelationship_subject, domain=PhenotypeHierarchyRelationship, range=Optional[Union[str, PhenotypeId]])

slots.AnatomyGeneExpressionRelationship_subject = Slot(uri=ALSKG.subject, name="AnatomyGeneExpressionRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.AnatomyGeneExpressionRelationship_subject, domain=AnatomyGeneExpressionRelationship, range=Optional[Union[str, AnatomyId]])

slots.AnatomyGeneExpressionRelationship_object = Slot(uri=ALSKG.object, name="AnatomyGeneExpressionRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.AnatomyGeneExpressionRelationship_object, domain=AnatomyGeneExpressionRelationship, range=Optional[Union[str, GeneId]])

slots.DiseasePhenotypeRelationship_subject = Slot(uri=ALSKG.subject, name="DiseasePhenotypeRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DiseasePhenotypeRelationship_subject, domain=DiseasePhenotypeRelationship, range=Optional[Union[str, DiseaseId]])

slots.DiseasePhenotypeRelationship_object = Slot(uri=ALSKG.object, name="DiseasePhenotypeRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DiseasePhenotypeRelationship_object, domain=DiseasePhenotypeRelationship, range=Optional[Union[str, PhenotypeId]])

slots.DrugBiologicalProcessTherapeuticRelationship_subject = Slot(uri=ALSKG.subject, name="DrugBiologicalProcessTherapeuticRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugBiologicalProcessTherapeuticRelationship_subject, domain=DrugBiologicalProcessTherapeuticRelationship, range=Optional[Union[str, DrugId]])

slots.DrugBiologicalProcessTherapeuticRelationship_object = Slot(uri=ALSKG.object, name="DrugBiologicalProcessTherapeuticRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugBiologicalProcessTherapeuticRelationship_object, domain=DrugBiologicalProcessTherapeuticRelationship, range=Optional[Union[str, BiologicalProcessId]])

slots.DrugBiologicalProcessTherapeuticRelationship_highest_clinical_trial_phase = Slot(uri=ALSKG.highest_clinical_trial_phase, name="DrugBiologicalProcessTherapeuticRelationship_highest_clinical_trial_phase", curie=ALSKG.curie('highest_clinical_trial_phase'),
                   model_uri=ALSKG.DrugBiologicalProcessTherapeuticRelationship_highest_clinical_trial_phase, domain=DrugBiologicalProcessTherapeuticRelationship, range=Optional[float])

slots.DrugBiologicalProcessTherapeuticRelationship_reference_ids = Slot(uri=ALSKG.reference_ids, name="DrugBiologicalProcessTherapeuticRelationship_reference_ids", curie=ALSKG.curie('reference_ids'),
                   model_uri=ALSKG.DrugBiologicalProcessTherapeuticRelationship_reference_ids, domain=DrugBiologicalProcessTherapeuticRelationship, range=Optional[Union[str, list[str]]])

slots.DrugDiseaseTherapeuticRelationship_subject = Slot(uri=ALSKG.subject, name="DrugDiseaseTherapeuticRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugDiseaseTherapeuticRelationship_subject, domain=DrugDiseaseTherapeuticRelationship, range=Optional[Union[str, DrugId]])

slots.DrugDiseaseTherapeuticRelationship_object = Slot(uri=ALSKG.object, name="DrugDiseaseTherapeuticRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugDiseaseTherapeuticRelationship_object, domain=DrugDiseaseTherapeuticRelationship, range=Optional[Union[str, DiseaseId]])

slots.DrugDiseaseTherapeuticRelationship_highest_clinical_trial_phase = Slot(uri=ALSKG.highest_clinical_trial_phase, name="DrugDiseaseTherapeuticRelationship_highest_clinical_trial_phase", curie=ALSKG.curie('highest_clinical_trial_phase'),
                   model_uri=ALSKG.DrugDiseaseTherapeuticRelationship_highest_clinical_trial_phase, domain=DrugDiseaseTherapeuticRelationship, range=Optional[float])

slots.DrugDiseaseTherapeuticRelationship_structure_id = Slot(uri=ALSKG.structure_id, name="DrugDiseaseTherapeuticRelationship_structure_id", curie=ALSKG.curie('structure_id'),
                   model_uri=ALSKG.DrugDiseaseTherapeuticRelationship_structure_id, domain=DrugDiseaseTherapeuticRelationship, range=Optional[str])

slots.DrugDiseaseTherapeuticRelationship_drug_disease_id = Slot(uri=ALSKG.drug_disease_id, name="DrugDiseaseTherapeuticRelationship_drug_disease_id", curie=ALSKG.curie('drug_disease_id'),
                   model_uri=ALSKG.DrugDiseaseTherapeuticRelationship_drug_disease_id, domain=DrugDiseaseTherapeuticRelationship, range=Optional[str])

slots.DrugDiseaseTherapeuticRelationship_reference_ids = Slot(uri=ALSKG.reference_ids, name="DrugDiseaseTherapeuticRelationship_reference_ids", curie=ALSKG.curie('reference_ids'),
                   model_uri=ALSKG.DrugDiseaseTherapeuticRelationship_reference_ids, domain=DrugDiseaseTherapeuticRelationship, range=Optional[Union[str, list[str]]])

slots.DrugPhenotypeTherapeuticRelationship_subject = Slot(uri=ALSKG.subject, name="DrugPhenotypeTherapeuticRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugPhenotypeTherapeuticRelationship_subject, domain=DrugPhenotypeTherapeuticRelationship, range=Optional[Union[str, DrugId]])

slots.DrugPhenotypeTherapeuticRelationship_object = Slot(uri=ALSKG.object, name="DrugPhenotypeTherapeuticRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugPhenotypeTherapeuticRelationship_object, domain=DrugPhenotypeTherapeuticRelationship, range=Optional[Union[str, PhenotypeId]])

slots.DrugPhenotypeTherapeuticRelationship_highest_clinical_trial_phase = Slot(uri=ALSKG.highest_clinical_trial_phase, name="DrugPhenotypeTherapeuticRelationship_highest_clinical_trial_phase", curie=ALSKG.curie('highest_clinical_trial_phase'),
                   model_uri=ALSKG.DrugPhenotypeTherapeuticRelationship_highest_clinical_trial_phase, domain=DrugPhenotypeTherapeuticRelationship, range=Optional[float])

slots.DrugPhenotypeTherapeuticRelationship_structure_id = Slot(uri=ALSKG.structure_id, name="DrugPhenotypeTherapeuticRelationship_structure_id", curie=ALSKG.curie('structure_id'),
                   model_uri=ALSKG.DrugPhenotypeTherapeuticRelationship_structure_id, domain=DrugPhenotypeTherapeuticRelationship, range=Optional[str])

slots.DrugPhenotypeTherapeuticRelationship_drug_disease_id = Slot(uri=ALSKG.drug_disease_id, name="DrugPhenotypeTherapeuticRelationship_drug_disease_id", curie=ALSKG.curie('drug_disease_id'),
                   model_uri=ALSKG.DrugPhenotypeTherapeuticRelationship_drug_disease_id, domain=DrugPhenotypeTherapeuticRelationship, range=Optional[str])

slots.DrugPhenotypeTherapeuticRelationship_reference_ids = Slot(uri=ALSKG.reference_ids, name="DrugPhenotypeTherapeuticRelationship_reference_ids", curie=ALSKG.curie('reference_ids'),
                   model_uri=ALSKG.DrugPhenotypeTherapeuticRelationship_reference_ids, domain=DrugPhenotypeTherapeuticRelationship, range=Optional[Union[str, list[str]]])

slots.DrugDrugRelationship_subject = Slot(uri=ALSKG.subject, name="DrugDrugRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugDrugRelationship_subject, domain=DrugDrugRelationship, range=Optional[Union[str, DrugId]])

slots.DrugDrugRelationship_object = Slot(uri=ALSKG.object, name="DrugDrugRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugDrugRelationship_object, domain=DrugDrugRelationship, range=Optional[Union[str, DrugId]])

slots.DrugGeneRelationship_subject = Slot(uri=ALSKG.subject, name="DrugGeneRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugGeneRelationship_subject, domain=DrugGeneRelationship, range=Optional[Union[str, DrugId]])

slots.DrugGeneRelationship_object = Slot(uri=ALSKG.object, name="DrugGeneRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugGeneRelationship_object, domain=DrugGeneRelationship, range=Optional[Union[str, GeneId]])

slots.DrugGeneRelationship_source_ids = Slot(uri=ALSKG.source_ids, name="DrugGeneRelationship_source_ids", curie=ALSKG.curie('source_ids'),
                   model_uri=ALSKG.DrugGeneRelationship_source_ids, domain=DrugGeneRelationship, range=Optional[Union[str, list[str]]])

slots.DrugGeneTargetingRelationship_subject = Slot(uri=ALSKG.subject, name="DrugGeneTargetingRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugGeneTargetingRelationship_subject, domain=DrugGeneTargetingRelationship, range=Optional[Union[str, DrugId]])

slots.DrugGeneTargetingRelationship_object = Slot(uri=ALSKG.object, name="DrugGeneTargetingRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugGeneTargetingRelationship_object, domain=DrugGeneTargetingRelationship, range=Optional[Union[str, GeneId]])

slots.DrugGeneModulationRelationship_subject = Slot(uri=ALSKG.subject, name="DrugGeneModulationRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugGeneModulationRelationship_subject, domain=DrugGeneModulationRelationship, range=Optional[Union[str, DrugId]])

slots.DrugGeneModulationRelationship_object = Slot(uri=ALSKG.object, name="DrugGeneModulationRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugGeneModulationRelationship_object, domain=DrugGeneModulationRelationship, range=Optional[Union[str, GeneId]])

slots.DrugGeneRoleRelationship_subject = Slot(uri=ALSKG.subject, name="DrugGeneRoleRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugGeneRoleRelationship_subject, domain=DrugGeneRoleRelationship, range=Optional[Union[str, DrugId]])

slots.DrugGeneRoleRelationship_object = Slot(uri=ALSKG.object, name="DrugGeneRoleRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugGeneRoleRelationship_object, domain=DrugGeneRoleRelationship, range=Optional[Union[str, GeneId]])

slots.AnatomyHasParentAnatomyRelationship_subject = Slot(uri=ALSKG.subject, name="AnatomyHasParentAnatomyRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.AnatomyHasParentAnatomyRelationship_subject, domain=AnatomyHasParentAnatomyRelationship, range=Optional[Union[str, AnatomyId]])

slots.AnatomyHasParentAnatomyRelationship_object = Slot(uri=ALSKG.object, name="AnatomyHasParentAnatomyRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.AnatomyHasParentAnatomyRelationship_object, domain=AnatomyHasParentAnatomyRelationship, range=Optional[Union[str, AnatomyId]])

slots.AnatomyHasParentAnatomyRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="AnatomyHasParentAnatomyRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.AnatomyHasParentAnatomyRelationship_original_optimus_relationship_type, domain=AnatomyHasParentAnatomyRelationship, range=Optional[str])

slots.AnatomyHasGeneExpressionAbsentRelationship_subject = Slot(uri=ALSKG.subject, name="AnatomyHasGeneExpressionAbsentRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.AnatomyHasGeneExpressionAbsentRelationship_subject, domain=AnatomyHasGeneExpressionAbsentRelationship, range=Optional[Union[str, AnatomyId]])

slots.AnatomyHasGeneExpressionAbsentRelationship_object = Slot(uri=ALSKG.object, name="AnatomyHasGeneExpressionAbsentRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.AnatomyHasGeneExpressionAbsentRelationship_object, domain=AnatomyHasGeneExpressionAbsentRelationship, range=Optional[Union[str, GeneId]])

slots.AnatomyHasGeneExpressionAbsentRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="AnatomyHasGeneExpressionAbsentRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.AnatomyHasGeneExpressionAbsentRelationship_original_optimus_relationship_type, domain=AnatomyHasGeneExpressionAbsentRelationship, range=Optional[str])

slots.AnatomyHasGeneExpressionPresentRelationship_subject = Slot(uri=ALSKG.subject, name="AnatomyHasGeneExpressionPresentRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.AnatomyHasGeneExpressionPresentRelationship_subject, domain=AnatomyHasGeneExpressionPresentRelationship, range=Optional[Union[str, AnatomyId]])

slots.AnatomyHasGeneExpressionPresentRelationship_object = Slot(uri=ALSKG.object, name="AnatomyHasGeneExpressionPresentRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.AnatomyHasGeneExpressionPresentRelationship_object, domain=AnatomyHasGeneExpressionPresentRelationship, range=Optional[Union[str, GeneId]])

slots.AnatomyHasGeneExpressionPresentRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="AnatomyHasGeneExpressionPresentRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.AnatomyHasGeneExpressionPresentRelationship_original_optimus_relationship_type, domain=AnatomyHasGeneExpressionPresentRelationship, range=Optional[str])

slots.BiologicalProcessIsSubclassOfRelationship_subject = Slot(uri=ALSKG.subject, name="BiologicalProcessIsSubclassOfRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.BiologicalProcessIsSubclassOfRelationship_subject, domain=BiologicalProcessIsSubclassOfRelationship, range=Optional[Union[str, BiologicalProcessId]])

slots.BiologicalProcessIsSubclassOfRelationship_object = Slot(uri=ALSKG.object, name="BiologicalProcessIsSubclassOfRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.BiologicalProcessIsSubclassOfRelationship_object, domain=BiologicalProcessIsSubclassOfRelationship, range=Optional[Union[str, BiologicalProcessId]])

slots.BiologicalProcessIsSubclassOfRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="BiologicalProcessIsSubclassOfRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.BiologicalProcessIsSubclassOfRelationship_original_optimus_relationship_type, domain=BiologicalProcessIsSubclassOfRelationship, range=Optional[str])

slots.BiologicalProcessHasParticipatingGeneRelationship_subject = Slot(uri=ALSKG.subject, name="BiologicalProcessHasParticipatingGeneRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.BiologicalProcessHasParticipatingGeneRelationship_subject, domain=BiologicalProcessHasParticipatingGeneRelationship, range=Optional[Union[str, BiologicalProcessId]])

slots.BiologicalProcessHasParticipatingGeneRelationship_object = Slot(uri=ALSKG.object, name="BiologicalProcessHasParticipatingGeneRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.BiologicalProcessHasParticipatingGeneRelationship_object, domain=BiologicalProcessHasParticipatingGeneRelationship, range=Optional[Union[str, GeneId]])

slots.BiologicalProcessHasParticipatingGeneRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="BiologicalProcessHasParticipatingGeneRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.BiologicalProcessHasParticipatingGeneRelationship_original_optimus_relationship_type, domain=BiologicalProcessHasParticipatingGeneRelationship, range=Optional[str])

slots.CellularComponentIsSubclassOfRelationship_subject = Slot(uri=ALSKG.subject, name="CellularComponentIsSubclassOfRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.CellularComponentIsSubclassOfRelationship_subject, domain=CellularComponentIsSubclassOfRelationship, range=Optional[Union[str, CellularComponentId]])

slots.CellularComponentIsSubclassOfRelationship_object = Slot(uri=ALSKG.object, name="CellularComponentIsSubclassOfRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.CellularComponentIsSubclassOfRelationship_object, domain=CellularComponentIsSubclassOfRelationship, range=Optional[Union[str, CellularComponentId]])

slots.CellularComponentIsSubclassOfRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="CellularComponentIsSubclassOfRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.CellularComponentIsSubclassOfRelationship_original_optimus_relationship_type, domain=CellularComponentIsSubclassOfRelationship, range=Optional[str])

slots.CellularComponentHasLocatedGeneRelationship_subject = Slot(uri=ALSKG.subject, name="CellularComponentHasLocatedGeneRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.CellularComponentHasLocatedGeneRelationship_subject, domain=CellularComponentHasLocatedGeneRelationship, range=Optional[Union[str, CellularComponentId]])

slots.CellularComponentHasLocatedGeneRelationship_object = Slot(uri=ALSKG.object, name="CellularComponentHasLocatedGeneRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.CellularComponentHasLocatedGeneRelationship_object, domain=CellularComponentHasLocatedGeneRelationship, range=Optional[Union[str, GeneId]])

slots.CellularComponentHasLocatedGeneRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="CellularComponentHasLocatedGeneRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.CellularComponentHasLocatedGeneRelationship_original_optimus_relationship_type, domain=CellularComponentHasLocatedGeneRelationship, range=Optional[str])

slots.DiseaseHasParentDiseaseRelationship_subject = Slot(uri=ALSKG.subject, name="DiseaseHasParentDiseaseRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DiseaseHasParentDiseaseRelationship_subject, domain=DiseaseHasParentDiseaseRelationship, range=Optional[Union[str, DiseaseId]])

slots.DiseaseHasParentDiseaseRelationship_object = Slot(uri=ALSKG.object, name="DiseaseHasParentDiseaseRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DiseaseHasParentDiseaseRelationship_object, domain=DiseaseHasParentDiseaseRelationship, range=Optional[Union[str, DiseaseId]])

slots.DiseaseHasParentDiseaseRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DiseaseHasParentDiseaseRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DiseaseHasParentDiseaseRelationship_original_optimus_relationship_type, domain=DiseaseHasParentDiseaseRelationship, range=Optional[str])

slots.DiseaseAssociatedWithGeneRelationship_subject = Slot(uri=ALSKG.subject, name="DiseaseAssociatedWithGeneRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DiseaseAssociatedWithGeneRelationship_subject, domain=DiseaseAssociatedWithGeneRelationship, range=Optional[Union[str, DiseaseId]])

slots.DiseaseAssociatedWithGeneRelationship_object = Slot(uri=ALSKG.object, name="DiseaseAssociatedWithGeneRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DiseaseAssociatedWithGeneRelationship_object, domain=DiseaseAssociatedWithGeneRelationship, range=Optional[Union[str, GeneId]])

slots.DiseaseAssociatedWithGeneRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DiseaseAssociatedWithGeneRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DiseaseAssociatedWithGeneRelationship_original_optimus_relationship_type, domain=DiseaseAssociatedWithGeneRelationship, range=Optional[str])

slots.DiseaseHasPhenotypeRelationship_subject = Slot(uri=ALSKG.subject, name="DiseaseHasPhenotypeRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DiseaseHasPhenotypeRelationship_subject, domain=DiseaseHasPhenotypeRelationship, range=Optional[Union[str, DiseaseId]])

slots.DiseaseHasPhenotypeRelationship_object = Slot(uri=ALSKG.object, name="DiseaseHasPhenotypeRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DiseaseHasPhenotypeRelationship_object, domain=DiseaseHasPhenotypeRelationship, range=Optional[Union[str, PhenotypeId]])

slots.DiseaseHasPhenotypeRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DiseaseHasPhenotypeRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DiseaseHasPhenotypeRelationship_original_optimus_relationship_type, domain=DiseaseHasPhenotypeRelationship, range=Optional[str])

slots.DrugHasIndicationForBiologicalProcessRelationship_subject = Slot(uri=ALSKG.subject, name="DrugHasIndicationForBiologicalProcessRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugHasIndicationForBiologicalProcessRelationship_subject, domain=DrugHasIndicationForBiologicalProcessRelationship, range=Optional[Union[str, DrugId]])

slots.DrugHasIndicationForBiologicalProcessRelationship_object = Slot(uri=ALSKG.object, name="DrugHasIndicationForBiologicalProcessRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugHasIndicationForBiologicalProcessRelationship_object, domain=DrugHasIndicationForBiologicalProcessRelationship, range=Optional[Union[str, BiologicalProcessId]])

slots.DrugHasIndicationForBiologicalProcessRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugHasIndicationForBiologicalProcessRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugHasIndicationForBiologicalProcessRelationship_original_optimus_relationship_type, domain=DrugHasIndicationForBiologicalProcessRelationship, range=Optional[str])

slots.DrugContraindicatedForDiseaseRelationship_subject = Slot(uri=ALSKG.subject, name="DrugContraindicatedForDiseaseRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugContraindicatedForDiseaseRelationship_subject, domain=DrugContraindicatedForDiseaseRelationship, range=Optional[Union[str, DrugId]])

slots.DrugContraindicatedForDiseaseRelationship_object = Slot(uri=ALSKG.object, name="DrugContraindicatedForDiseaseRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugContraindicatedForDiseaseRelationship_object, domain=DrugContraindicatedForDiseaseRelationship, range=Optional[Union[str, DiseaseId]])

slots.DrugContraindicatedForDiseaseRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugContraindicatedForDiseaseRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugContraindicatedForDiseaseRelationship_original_optimus_relationship_type, domain=DrugContraindicatedForDiseaseRelationship, range=Optional[str])

slots.DrugIndicatedForDiseaseRelationship_subject = Slot(uri=ALSKG.subject, name="DrugIndicatedForDiseaseRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugIndicatedForDiseaseRelationship_subject, domain=DrugIndicatedForDiseaseRelationship, range=Optional[Union[str, DrugId]])

slots.DrugIndicatedForDiseaseRelationship_object = Slot(uri=ALSKG.object, name="DrugIndicatedForDiseaseRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugIndicatedForDiseaseRelationship_object, domain=DrugIndicatedForDiseaseRelationship, range=Optional[Union[str, DiseaseId]])

slots.DrugIndicatedForDiseaseRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugIndicatedForDiseaseRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugIndicatedForDiseaseRelationship_original_optimus_relationship_type, domain=DrugIndicatedForDiseaseRelationship, range=Optional[str])

slots.DrugUsedOffLabelForDiseaseRelationship_subject = Slot(uri=ALSKG.subject, name="DrugUsedOffLabelForDiseaseRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugUsedOffLabelForDiseaseRelationship_subject, domain=DrugUsedOffLabelForDiseaseRelationship, range=Optional[Union[str, DrugId]])

slots.DrugUsedOffLabelForDiseaseRelationship_object = Slot(uri=ALSKG.object, name="DrugUsedOffLabelForDiseaseRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugUsedOffLabelForDiseaseRelationship_object, domain=DrugUsedOffLabelForDiseaseRelationship, range=Optional[Union[str, DiseaseId]])

slots.DrugUsedOffLabelForDiseaseRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugUsedOffLabelForDiseaseRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugUsedOffLabelForDiseaseRelationship_original_optimus_relationship_type, domain=DrugUsedOffLabelForDiseaseRelationship, range=Optional[str])

slots.DrugHasParentDrugRelationship_subject = Slot(uri=ALSKG.subject, name="DrugHasParentDrugRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugHasParentDrugRelationship_subject, domain=DrugHasParentDrugRelationship, range=Optional[Union[str, DrugId]])

slots.DrugHasParentDrugRelationship_object = Slot(uri=ALSKG.object, name="DrugHasParentDrugRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugHasParentDrugRelationship_object, domain=DrugHasParentDrugRelationship, range=Optional[Union[str, DrugId]])

slots.DrugHasParentDrugRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugHasParentDrugRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugHasParentDrugRelationship_original_optimus_relationship_type, domain=DrugHasParentDrugRelationship, range=Optional[str])

slots.DrugHasSynergisticInteractionWithDrugRelationship_subject = Slot(uri=ALSKG.subject, name="DrugHasSynergisticInteractionWithDrugRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugHasSynergisticInteractionWithDrugRelationship_subject, domain=DrugHasSynergisticInteractionWithDrugRelationship, range=Optional[Union[str, DrugId]])

slots.DrugHasSynergisticInteractionWithDrugRelationship_object = Slot(uri=ALSKG.object, name="DrugHasSynergisticInteractionWithDrugRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugHasSynergisticInteractionWithDrugRelationship_object, domain=DrugHasSynergisticInteractionWithDrugRelationship, range=Optional[Union[str, DrugId]])

slots.DrugHasSynergisticInteractionWithDrugRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugHasSynergisticInteractionWithDrugRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugHasSynergisticInteractionWithDrugRelationship_original_optimus_relationship_type, domain=DrugHasSynergisticInteractionWithDrugRelationship, range=Optional[str])

slots.DrugActivatesGeneProductRelationship_subject = Slot(uri=ALSKG.subject, name="DrugActivatesGeneProductRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugActivatesGeneProductRelationship_subject, domain=DrugActivatesGeneProductRelationship, range=Optional[Union[str, DrugId]])

slots.DrugActivatesGeneProductRelationship_object = Slot(uri=ALSKG.object, name="DrugActivatesGeneProductRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugActivatesGeneProductRelationship_object, domain=DrugActivatesGeneProductRelationship, range=Optional[Union[str, GeneId]])

slots.DrugActivatesGeneProductRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugActivatesGeneProductRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugActivatesGeneProductRelationship_original_optimus_relationship_type, domain=DrugActivatesGeneProductRelationship, range=Optional[str])

slots.DrugAgonistOfGeneProductRelationship_subject = Slot(uri=ALSKG.subject, name="DrugAgonistOfGeneProductRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugAgonistOfGeneProductRelationship_subject, domain=DrugAgonistOfGeneProductRelationship, range=Optional[Union[str, DrugId]])

slots.DrugAgonistOfGeneProductRelationship_object = Slot(uri=ALSKG.object, name="DrugAgonistOfGeneProductRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugAgonistOfGeneProductRelationship_object, domain=DrugAgonistOfGeneProductRelationship, range=Optional[Union[str, GeneId]])

slots.DrugAgonistOfGeneProductRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugAgonistOfGeneProductRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugAgonistOfGeneProductRelationship_original_optimus_relationship_type, domain=DrugAgonistOfGeneProductRelationship, range=Optional[str])

slots.DrugAllostericAntagonistOfGeneProductRelationship_subject = Slot(uri=ALSKG.subject, name="DrugAllostericAntagonistOfGeneProductRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugAllostericAntagonistOfGeneProductRelationship_subject, domain=DrugAllostericAntagonistOfGeneProductRelationship, range=Optional[Union[str, DrugId]])

slots.DrugAllostericAntagonistOfGeneProductRelationship_object = Slot(uri=ALSKG.object, name="DrugAllostericAntagonistOfGeneProductRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugAllostericAntagonistOfGeneProductRelationship_object, domain=DrugAllostericAntagonistOfGeneProductRelationship, range=Optional[Union[str, GeneId]])

slots.DrugAllostericAntagonistOfGeneProductRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugAllostericAntagonistOfGeneProductRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugAllostericAntagonistOfGeneProductRelationship_original_optimus_relationship_type, domain=DrugAllostericAntagonistOfGeneProductRelationship, range=Optional[str])

slots.DrugAntagonistOfGeneProductRelationship_subject = Slot(uri=ALSKG.subject, name="DrugAntagonistOfGeneProductRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugAntagonistOfGeneProductRelationship_subject, domain=DrugAntagonistOfGeneProductRelationship, range=Optional[Union[str, DrugId]])

slots.DrugAntagonistOfGeneProductRelationship_object = Slot(uri=ALSKG.object, name="DrugAntagonistOfGeneProductRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugAntagonistOfGeneProductRelationship_object, domain=DrugAntagonistOfGeneProductRelationship, range=Optional[Union[str, GeneId]])

slots.DrugAntagonistOfGeneProductRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugAntagonistOfGeneProductRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugAntagonistOfGeneProductRelationship_original_optimus_relationship_type, domain=DrugAntagonistOfGeneProductRelationship, range=Optional[str])

slots.DrugBindsGeneProductRelationship_subject = Slot(uri=ALSKG.subject, name="DrugBindsGeneProductRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugBindsGeneProductRelationship_subject, domain=DrugBindsGeneProductRelationship, range=Optional[Union[str, DrugId]])

slots.DrugBindsGeneProductRelationship_object = Slot(uri=ALSKG.object, name="DrugBindsGeneProductRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugBindsGeneProductRelationship_object, domain=DrugBindsGeneProductRelationship, range=Optional[Union[str, GeneId]])

slots.DrugBindsGeneProductRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugBindsGeneProductRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugBindsGeneProductRelationship_original_optimus_relationship_type, domain=DrugBindsGeneProductRelationship, range=Optional[str])

slots.DrugBlocksGeneProductRelationship_subject = Slot(uri=ALSKG.subject, name="DrugBlocksGeneProductRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugBlocksGeneProductRelationship_subject, domain=DrugBlocksGeneProductRelationship, range=Optional[Union[str, DrugId]])

slots.DrugBlocksGeneProductRelationship_object = Slot(uri=ALSKG.object, name="DrugBlocksGeneProductRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugBlocksGeneProductRelationship_object, domain=DrugBlocksGeneProductRelationship, range=Optional[Union[str, GeneId]])

slots.DrugBlocksGeneProductRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugBlocksGeneProductRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugBlocksGeneProductRelationship_original_optimus_relationship_type, domain=DrugBlocksGeneProductRelationship, range=Optional[str])

slots.DrugHasCarrierGeneProductRelationship_subject = Slot(uri=ALSKG.subject, name="DrugHasCarrierGeneProductRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugHasCarrierGeneProductRelationship_subject, domain=DrugHasCarrierGeneProductRelationship, range=Optional[Union[str, DrugId]])

slots.DrugHasCarrierGeneProductRelationship_object = Slot(uri=ALSKG.object, name="DrugHasCarrierGeneProductRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugHasCarrierGeneProductRelationship_object, domain=DrugHasCarrierGeneProductRelationship, range=Optional[Union[str, GeneId]])

slots.DrugHasCarrierGeneProductRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugHasCarrierGeneProductRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugHasCarrierGeneProductRelationship_original_optimus_relationship_type, domain=DrugHasCarrierGeneProductRelationship, range=Optional[str])

slots.DrugDegradesGeneProductRelationship_subject = Slot(uri=ALSKG.subject, name="DrugDegradesGeneProductRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugDegradesGeneProductRelationship_subject, domain=DrugDegradesGeneProductRelationship, range=Optional[Union[str, DrugId]])

slots.DrugDegradesGeneProductRelationship_object = Slot(uri=ALSKG.object, name="DrugDegradesGeneProductRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugDegradesGeneProductRelationship_object, domain=DrugDegradesGeneProductRelationship, range=Optional[Union[str, GeneId]])

slots.DrugDegradesGeneProductRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugDegradesGeneProductRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugDegradesGeneProductRelationship_original_optimus_relationship_type, domain=DrugDegradesGeneProductRelationship, range=Optional[str])

slots.DrugHasMetabolizingEnzymeGeneProductRelationship_subject = Slot(uri=ALSKG.subject, name="DrugHasMetabolizingEnzymeGeneProductRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugHasMetabolizingEnzymeGeneProductRelationship_subject, domain=DrugHasMetabolizingEnzymeGeneProductRelationship, range=Optional[Union[str, DrugId]])

slots.DrugHasMetabolizingEnzymeGeneProductRelationship_object = Slot(uri=ALSKG.object, name="DrugHasMetabolizingEnzymeGeneProductRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugHasMetabolizingEnzymeGeneProductRelationship_object, domain=DrugHasMetabolizingEnzymeGeneProductRelationship, range=Optional[Union[str, GeneId]])

slots.DrugHasMetabolizingEnzymeGeneProductRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugHasMetabolizingEnzymeGeneProductRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugHasMetabolizingEnzymeGeneProductRelationship_original_optimus_relationship_type, domain=DrugHasMetabolizingEnzymeGeneProductRelationship, range=Optional[str])

slots.DrugInhibitsGeneProductRelationship_subject = Slot(uri=ALSKG.subject, name="DrugInhibitsGeneProductRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugInhibitsGeneProductRelationship_subject, domain=DrugInhibitsGeneProductRelationship, range=Optional[Union[str, DrugId]])

slots.DrugInhibitsGeneProductRelationship_object = Slot(uri=ALSKG.object, name="DrugInhibitsGeneProductRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugInhibitsGeneProductRelationship_object, domain=DrugInhibitsGeneProductRelationship, range=Optional[Union[str, GeneId]])

slots.DrugInhibitsGeneProductRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugInhibitsGeneProductRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugInhibitsGeneProductRelationship_original_optimus_relationship_type, domain=DrugInhibitsGeneProductRelationship, range=Optional[str])

slots.DrugInverseAgonistOfGeneProductRelationship_subject = Slot(uri=ALSKG.subject, name="DrugInverseAgonistOfGeneProductRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugInverseAgonistOfGeneProductRelationship_subject, domain=DrugInverseAgonistOfGeneProductRelationship, range=Optional[Union[str, DrugId]])

slots.DrugInverseAgonistOfGeneProductRelationship_object = Slot(uri=ALSKG.object, name="DrugInverseAgonistOfGeneProductRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugInverseAgonistOfGeneProductRelationship_object, domain=DrugInverseAgonistOfGeneProductRelationship, range=Optional[Union[str, GeneId]])

slots.DrugInverseAgonistOfGeneProductRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugInverseAgonistOfGeneProductRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugInverseAgonistOfGeneProductRelationship_original_optimus_relationship_type, domain=DrugInverseAgonistOfGeneProductRelationship, range=Optional[str])

slots.DrugModulatesGeneProductRelationship_subject = Slot(uri=ALSKG.subject, name="DrugModulatesGeneProductRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugModulatesGeneProductRelationship_subject, domain=DrugModulatesGeneProductRelationship, range=Optional[Union[str, DrugId]])

slots.DrugModulatesGeneProductRelationship_object = Slot(uri=ALSKG.object, name="DrugModulatesGeneProductRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugModulatesGeneProductRelationship_object, domain=DrugModulatesGeneProductRelationship, range=Optional[Union[str, GeneId]])

slots.DrugModulatesGeneProductRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugModulatesGeneProductRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugModulatesGeneProductRelationship_original_optimus_relationship_type, domain=DrugModulatesGeneProductRelationship, range=Optional[str])

slots.DrugNegativeAllostericModulatorOfGeneProductRelationship_subject = Slot(uri=ALSKG.subject, name="DrugNegativeAllostericModulatorOfGeneProductRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugNegativeAllostericModulatorOfGeneProductRelationship_subject, domain=DrugNegativeAllostericModulatorOfGeneProductRelationship, range=Optional[Union[str, DrugId]])

slots.DrugNegativeAllostericModulatorOfGeneProductRelationship_object = Slot(uri=ALSKG.object, name="DrugNegativeAllostericModulatorOfGeneProductRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugNegativeAllostericModulatorOfGeneProductRelationship_object, domain=DrugNegativeAllostericModulatorOfGeneProductRelationship, range=Optional[Union[str, GeneId]])

slots.DrugNegativeAllostericModulatorOfGeneProductRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugNegativeAllostericModulatorOfGeneProductRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugNegativeAllostericModulatorOfGeneProductRelationship_original_optimus_relationship_type, domain=DrugNegativeAllostericModulatorOfGeneProductRelationship, range=Optional[str])

slots.DrugNegativelyModulatesGeneProductRelationship_subject = Slot(uri=ALSKG.subject, name="DrugNegativelyModulatesGeneProductRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugNegativelyModulatesGeneProductRelationship_subject, domain=DrugNegativelyModulatesGeneProductRelationship, range=Optional[Union[str, DrugId]])

slots.DrugNegativelyModulatesGeneProductRelationship_object = Slot(uri=ALSKG.object, name="DrugNegativelyModulatesGeneProductRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugNegativelyModulatesGeneProductRelationship_object, domain=DrugNegativelyModulatesGeneProductRelationship, range=Optional[Union[str, GeneId]])

slots.DrugNegativelyModulatesGeneProductRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugNegativelyModulatesGeneProductRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugNegativelyModulatesGeneProductRelationship_original_optimus_relationship_type, domain=DrugNegativelyModulatesGeneProductRelationship, range=Optional[str])

slots.DrugOpensGeneProductRelationship_subject = Slot(uri=ALSKG.subject, name="DrugOpensGeneProductRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugOpensGeneProductRelationship_subject, domain=DrugOpensGeneProductRelationship, range=Optional[Union[str, DrugId]])

slots.DrugOpensGeneProductRelationship_object = Slot(uri=ALSKG.object, name="DrugOpensGeneProductRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugOpensGeneProductRelationship_object, domain=DrugOpensGeneProductRelationship, range=Optional[Union[str, GeneId]])

slots.DrugOpensGeneProductRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugOpensGeneProductRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugOpensGeneProductRelationship_original_optimus_relationship_type, domain=DrugOpensGeneProductRelationship, range=Optional[str])

slots.DrugPartialAgonistOfGeneProductRelationship_subject = Slot(uri=ALSKG.subject, name="DrugPartialAgonistOfGeneProductRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugPartialAgonistOfGeneProductRelationship_subject, domain=DrugPartialAgonistOfGeneProductRelationship, range=Optional[Union[str, DrugId]])

slots.DrugPartialAgonistOfGeneProductRelationship_object = Slot(uri=ALSKG.object, name="DrugPartialAgonistOfGeneProductRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugPartialAgonistOfGeneProductRelationship_object, domain=DrugPartialAgonistOfGeneProductRelationship, range=Optional[Union[str, GeneId]])

slots.DrugPartialAgonistOfGeneProductRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugPartialAgonistOfGeneProductRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugPartialAgonistOfGeneProductRelationship_original_optimus_relationship_type, domain=DrugPartialAgonistOfGeneProductRelationship, range=Optional[str])

slots.DrugPositiveAllostericModulatorOfGeneProductRelationship_subject = Slot(uri=ALSKG.subject, name="DrugPositiveAllostericModulatorOfGeneProductRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugPositiveAllostericModulatorOfGeneProductRelationship_subject, domain=DrugPositiveAllostericModulatorOfGeneProductRelationship, range=Optional[Union[str, DrugId]])

slots.DrugPositiveAllostericModulatorOfGeneProductRelationship_object = Slot(uri=ALSKG.object, name="DrugPositiveAllostericModulatorOfGeneProductRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugPositiveAllostericModulatorOfGeneProductRelationship_object, domain=DrugPositiveAllostericModulatorOfGeneProductRelationship, range=Optional[Union[str, GeneId]])

slots.DrugPositiveAllostericModulatorOfGeneProductRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugPositiveAllostericModulatorOfGeneProductRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugPositiveAllostericModulatorOfGeneProductRelationship_original_optimus_relationship_type, domain=DrugPositiveAllostericModulatorOfGeneProductRelationship, range=Optional[str])

slots.DrugPositivelyModulatesGeneProductRelationship_subject = Slot(uri=ALSKG.subject, name="DrugPositivelyModulatesGeneProductRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugPositivelyModulatesGeneProductRelationship_subject, domain=DrugPositivelyModulatesGeneProductRelationship, range=Optional[Union[str, DrugId]])

slots.DrugPositivelyModulatesGeneProductRelationship_object = Slot(uri=ALSKG.object, name="DrugPositivelyModulatesGeneProductRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugPositivelyModulatesGeneProductRelationship_object, domain=DrugPositivelyModulatesGeneProductRelationship, range=Optional[Union[str, GeneId]])

slots.DrugPositivelyModulatesGeneProductRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugPositivelyModulatesGeneProductRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugPositivelyModulatesGeneProductRelationship_original_optimus_relationship_type, domain=DrugPositivelyModulatesGeneProductRelationship, range=Optional[str])

slots.DrugReleasingAgentOfGeneProductRelationship_subject = Slot(uri=ALSKG.subject, name="DrugReleasingAgentOfGeneProductRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugReleasingAgentOfGeneProductRelationship_subject, domain=DrugReleasingAgentOfGeneProductRelationship, range=Optional[Union[str, DrugId]])

slots.DrugReleasingAgentOfGeneProductRelationship_object = Slot(uri=ALSKG.object, name="DrugReleasingAgentOfGeneProductRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugReleasingAgentOfGeneProductRelationship_object, domain=DrugReleasingAgentOfGeneProductRelationship, range=Optional[Union[str, GeneId]])

slots.DrugReleasingAgentOfGeneProductRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugReleasingAgentOfGeneProductRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugReleasingAgentOfGeneProductRelationship_original_optimus_relationship_type, domain=DrugReleasingAgentOfGeneProductRelationship, range=Optional[str])

slots.DrugStabilizesGeneProductRelationship_subject = Slot(uri=ALSKG.subject, name="DrugStabilizesGeneProductRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugStabilizesGeneProductRelationship_subject, domain=DrugStabilizesGeneProductRelationship, range=Optional[Union[str, DrugId]])

slots.DrugStabilizesGeneProductRelationship_object = Slot(uri=ALSKG.object, name="DrugStabilizesGeneProductRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugStabilizesGeneProductRelationship_object, domain=DrugStabilizesGeneProductRelationship, range=Optional[Union[str, GeneId]])

slots.DrugStabilizesGeneProductRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugStabilizesGeneProductRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugStabilizesGeneProductRelationship_original_optimus_relationship_type, domain=DrugStabilizesGeneProductRelationship, range=Optional[str])

slots.DrugIsSubstrateOfGeneProductRelationship_subject = Slot(uri=ALSKG.subject, name="DrugIsSubstrateOfGeneProductRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugIsSubstrateOfGeneProductRelationship_subject, domain=DrugIsSubstrateOfGeneProductRelationship, range=Optional[Union[str, DrugId]])

slots.DrugIsSubstrateOfGeneProductRelationship_object = Slot(uri=ALSKG.object, name="DrugIsSubstrateOfGeneProductRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugIsSubstrateOfGeneProductRelationship_object, domain=DrugIsSubstrateOfGeneProductRelationship, range=Optional[Union[str, GeneId]])

slots.DrugIsSubstrateOfGeneProductRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugIsSubstrateOfGeneProductRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugIsSubstrateOfGeneProductRelationship_original_optimus_relationship_type, domain=DrugIsSubstrateOfGeneProductRelationship, range=Optional[str])

slots.DrugTargetsGeneProductRelationship_subject = Slot(uri=ALSKG.subject, name="DrugTargetsGeneProductRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugTargetsGeneProductRelationship_subject, domain=DrugTargetsGeneProductRelationship, range=Optional[Union[str, DrugId]])

slots.DrugTargetsGeneProductRelationship_object = Slot(uri=ALSKG.object, name="DrugTargetsGeneProductRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugTargetsGeneProductRelationship_object, domain=DrugTargetsGeneProductRelationship, range=Optional[Union[str, GeneId]])

slots.DrugTargetsGeneProductRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugTargetsGeneProductRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugTargetsGeneProductRelationship_original_optimus_relationship_type, domain=DrugTargetsGeneProductRelationship, range=Optional[str])

slots.DrugHasTransporterGeneProductRelationship_subject = Slot(uri=ALSKG.subject, name="DrugHasTransporterGeneProductRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugHasTransporterGeneProductRelationship_subject, domain=DrugHasTransporterGeneProductRelationship, range=Optional[Union[str, DrugId]])

slots.DrugHasTransporterGeneProductRelationship_object = Slot(uri=ALSKG.object, name="DrugHasTransporterGeneProductRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugHasTransporterGeneProductRelationship_object, domain=DrugHasTransporterGeneProductRelationship, range=Optional[Union[str, GeneId]])

slots.DrugHasTransporterGeneProductRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugHasTransporterGeneProductRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugHasTransporterGeneProductRelationship_original_optimus_relationship_type, domain=DrugHasTransporterGeneProductRelationship, range=Optional[str])

slots.DrugHasAdversePhenotypeRelationship_subject = Slot(uri=ALSKG.subject, name="DrugHasAdversePhenotypeRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugHasAdversePhenotypeRelationship_subject, domain=DrugHasAdversePhenotypeRelationship, range=Optional[Union[str, DrugId]])

slots.DrugHasAdversePhenotypeRelationship_object = Slot(uri=ALSKG.object, name="DrugHasAdversePhenotypeRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugHasAdversePhenotypeRelationship_object, domain=DrugHasAdversePhenotypeRelationship, range=Optional[Union[str, PhenotypeId]])

slots.DrugHasAdversePhenotypeRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugHasAdversePhenotypeRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugHasAdversePhenotypeRelationship_original_optimus_relationship_type, domain=DrugHasAdversePhenotypeRelationship, range=Optional[str])

slots.DrugAssociatedWithPhenotypeRelationship_subject = Slot(uri=ALSKG.subject, name="DrugAssociatedWithPhenotypeRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugAssociatedWithPhenotypeRelationship_subject, domain=DrugAssociatedWithPhenotypeRelationship, range=Optional[Union[str, DrugId]])

slots.DrugAssociatedWithPhenotypeRelationship_object = Slot(uri=ALSKG.object, name="DrugAssociatedWithPhenotypeRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugAssociatedWithPhenotypeRelationship_object, domain=DrugAssociatedWithPhenotypeRelationship, range=Optional[Union[str, PhenotypeId]])

slots.DrugAssociatedWithPhenotypeRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugAssociatedWithPhenotypeRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugAssociatedWithPhenotypeRelationship_original_optimus_relationship_type, domain=DrugAssociatedWithPhenotypeRelationship, range=Optional[str])

slots.DrugContraindicatedForPhenotypeRelationship_subject = Slot(uri=ALSKG.subject, name="DrugContraindicatedForPhenotypeRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugContraindicatedForPhenotypeRelationship_subject, domain=DrugContraindicatedForPhenotypeRelationship, range=Optional[Union[str, DrugId]])

slots.DrugContraindicatedForPhenotypeRelationship_object = Slot(uri=ALSKG.object, name="DrugContraindicatedForPhenotypeRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugContraindicatedForPhenotypeRelationship_object, domain=DrugContraindicatedForPhenotypeRelationship, range=Optional[Union[str, PhenotypeId]])

slots.DrugContraindicatedForPhenotypeRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugContraindicatedForPhenotypeRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugContraindicatedForPhenotypeRelationship_original_optimus_relationship_type, domain=DrugContraindicatedForPhenotypeRelationship, range=Optional[str])

slots.DrugIndicatedForPhenotypeRelationship_subject = Slot(uri=ALSKG.subject, name="DrugIndicatedForPhenotypeRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugIndicatedForPhenotypeRelationship_subject, domain=DrugIndicatedForPhenotypeRelationship, range=Optional[Union[str, DrugId]])

slots.DrugIndicatedForPhenotypeRelationship_object = Slot(uri=ALSKG.object, name="DrugIndicatedForPhenotypeRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugIndicatedForPhenotypeRelationship_object, domain=DrugIndicatedForPhenotypeRelationship, range=Optional[Union[str, PhenotypeId]])

slots.DrugIndicatedForPhenotypeRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugIndicatedForPhenotypeRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugIndicatedForPhenotypeRelationship_original_optimus_relationship_type, domain=DrugIndicatedForPhenotypeRelationship, range=Optional[str])

slots.DrugUsedOffLabelForPhenotypeRelationship_subject = Slot(uri=ALSKG.subject, name="DrugUsedOffLabelForPhenotypeRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugUsedOffLabelForPhenotypeRelationship_subject, domain=DrugUsedOffLabelForPhenotypeRelationship, range=Optional[Union[str, DrugId]])

slots.DrugUsedOffLabelForPhenotypeRelationship_object = Slot(uri=ALSKG.object, name="DrugUsedOffLabelForPhenotypeRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugUsedOffLabelForPhenotypeRelationship_object, domain=DrugUsedOffLabelForPhenotypeRelationship, range=Optional[Union[str, PhenotypeId]])

slots.DrugUsedOffLabelForPhenotypeRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugUsedOffLabelForPhenotypeRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugUsedOffLabelForPhenotypeRelationship_original_optimus_relationship_type, domain=DrugUsedOffLabelForPhenotypeRelationship, range=Optional[str])

slots.ExposureAssociatedWithBiologicalProcessRelationship_subject = Slot(uri=ALSKG.subject, name="ExposureAssociatedWithBiologicalProcessRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.ExposureAssociatedWithBiologicalProcessRelationship_subject, domain=ExposureAssociatedWithBiologicalProcessRelationship, range=Optional[Union[str, ExposureId]])

slots.ExposureAssociatedWithBiologicalProcessRelationship_object = Slot(uri=ALSKG.object, name="ExposureAssociatedWithBiologicalProcessRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.ExposureAssociatedWithBiologicalProcessRelationship_object, domain=ExposureAssociatedWithBiologicalProcessRelationship, range=Optional[Union[str, BiologicalProcessId]])

slots.ExposureAssociatedWithBiologicalProcessRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="ExposureAssociatedWithBiologicalProcessRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.ExposureAssociatedWithBiologicalProcessRelationship_original_optimus_relationship_type, domain=ExposureAssociatedWithBiologicalProcessRelationship, range=Optional[str])

slots.ExposureAssociatedWithCellularComponentRelationship_subject = Slot(uri=ALSKG.subject, name="ExposureAssociatedWithCellularComponentRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.ExposureAssociatedWithCellularComponentRelationship_subject, domain=ExposureAssociatedWithCellularComponentRelationship, range=Optional[Union[str, ExposureId]])

slots.ExposureAssociatedWithCellularComponentRelationship_object = Slot(uri=ALSKG.object, name="ExposureAssociatedWithCellularComponentRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.ExposureAssociatedWithCellularComponentRelationship_object, domain=ExposureAssociatedWithCellularComponentRelationship, range=Optional[Union[str, CellularComponentId]])

slots.ExposureAssociatedWithCellularComponentRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="ExposureAssociatedWithCellularComponentRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.ExposureAssociatedWithCellularComponentRelationship_original_optimus_relationship_type, domain=ExposureAssociatedWithCellularComponentRelationship, range=Optional[str])

slots.ExposureLinkedToDiseaseRelationship_subject = Slot(uri=ALSKG.subject, name="ExposureLinkedToDiseaseRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.ExposureLinkedToDiseaseRelationship_subject, domain=ExposureLinkedToDiseaseRelationship, range=Optional[Union[str, ExposureId]])

slots.ExposureLinkedToDiseaseRelationship_object = Slot(uri=ALSKG.object, name="ExposureLinkedToDiseaseRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.ExposureLinkedToDiseaseRelationship_object, domain=ExposureLinkedToDiseaseRelationship, range=Optional[Union[str, DiseaseId]])

slots.ExposureLinkedToDiseaseRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="ExposureLinkedToDiseaseRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.ExposureLinkedToDiseaseRelationship_original_optimus_relationship_type, domain=ExposureLinkedToDiseaseRelationship, range=Optional[str])

slots.ExposureHasParentExposureRelationship_subject = Slot(uri=ALSKG.subject, name="ExposureHasParentExposureRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.ExposureHasParentExposureRelationship_subject, domain=ExposureHasParentExposureRelationship, range=Optional[Union[str, ExposureId]])

slots.ExposureHasParentExposureRelationship_object = Slot(uri=ALSKG.object, name="ExposureHasParentExposureRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.ExposureHasParentExposureRelationship_object, domain=ExposureHasParentExposureRelationship, range=Optional[Union[str, ExposureId]])

slots.ExposureHasParentExposureRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="ExposureHasParentExposureRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.ExposureHasParentExposureRelationship_original_optimus_relationship_type, domain=ExposureHasParentExposureRelationship, range=Optional[str])

slots.ExposureAssociatedWithGeneRelationship_subject = Slot(uri=ALSKG.subject, name="ExposureAssociatedWithGeneRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.ExposureAssociatedWithGeneRelationship_subject, domain=ExposureAssociatedWithGeneRelationship, range=Optional[Union[str, ExposureId]])

slots.ExposureAssociatedWithGeneRelationship_object = Slot(uri=ALSKG.object, name="ExposureAssociatedWithGeneRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.ExposureAssociatedWithGeneRelationship_object, domain=ExposureAssociatedWithGeneRelationship, range=Optional[Union[str, GeneId]])

slots.ExposureAssociatedWithGeneRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="ExposureAssociatedWithGeneRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.ExposureAssociatedWithGeneRelationship_original_optimus_relationship_type, domain=ExposureAssociatedWithGeneRelationship, range=Optional[str])

slots.ExposureAssociatedWithMolecularFunctionRelationship_subject = Slot(uri=ALSKG.subject, name="ExposureAssociatedWithMolecularFunctionRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.ExposureAssociatedWithMolecularFunctionRelationship_subject, domain=ExposureAssociatedWithMolecularFunctionRelationship, range=Optional[Union[str, ExposureId]])

slots.ExposureAssociatedWithMolecularFunctionRelationship_object = Slot(uri=ALSKG.object, name="ExposureAssociatedWithMolecularFunctionRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.ExposureAssociatedWithMolecularFunctionRelationship_object, domain=ExposureAssociatedWithMolecularFunctionRelationship, range=Optional[Union[str, MolecularFunctionId]])

slots.ExposureAssociatedWithMolecularFunctionRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="ExposureAssociatedWithMolecularFunctionRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.ExposureAssociatedWithMolecularFunctionRelationship_original_optimus_relationship_type, domain=ExposureAssociatedWithMolecularFunctionRelationship, range=Optional[str])

slots.GeneInteractsWithGeneRelationship_subject = Slot(uri=ALSKG.subject, name="GeneInteractsWithGeneRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.GeneInteractsWithGeneRelationship_subject, domain=GeneInteractsWithGeneRelationship, range=Optional[Union[str, GeneId]])

slots.GeneInteractsWithGeneRelationship_object = Slot(uri=ALSKG.object, name="GeneInteractsWithGeneRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.GeneInteractsWithGeneRelationship_object, domain=GeneInteractsWithGeneRelationship, range=Optional[Union[str, GeneId]])

slots.GeneInteractsWithGeneRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="GeneInteractsWithGeneRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.GeneInteractsWithGeneRelationship_original_optimus_relationship_type, domain=GeneInteractsWithGeneRelationship, range=Optional[str])

slots.MolecularFunctionEnabledByGeneRelationship_subject = Slot(uri=ALSKG.subject, name="MolecularFunctionEnabledByGeneRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.MolecularFunctionEnabledByGeneRelationship_subject, domain=MolecularFunctionEnabledByGeneRelationship, range=Optional[Union[str, MolecularFunctionId]])

slots.MolecularFunctionEnabledByGeneRelationship_object = Slot(uri=ALSKG.object, name="MolecularFunctionEnabledByGeneRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.MolecularFunctionEnabledByGeneRelationship_object, domain=MolecularFunctionEnabledByGeneRelationship, range=Optional[Union[str, GeneId]])

slots.MolecularFunctionEnabledByGeneRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="MolecularFunctionEnabledByGeneRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.MolecularFunctionEnabledByGeneRelationship_original_optimus_relationship_type, domain=MolecularFunctionEnabledByGeneRelationship, range=Optional[str])

slots.MolecularFunctionIsSubclassOfRelationship_subject = Slot(uri=ALSKG.subject, name="MolecularFunctionIsSubclassOfRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.MolecularFunctionIsSubclassOfRelationship_subject, domain=MolecularFunctionIsSubclassOfRelationship, range=Optional[Union[str, MolecularFunctionId]])

slots.MolecularFunctionIsSubclassOfRelationship_object = Slot(uri=ALSKG.object, name="MolecularFunctionIsSubclassOfRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.MolecularFunctionIsSubclassOfRelationship_object, domain=MolecularFunctionIsSubclassOfRelationship, range=Optional[Union[str, MolecularFunctionId]])

slots.MolecularFunctionIsSubclassOfRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="MolecularFunctionIsSubclassOfRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.MolecularFunctionIsSubclassOfRelationship_original_optimus_relationship_type, domain=MolecularFunctionIsSubclassOfRelationship, range=Optional[str])

slots.PhenotypeHasParentDiseaseRelationship_subject = Slot(uri=ALSKG.subject, name="PhenotypeHasParentDiseaseRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.PhenotypeHasParentDiseaseRelationship_subject, domain=PhenotypeHasParentDiseaseRelationship, range=Optional[Union[str, PhenotypeId]])

slots.PhenotypeHasParentDiseaseRelationship_object = Slot(uri=ALSKG.object, name="PhenotypeHasParentDiseaseRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.PhenotypeHasParentDiseaseRelationship_object, domain=PhenotypeHasParentDiseaseRelationship, range=Optional[Union[str, DiseaseId]])

slots.PhenotypeHasParentDiseaseRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="PhenotypeHasParentDiseaseRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.PhenotypeHasParentDiseaseRelationship_original_optimus_relationship_type, domain=PhenotypeHasParentDiseaseRelationship, range=Optional[str])

slots.PhenotypeAssociatedWithGeneRelationship_subject = Slot(uri=ALSKG.subject, name="PhenotypeAssociatedWithGeneRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.PhenotypeAssociatedWithGeneRelationship_subject, domain=PhenotypeAssociatedWithGeneRelationship, range=Optional[Union[str, PhenotypeId]])

slots.PhenotypeAssociatedWithGeneRelationship_object = Slot(uri=ALSKG.object, name="PhenotypeAssociatedWithGeneRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.PhenotypeAssociatedWithGeneRelationship_object, domain=PhenotypeAssociatedWithGeneRelationship, range=Optional[Union[str, GeneId]])

slots.PhenotypeAssociatedWithGeneRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="PhenotypeAssociatedWithGeneRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.PhenotypeAssociatedWithGeneRelationship_original_optimus_relationship_type, domain=PhenotypeAssociatedWithGeneRelationship, range=Optional[str])

slots.PhenotypeHasParentPhenotypeRelationship_subject = Slot(uri=ALSKG.subject, name="PhenotypeHasParentPhenotypeRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.PhenotypeHasParentPhenotypeRelationship_subject, domain=PhenotypeHasParentPhenotypeRelationship, range=Optional[Union[str, PhenotypeId]])

slots.PhenotypeHasParentPhenotypeRelationship_object = Slot(uri=ALSKG.object, name="PhenotypeHasParentPhenotypeRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.PhenotypeHasParentPhenotypeRelationship_object, domain=PhenotypeHasParentPhenotypeRelationship, range=Optional[Union[str, PhenotypeId]])

slots.PhenotypeHasParentPhenotypeRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="PhenotypeHasParentPhenotypeRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.PhenotypeHasParentPhenotypeRelationship_original_optimus_relationship_type, domain=PhenotypeHasParentPhenotypeRelationship, range=Optional[str])

slots.PathwayHasMemberGeneRelationship_subject = Slot(uri=ALSKG.subject, name="PathwayHasMemberGeneRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.PathwayHasMemberGeneRelationship_subject, domain=PathwayHasMemberGeneRelationship, range=Optional[Union[str, PathwayId]])

slots.PathwayHasMemberGeneRelationship_object = Slot(uri=ALSKG.object, name="PathwayHasMemberGeneRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.PathwayHasMemberGeneRelationship_object, domain=PathwayHasMemberGeneRelationship, range=Optional[Union[str, GeneId]])

slots.PathwayHasMemberGeneRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="PathwayHasMemberGeneRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.PathwayHasMemberGeneRelationship_original_optimus_relationship_type, domain=PathwayHasMemberGeneRelationship, range=Optional[str])

slots.PathwayHasParentPathwayRelationship_subject = Slot(uri=ALSKG.subject, name="PathwayHasParentPathwayRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.PathwayHasParentPathwayRelationship_subject, domain=PathwayHasParentPathwayRelationship, range=Optional[Union[str, PathwayId]])

slots.PathwayHasParentPathwayRelationship_object = Slot(uri=ALSKG.object, name="PathwayHasParentPathwayRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.PathwayHasParentPathwayRelationship_object, domain=PathwayHasParentPathwayRelationship, range=Optional[Union[str, PathwayId]])

slots.PathwayHasParentPathwayRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="PathwayHasParentPathwayRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.PathwayHasParentPathwayRelationship_original_optimus_relationship_type, domain=PathwayHasParentPathwayRelationship, range=Optional[str])

slots.DiseaseHasMolecularSubtypeConcreteRelationship_subject = Slot(uri=ALSKG.subject, name="DiseaseHasMolecularSubtypeConcreteRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DiseaseHasMolecularSubtypeConcreteRelationship_subject, domain=DiseaseHasMolecularSubtypeConcreteRelationship, range=Optional[Union[str, DiseaseId]])

slots.DiseaseHasMolecularSubtypeConcreteRelationship_object = Slot(uri=ALSKG.object, name="DiseaseHasMolecularSubtypeConcreteRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DiseaseHasMolecularSubtypeConcreteRelationship_object, domain=DiseaseHasMolecularSubtypeConcreteRelationship, range=Optional[Union[str, MolecularSubtypeId]])

slots.DiseaseHasMolecularSubtypeConcreteRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DiseaseHasMolecularSubtypeConcreteRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DiseaseHasMolecularSubtypeConcreteRelationship_original_optimus_relationship_type, domain=DiseaseHasMolecularSubtypeConcreteRelationship, range=Optional[str])

slots.MolecularSubtypeHasParentDiseaseRelationship_subject = Slot(uri=ALSKG.subject, name="MolecularSubtypeHasParentDiseaseRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.MolecularSubtypeHasParentDiseaseRelationship_subject, domain=MolecularSubtypeHasParentDiseaseRelationship, range=Optional[Union[str, MolecularSubtypeId]])

slots.MolecularSubtypeHasParentDiseaseRelationship_object = Slot(uri=ALSKG.object, name="MolecularSubtypeHasParentDiseaseRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.MolecularSubtypeHasParentDiseaseRelationship_object, domain=MolecularSubtypeHasParentDiseaseRelationship, range=Optional[Union[str, DiseaseId]])

slots.MolecularSubtypeHasParentDiseaseRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="MolecularSubtypeHasParentDiseaseRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.MolecularSubtypeHasParentDiseaseRelationship_original_optimus_relationship_type, domain=MolecularSubtypeHasParentDiseaseRelationship, range=Optional[str])

slots.MolecularSubtypeMeasuredInAnatomyRelationship_subject = Slot(uri=ALSKG.subject, name="MolecularSubtypeMeasuredInAnatomyRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.MolecularSubtypeMeasuredInAnatomyRelationship_subject, domain=MolecularSubtypeMeasuredInAnatomyRelationship, range=Optional[Union[str, MolecularSubtypeId]])

slots.MolecularSubtypeMeasuredInAnatomyRelationship_object = Slot(uri=ALSKG.object, name="MolecularSubtypeMeasuredInAnatomyRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.MolecularSubtypeMeasuredInAnatomyRelationship_object, domain=MolecularSubtypeMeasuredInAnatomyRelationship, range=Optional[Union[str, AnatomyId]])

slots.MolecularSubtypeMeasuredInAnatomyRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="MolecularSubtypeMeasuredInAnatomyRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.MolecularSubtypeMeasuredInAnatomyRelationship_original_optimus_relationship_type, domain=MolecularSubtypeMeasuredInAnatomyRelationship, range=Optional[str])

slots.GeneHasExpressionContextRelationship_subject = Slot(uri=ALSKG.subject, name="GeneHasExpressionContextRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.GeneHasExpressionContextRelationship_subject, domain=GeneHasExpressionContextRelationship, range=Optional[Union[str, GeneId]])

slots.GeneHasExpressionContextRelationship_object = Slot(uri=ALSKG.object, name="GeneHasExpressionContextRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.GeneHasExpressionContextRelationship_object, domain=GeneHasExpressionContextRelationship, range=Optional[Union[str, GeneExpressionContextId]])

slots.GeneHasExpressionContextRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="GeneHasExpressionContextRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.GeneHasExpressionContextRelationship_original_optimus_relationship_type, domain=GeneHasExpressionContextRelationship, range=Optional[str])

slots.ExpressionContextInAnatomyRelationship_subject = Slot(uri=ALSKG.subject, name="ExpressionContextInAnatomyRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.ExpressionContextInAnatomyRelationship_subject, domain=ExpressionContextInAnatomyRelationship, range=Optional[Union[str, GeneExpressionContextId]])

slots.ExpressionContextInAnatomyRelationship_object = Slot(uri=ALSKG.object, name="ExpressionContextInAnatomyRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.ExpressionContextInAnatomyRelationship_object, domain=ExpressionContextInAnatomyRelationship, range=Optional[Union[str, AnatomyId]])

slots.ExpressionContextInAnatomyRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="ExpressionContextInAnatomyRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.ExpressionContextInAnatomyRelationship_original_optimus_relationship_type, domain=ExpressionContextInAnatomyRelationship, range=Optional[str])

slots.ExpressionContextInMolecularSubtypeRelationship_subject = Slot(uri=ALSKG.subject, name="ExpressionContextInMolecularSubtypeRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.ExpressionContextInMolecularSubtypeRelationship_subject, domain=ExpressionContextInMolecularSubtypeRelationship, range=Optional[Union[str, GeneExpressionContextId]])

slots.ExpressionContextInMolecularSubtypeRelationship_object = Slot(uri=ALSKG.object, name="ExpressionContextInMolecularSubtypeRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.ExpressionContextInMolecularSubtypeRelationship_object, domain=ExpressionContextInMolecularSubtypeRelationship, range=Optional[Union[str, MolecularSubtypeId]])

slots.ExpressionContextInMolecularSubtypeRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="ExpressionContextInMolecularSubtypeRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.ExpressionContextInMolecularSubtypeRelationship_original_optimus_relationship_type, domain=ExpressionContextInMolecularSubtypeRelationship, range=Optional[str])

slots.DiseaseHasALSSubtypeRelationship_subject = Slot(uri=ALSKG.subject, name="DiseaseHasALSSubtypeRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DiseaseHasALSSubtypeRelationship_subject, domain=DiseaseHasALSSubtypeRelationship, range=Optional[Union[str, DiseaseId]])

slots.DiseaseHasALSSubtypeRelationship_object = Slot(uri=ALSKG.object, name="DiseaseHasALSSubtypeRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DiseaseHasALSSubtypeRelationship_object, domain=DiseaseHasALSSubtypeRelationship, range=Optional[Union[str, ALSSubtypeId]])

slots.DiseaseHasALSSubtypeRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DiseaseHasALSSubtypeRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DiseaseHasALSSubtypeRelationship_original_optimus_relationship_type, domain=DiseaseHasALSSubtypeRelationship, range=Optional[str])

slots.ALSSubtypeIsSubtypeOfDiseaseRelationship_subject = Slot(uri=ALSKG.subject, name="ALSSubtypeIsSubtypeOfDiseaseRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.ALSSubtypeIsSubtypeOfDiseaseRelationship_subject, domain=ALSSubtypeIsSubtypeOfDiseaseRelationship, range=Optional[Union[str, ALSSubtypeId]])

slots.ALSSubtypeIsSubtypeOfDiseaseRelationship_object = Slot(uri=ALSKG.object, name="ALSSubtypeIsSubtypeOfDiseaseRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.ALSSubtypeIsSubtypeOfDiseaseRelationship_object, domain=ALSSubtypeIsSubtypeOfDiseaseRelationship, range=Optional[Union[str, DiseaseId]])

slots.ALSSubtypeIsSubtypeOfDiseaseRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="ALSSubtypeIsSubtypeOfDiseaseRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.ALSSubtypeIsSubtypeOfDiseaseRelationship_original_optimus_relationship_type, domain=ALSSubtypeIsSubtypeOfDiseaseRelationship, range=Optional[str])

slots.ALSSubtypeHasSubtypeSchemeRelationship_subject = Slot(uri=ALSKG.subject, name="ALSSubtypeHasSubtypeSchemeRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.ALSSubtypeHasSubtypeSchemeRelationship_subject, domain=ALSSubtypeHasSubtypeSchemeRelationship, range=Optional[Union[str, ALSSubtypeId]])

slots.ALSSubtypeHasSubtypeSchemeRelationship_object = Slot(uri=ALSKG.object, name="ALSSubtypeHasSubtypeSchemeRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.ALSSubtypeHasSubtypeSchemeRelationship_object, domain=ALSSubtypeHasSubtypeSchemeRelationship, range=Optional[Union[str, SubtypeSchemeId]])

slots.ALSSubtypeHasSubtypeSchemeRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="ALSSubtypeHasSubtypeSchemeRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.ALSSubtypeHasSubtypeSchemeRelationship_original_optimus_relationship_type, domain=ALSSubtypeHasSubtypeSchemeRelationship, range=Optional[str])

slots.ALSSubtypeHasSubtypeCriterionRelationship_subject = Slot(uri=ALSKG.subject, name="ALSSubtypeHasSubtypeCriterionRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.ALSSubtypeHasSubtypeCriterionRelationship_subject, domain=ALSSubtypeHasSubtypeCriterionRelationship, range=Optional[Union[str, ALSSubtypeId]])

slots.ALSSubtypeHasSubtypeCriterionRelationship_object = Slot(uri=ALSKG.object, name="ALSSubtypeHasSubtypeCriterionRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.ALSSubtypeHasSubtypeCriterionRelationship_object, domain=ALSSubtypeHasSubtypeCriterionRelationship, range=Optional[Union[str, SubtypeCriterionId]])

slots.ALSSubtypeHasSubtypeCriterionRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="ALSSubtypeHasSubtypeCriterionRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.ALSSubtypeHasSubtypeCriterionRelationship_original_optimus_relationship_type, domain=ALSSubtypeHasSubtypeCriterionRelationship, range=Optional[str])

slots.ALSSubtypeDefinedByGeneRelationship_subject = Slot(uri=ALSKG.subject, name="ALSSubtypeDefinedByGeneRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.ALSSubtypeDefinedByGeneRelationship_subject, domain=ALSSubtypeDefinedByGeneRelationship, range=Optional[Union[str, ALSSubtypeId]])

slots.ALSSubtypeDefinedByGeneRelationship_object = Slot(uri=ALSKG.object, name="ALSSubtypeDefinedByGeneRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.ALSSubtypeDefinedByGeneRelationship_object, domain=ALSSubtypeDefinedByGeneRelationship, range=Optional[Union[str, GeneId]])

slots.ALSSubtypeDefinedByGeneRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="ALSSubtypeDefinedByGeneRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.ALSSubtypeDefinedByGeneRelationship_original_optimus_relationship_type, domain=ALSSubtypeDefinedByGeneRelationship, range=Optional[str])

slots.ALSSubtypeDefinedByVariantRelationship_subject = Slot(uri=ALSKG.subject, name="ALSSubtypeDefinedByVariantRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.ALSSubtypeDefinedByVariantRelationship_subject, domain=ALSSubtypeDefinedByVariantRelationship, range=Optional[Union[str, ALSSubtypeId]])

slots.ALSSubtypeDefinedByVariantRelationship_object = Slot(uri=ALSKG.object, name="ALSSubtypeDefinedByVariantRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.ALSSubtypeDefinedByVariantRelationship_object, domain=ALSSubtypeDefinedByVariantRelationship, range=Optional[Union[str, SequenceVariantId]])

slots.ALSSubtypeDefinedByVariantRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="ALSSubtypeDefinedByVariantRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.ALSSubtypeDefinedByVariantRelationship_original_optimus_relationship_type, domain=ALSSubtypeDefinedByVariantRelationship, range=Optional[str])

slots.ALSSubtypeHasPathogenicMechanismRelationship_subject = Slot(uri=ALSKG.subject, name="ALSSubtypeHasPathogenicMechanismRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.ALSSubtypeHasPathogenicMechanismRelationship_subject, domain=ALSSubtypeHasPathogenicMechanismRelationship, range=Optional[Union[str, ALSSubtypeId]])

slots.ALSSubtypeHasPathogenicMechanismRelationship_object = Slot(uri=ALSKG.object, name="ALSSubtypeHasPathogenicMechanismRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.ALSSubtypeHasPathogenicMechanismRelationship_object, domain=ALSSubtypeHasPathogenicMechanismRelationship, range=Optional[Union[str, PathogenicMechanismId]])

slots.ALSSubtypeHasPathogenicMechanismRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="ALSSubtypeHasPathogenicMechanismRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.ALSSubtypeHasPathogenicMechanismRelationship_original_optimus_relationship_type, domain=ALSSubtypeHasPathogenicMechanismRelationship, range=Optional[str])

slots.ALSSubtypeAffectsAnatomyRelationship_subject = Slot(uri=ALSKG.subject, name="ALSSubtypeAffectsAnatomyRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.ALSSubtypeAffectsAnatomyRelationship_subject, domain=ALSSubtypeAffectsAnatomyRelationship, range=Optional[Union[str, ALSSubtypeId]])

slots.ALSSubtypeAffectsAnatomyRelationship_object = Slot(uri=ALSKG.object, name="ALSSubtypeAffectsAnatomyRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.ALSSubtypeAffectsAnatomyRelationship_object, domain=ALSSubtypeAffectsAnatomyRelationship, range=Optional[Union[str, AnatomyId]])

slots.ALSSubtypeAffectsAnatomyRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="ALSSubtypeAffectsAnatomyRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.ALSSubtypeAffectsAnatomyRelationship_original_optimus_relationship_type, domain=ALSSubtypeAffectsAnatomyRelationship, range=Optional[str])

slots.ALSSubtypeInvolvesCellTypeRelationship_subject = Slot(uri=ALSKG.subject, name="ALSSubtypeInvolvesCellTypeRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.ALSSubtypeInvolvesCellTypeRelationship_subject, domain=ALSSubtypeInvolvesCellTypeRelationship, range=Optional[Union[str, ALSSubtypeId]])

slots.ALSSubtypeInvolvesCellTypeRelationship_object = Slot(uri=ALSKG.object, name="ALSSubtypeInvolvesCellTypeRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.ALSSubtypeInvolvesCellTypeRelationship_object, domain=ALSSubtypeInvolvesCellTypeRelationship, range=Optional[Union[str, CellTypeId]])

slots.ALSSubtypeInvolvesCellTypeRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="ALSSubtypeInvolvesCellTypeRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.ALSSubtypeInvolvesCellTypeRelationship_original_optimus_relationship_type, domain=ALSSubtypeInvolvesCellTypeRelationship, range=Optional[str])

slots.ALSSubtypeHasPhenotypeObservationRelationship_subject = Slot(uri=ALSKG.subject, name="ALSSubtypeHasPhenotypeObservationRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.ALSSubtypeHasPhenotypeObservationRelationship_subject, domain=ALSSubtypeHasPhenotypeObservationRelationship, range=Optional[Union[str, ALSSubtypeId]])

slots.ALSSubtypeHasPhenotypeObservationRelationship_object = Slot(uri=ALSKG.object, name="ALSSubtypeHasPhenotypeObservationRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.ALSSubtypeHasPhenotypeObservationRelationship_object, domain=ALSSubtypeHasPhenotypeObservationRelationship, range=Optional[Union[str, PhenotypeObservationId]])

slots.ALSSubtypeHasPhenotypeObservationRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="ALSSubtypeHasPhenotypeObservationRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.ALSSubtypeHasPhenotypeObservationRelationship_original_optimus_relationship_type, domain=ALSSubtypeHasPhenotypeObservationRelationship, range=Optional[str])

slots.GeneHasVariantRelationship_subject = Slot(uri=ALSKG.subject, name="GeneHasVariantRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.GeneHasVariantRelationship_subject, domain=GeneHasVariantRelationship, range=Optional[Union[str, GeneId]])

slots.GeneHasVariantRelationship_object = Slot(uri=ALSKG.object, name="GeneHasVariantRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.GeneHasVariantRelationship_object, domain=GeneHasVariantRelationship, range=Optional[Union[str, SequenceVariantId]])

slots.GeneHasVariantRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="GeneHasVariantRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.GeneHasVariantRelationship_original_optimus_relationship_type, domain=GeneHasVariantRelationship, range=Optional[str])

slots.VariantAffectsGeneRelationship_subject = Slot(uri=ALSKG.subject, name="VariantAffectsGeneRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.VariantAffectsGeneRelationship_subject, domain=VariantAffectsGeneRelationship, range=Optional[Union[str, SequenceVariantId]])

slots.VariantAffectsGeneRelationship_object = Slot(uri=ALSKG.object, name="VariantAffectsGeneRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.VariantAffectsGeneRelationship_object, domain=VariantAffectsGeneRelationship, range=Optional[Union[str, GeneId]])

slots.VariantAffectsGeneRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="VariantAffectsGeneRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.VariantAffectsGeneRelationship_original_optimus_relationship_type, domain=VariantAffectsGeneRelationship, range=Optional[str])

slots.VariantAltersProteinRelationship_subject = Slot(uri=ALSKG.subject, name="VariantAltersProteinRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.VariantAltersProteinRelationship_subject, domain=VariantAltersProteinRelationship, range=Optional[Union[str, SequenceVariantId]])

slots.VariantAltersProteinRelationship_object = Slot(uri=ALSKG.object, name="VariantAltersProteinRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.VariantAltersProteinRelationship_object, domain=VariantAltersProteinRelationship, range=Optional[Union[str, ProteinId]])

slots.VariantAltersProteinRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="VariantAltersProteinRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.VariantAltersProteinRelationship_original_optimus_relationship_type, domain=VariantAltersProteinRelationship, range=Optional[str])

slots.GeneContributesToPathogenicMechanismRelationship_subject = Slot(uri=ALSKG.subject, name="GeneContributesToPathogenicMechanismRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.GeneContributesToPathogenicMechanismRelationship_subject, domain=GeneContributesToPathogenicMechanismRelationship, range=Optional[Union[str, GeneId]])

slots.GeneContributesToPathogenicMechanismRelationship_object = Slot(uri=ALSKG.object, name="GeneContributesToPathogenicMechanismRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.GeneContributesToPathogenicMechanismRelationship_object, domain=GeneContributesToPathogenicMechanismRelationship, range=Optional[Union[str, PathogenicMechanismId]])

slots.GeneContributesToPathogenicMechanismRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="GeneContributesToPathogenicMechanismRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.GeneContributesToPathogenicMechanismRelationship_original_optimus_relationship_type, domain=GeneContributesToPathogenicMechanismRelationship, range=Optional[str])

slots.ProteinContributesToPathogenicMechanismRelationship_subject = Slot(uri=ALSKG.subject, name="ProteinContributesToPathogenicMechanismRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.ProteinContributesToPathogenicMechanismRelationship_subject, domain=ProteinContributesToPathogenicMechanismRelationship, range=Optional[Union[str, ProteinId]])

slots.ProteinContributesToPathogenicMechanismRelationship_object = Slot(uri=ALSKG.object, name="ProteinContributesToPathogenicMechanismRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.ProteinContributesToPathogenicMechanismRelationship_object, domain=ProteinContributesToPathogenicMechanismRelationship, range=Optional[Union[str, PathogenicMechanismId]])

slots.ProteinContributesToPathogenicMechanismRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="ProteinContributesToPathogenicMechanismRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.ProteinContributesToPathogenicMechanismRelationship_original_optimus_relationship_type, domain=ProteinContributesToPathogenicMechanismRelationship, range=Optional[str])

slots.MolecularEventContributesToPathogenicMechanismRelationship_subject = Slot(uri=ALSKG.subject, name="MolecularEventContributesToPathogenicMechanismRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.MolecularEventContributesToPathogenicMechanismRelationship_subject, domain=MolecularEventContributesToPathogenicMechanismRelationship, range=Optional[Union[str, MolecularEventId]])

slots.MolecularEventContributesToPathogenicMechanismRelationship_object = Slot(uri=ALSKG.object, name="MolecularEventContributesToPathogenicMechanismRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.MolecularEventContributesToPathogenicMechanismRelationship_object, domain=MolecularEventContributesToPathogenicMechanismRelationship, range=Optional[Union[str, PathogenicMechanismId]])

slots.MolecularEventContributesToPathogenicMechanismRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="MolecularEventContributesToPathogenicMechanismRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.MolecularEventContributesToPathogenicMechanismRelationship_original_optimus_relationship_type, domain=MolecularEventContributesToPathogenicMechanismRelationship, range=Optional[str])

slots.PathogenicMechanismOccursInCellTypeRelationship_subject = Slot(uri=ALSKG.subject, name="PathogenicMechanismOccursInCellTypeRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.PathogenicMechanismOccursInCellTypeRelationship_subject, domain=PathogenicMechanismOccursInCellTypeRelationship, range=Optional[Union[str, PathogenicMechanismId]])

slots.PathogenicMechanismOccursInCellTypeRelationship_object = Slot(uri=ALSKG.object, name="PathogenicMechanismOccursInCellTypeRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.PathogenicMechanismOccursInCellTypeRelationship_object, domain=PathogenicMechanismOccursInCellTypeRelationship, range=Optional[Union[str, CellTypeId]])

slots.PathogenicMechanismOccursInCellTypeRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="PathogenicMechanismOccursInCellTypeRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.PathogenicMechanismOccursInCellTypeRelationship_original_optimus_relationship_type, domain=PathogenicMechanismOccursInCellTypeRelationship, range=Optional[str])

slots.PathogenicMechanismOccursInAnatomyRelationship_subject = Slot(uri=ALSKG.subject, name="PathogenicMechanismOccursInAnatomyRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.PathogenicMechanismOccursInAnatomyRelationship_subject, domain=PathogenicMechanismOccursInAnatomyRelationship, range=Optional[Union[str, PathogenicMechanismId]])

slots.PathogenicMechanismOccursInAnatomyRelationship_object = Slot(uri=ALSKG.object, name="PathogenicMechanismOccursInAnatomyRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.PathogenicMechanismOccursInAnatomyRelationship_object, domain=PathogenicMechanismOccursInAnatomyRelationship, range=Optional[Union[str, AnatomyId]])

slots.PathogenicMechanismOccursInAnatomyRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="PathogenicMechanismOccursInAnatomyRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.PathogenicMechanismOccursInAnatomyRelationship_original_optimus_relationship_type, domain=PathogenicMechanismOccursInAnatomyRelationship, range=Optional[str])

slots.DifferentialExpressionMeasuresGeneRelationship_subject = Slot(uri=ALSKG.subject, name="DifferentialExpressionMeasuresGeneRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DifferentialExpressionMeasuresGeneRelationship_subject, domain=DifferentialExpressionMeasuresGeneRelationship, range=Optional[Union[str, DifferentialExpressionStatementId]])

slots.DifferentialExpressionMeasuresGeneRelationship_object = Slot(uri=ALSKG.object, name="DifferentialExpressionMeasuresGeneRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DifferentialExpressionMeasuresGeneRelationship_object, domain=DifferentialExpressionMeasuresGeneRelationship, range=Optional[Union[str, GeneId]])

slots.DifferentialExpressionMeasuresGeneRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DifferentialExpressionMeasuresGeneRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DifferentialExpressionMeasuresGeneRelationship_original_optimus_relationship_type, domain=DifferentialExpressionMeasuresGeneRelationship, range=Optional[str])

slots.DifferentialExpressionOccursInSubtypeRelationship_subject = Slot(uri=ALSKG.subject, name="DifferentialExpressionOccursInSubtypeRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DifferentialExpressionOccursInSubtypeRelationship_subject, domain=DifferentialExpressionOccursInSubtypeRelationship, range=Optional[Union[str, DifferentialExpressionStatementId]])

slots.DifferentialExpressionOccursInSubtypeRelationship_object = Slot(uri=ALSKG.object, name="DifferentialExpressionOccursInSubtypeRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DifferentialExpressionOccursInSubtypeRelationship_object, domain=DifferentialExpressionOccursInSubtypeRelationship, range=Optional[Union[str, ALSSubtypeId]])

slots.DifferentialExpressionOccursInSubtypeRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DifferentialExpressionOccursInSubtypeRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DifferentialExpressionOccursInSubtypeRelationship_original_optimus_relationship_type, domain=DifferentialExpressionOccursInSubtypeRelationship, range=Optional[str])

slots.DifferentialExpressionOccursInAnatomyRelationship_subject = Slot(uri=ALSKG.subject, name="DifferentialExpressionOccursInAnatomyRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DifferentialExpressionOccursInAnatomyRelationship_subject, domain=DifferentialExpressionOccursInAnatomyRelationship, range=Optional[Union[str, DifferentialExpressionStatementId]])

slots.DifferentialExpressionOccursInAnatomyRelationship_object = Slot(uri=ALSKG.object, name="DifferentialExpressionOccursInAnatomyRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DifferentialExpressionOccursInAnatomyRelationship_object, domain=DifferentialExpressionOccursInAnatomyRelationship, range=Optional[Union[str, AnatomyId]])

slots.DifferentialExpressionOccursInAnatomyRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DifferentialExpressionOccursInAnatomyRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DifferentialExpressionOccursInAnatomyRelationship_original_optimus_relationship_type, domain=DifferentialExpressionOccursInAnatomyRelationship, range=Optional[str])

slots.DifferentialExpressionOccursInCellTypeRelationship_subject = Slot(uri=ALSKG.subject, name="DifferentialExpressionOccursInCellTypeRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DifferentialExpressionOccursInCellTypeRelationship_subject, domain=DifferentialExpressionOccursInCellTypeRelationship, range=Optional[Union[str, DifferentialExpressionStatementId]])

slots.DifferentialExpressionOccursInCellTypeRelationship_object = Slot(uri=ALSKG.object, name="DifferentialExpressionOccursInCellTypeRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DifferentialExpressionOccursInCellTypeRelationship_object, domain=DifferentialExpressionOccursInCellTypeRelationship, range=Optional[Union[str, CellTypeId]])

slots.DifferentialExpressionOccursInCellTypeRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DifferentialExpressionOccursInCellTypeRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DifferentialExpressionOccursInCellTypeRelationship_original_optimus_relationship_type, domain=DifferentialExpressionOccursInCellTypeRelationship, range=Optional[str])

slots.DifferentialExpressionMeasuredByAssayRelationship_subject = Slot(uri=ALSKG.subject, name="DifferentialExpressionMeasuredByAssayRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DifferentialExpressionMeasuredByAssayRelationship_subject, domain=DifferentialExpressionMeasuredByAssayRelationship, range=Optional[Union[str, DifferentialExpressionStatementId]])

slots.DifferentialExpressionMeasuredByAssayRelationship_object = Slot(uri=ALSKG.object, name="DifferentialExpressionMeasuredByAssayRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DifferentialExpressionMeasuredByAssayRelationship_object, domain=DifferentialExpressionMeasuredByAssayRelationship, range=Optional[Union[str, AssayId]])

slots.DifferentialExpressionMeasuredByAssayRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DifferentialExpressionMeasuredByAssayRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DifferentialExpressionMeasuredByAssayRelationship_original_optimus_relationship_type, domain=DifferentialExpressionMeasuredByAssayRelationship, range=Optional[str])

slots.DifferentialExpressionDerivedFromDatasetRelationship_subject = Slot(uri=ALSKG.subject, name="DifferentialExpressionDerivedFromDatasetRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DifferentialExpressionDerivedFromDatasetRelationship_subject, domain=DifferentialExpressionDerivedFromDatasetRelationship, range=Optional[Union[str, DifferentialExpressionStatementId]])

slots.DifferentialExpressionDerivedFromDatasetRelationship_object = Slot(uri=ALSKG.object, name="DifferentialExpressionDerivedFromDatasetRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DifferentialExpressionDerivedFromDatasetRelationship_object, domain=DifferentialExpressionDerivedFromDatasetRelationship, range=Optional[Union[str, DatasetId]])

slots.DifferentialExpressionDerivedFromDatasetRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DifferentialExpressionDerivedFromDatasetRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DifferentialExpressionDerivedFromDatasetRelationship_original_optimus_relationship_type, domain=DifferentialExpressionDerivedFromDatasetRelationship, range=Optional[str])

slots.EvidenceStatementSupportedByEvidenceRelationship_subject = Slot(uri=ALSKG.subject, name="EvidenceStatementSupportedByEvidenceRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.EvidenceStatementSupportedByEvidenceRelationship_subject, domain=EvidenceStatementSupportedByEvidenceRelationship, range=Optional[Union[str, EvidenceStatementId]])

slots.EvidenceStatementSupportedByEvidenceRelationship_object = Slot(uri=ALSKG.object, name="EvidenceStatementSupportedByEvidenceRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.EvidenceStatementSupportedByEvidenceRelationship_object, domain=EvidenceStatementSupportedByEvidenceRelationship, range=Optional[Union[str, EvidenceRecordId]])

slots.EvidenceStatementSupportedByEvidenceRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="EvidenceStatementSupportedByEvidenceRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.EvidenceStatementSupportedByEvidenceRelationship_original_optimus_relationship_type, domain=EvidenceStatementSupportedByEvidenceRelationship, range=Optional[str])

slots.EvidenceStatementDerivedFromDatasetRelationship_subject = Slot(uri=ALSKG.subject, name="EvidenceStatementDerivedFromDatasetRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.EvidenceStatementDerivedFromDatasetRelationship_subject, domain=EvidenceStatementDerivedFromDatasetRelationship, range=Optional[Union[str, EvidenceStatementId]])

slots.EvidenceStatementDerivedFromDatasetRelationship_object = Slot(uri=ALSKG.object, name="EvidenceStatementDerivedFromDatasetRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.EvidenceStatementDerivedFromDatasetRelationship_object, domain=EvidenceStatementDerivedFromDatasetRelationship, range=Optional[Union[str, DatasetId]])

slots.EvidenceStatementDerivedFromDatasetRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="EvidenceStatementDerivedFromDatasetRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.EvidenceStatementDerivedFromDatasetRelationship_original_optimus_relationship_type, domain=EvidenceStatementDerivedFromDatasetRelationship, range=Optional[str])

slots.PhenotypeObservationHasObservedPhenotypeRelationship_subject = Slot(uri=ALSKG.subject, name="PhenotypeObservationHasObservedPhenotypeRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.PhenotypeObservationHasObservedPhenotypeRelationship_subject, domain=PhenotypeObservationHasObservedPhenotypeRelationship, range=Optional[Union[str, PhenotypeObservationId]])

slots.PhenotypeObservationHasObservedPhenotypeRelationship_object = Slot(uri=ALSKG.object, name="PhenotypeObservationHasObservedPhenotypeRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.PhenotypeObservationHasObservedPhenotypeRelationship_object, domain=PhenotypeObservationHasObservedPhenotypeRelationship, range=Optional[Union[str, PhenotypeId]])

slots.PhenotypeObservationHasObservedPhenotypeRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="PhenotypeObservationHasObservedPhenotypeRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.PhenotypeObservationHasObservedPhenotypeRelationship_original_optimus_relationship_type, domain=PhenotypeObservationHasObservedPhenotypeRelationship, range=Optional[str])

slots.PhenotypeObservationOccursInSubtypeRelationship_subject = Slot(uri=ALSKG.subject, name="PhenotypeObservationOccursInSubtypeRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.PhenotypeObservationOccursInSubtypeRelationship_subject, domain=PhenotypeObservationOccursInSubtypeRelationship, range=Optional[Union[str, PhenotypeObservationId]])

slots.PhenotypeObservationOccursInSubtypeRelationship_object = Slot(uri=ALSKG.object, name="PhenotypeObservationOccursInSubtypeRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.PhenotypeObservationOccursInSubtypeRelationship_object, domain=PhenotypeObservationOccursInSubtypeRelationship, range=Optional[Union[str, ALSSubtypeId]])

slots.PhenotypeObservationOccursInSubtypeRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="PhenotypeObservationOccursInSubtypeRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.PhenotypeObservationOccursInSubtypeRelationship_original_optimus_relationship_type, domain=PhenotypeObservationOccursInSubtypeRelationship, range=Optional[str])

slots.BiomarkerIndicatesPathogenicMechanismRelationship_subject = Slot(uri=ALSKG.subject, name="BiomarkerIndicatesPathogenicMechanismRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.BiomarkerIndicatesPathogenicMechanismRelationship_subject, domain=BiomarkerIndicatesPathogenicMechanismRelationship, range=Optional[Union[str, BiomarkerId]])

slots.BiomarkerIndicatesPathogenicMechanismRelationship_object = Slot(uri=ALSKG.object, name="BiomarkerIndicatesPathogenicMechanismRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.BiomarkerIndicatesPathogenicMechanismRelationship_object, domain=BiomarkerIndicatesPathogenicMechanismRelationship, range=Optional[Union[str, PathogenicMechanismId]])

slots.BiomarkerIndicatesPathogenicMechanismRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="BiomarkerIndicatesPathogenicMechanismRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.BiomarkerIndicatesPathogenicMechanismRelationship_original_optimus_relationship_type, domain=BiomarkerIndicatesPathogenicMechanismRelationship, range=Optional[str])

slots.DrugRepurposingHypothesisPrioritizesDrugRelationship_subject = Slot(uri=ALSKG.subject, name="DrugRepurposingHypothesisPrioritizesDrugRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugRepurposingHypothesisPrioritizesDrugRelationship_subject, domain=DrugRepurposingHypothesisPrioritizesDrugRelationship, range=Optional[Union[str, DrugRepurposingHypothesisId]])

slots.DrugRepurposingHypothesisPrioritizesDrugRelationship_object = Slot(uri=ALSKG.object, name="DrugRepurposingHypothesisPrioritizesDrugRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugRepurposingHypothesisPrioritizesDrugRelationship_object, domain=DrugRepurposingHypothesisPrioritizesDrugRelationship, range=Optional[Union[str, DrugId]])

slots.DrugRepurposingHypothesisPrioritizesDrugRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugRepurposingHypothesisPrioritizesDrugRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugRepurposingHypothesisPrioritizesDrugRelationship_original_optimus_relationship_type, domain=DrugRepurposingHypothesisPrioritizesDrugRelationship, range=Optional[str])

slots.DrugRepurposingHypothesisTargetsGeneRelationship_subject = Slot(uri=ALSKG.subject, name="DrugRepurposingHypothesisTargetsGeneRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugRepurposingHypothesisTargetsGeneRelationship_subject, domain=DrugRepurposingHypothesisTargetsGeneRelationship, range=Optional[Union[str, DrugRepurposingHypothesisId]])

slots.DrugRepurposingHypothesisTargetsGeneRelationship_object = Slot(uri=ALSKG.object, name="DrugRepurposingHypothesisTargetsGeneRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugRepurposingHypothesisTargetsGeneRelationship_object, domain=DrugRepurposingHypothesisTargetsGeneRelationship, range=Optional[Union[str, GeneId]])

slots.DrugRepurposingHypothesisTargetsGeneRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugRepurposingHypothesisTargetsGeneRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugRepurposingHypothesisTargetsGeneRelationship_original_optimus_relationship_type, domain=DrugRepurposingHypothesisTargetsGeneRelationship, range=Optional[str])

slots.DrugRepurposingHypothesisModulatesPathogenicMechanismRelationship_subject = Slot(uri=ALSKG.subject, name="DrugRepurposingHypothesisModulatesPathogenicMechanismRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.DrugRepurposingHypothesisModulatesPathogenicMechanismRelationship_subject, domain=DrugRepurposingHypothesisModulatesPathogenicMechanismRelationship, range=Optional[Union[str, DrugRepurposingHypothesisId]])

slots.DrugRepurposingHypothesisModulatesPathogenicMechanismRelationship_object = Slot(uri=ALSKG.object, name="DrugRepurposingHypothesisModulatesPathogenicMechanismRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.DrugRepurposingHypothesisModulatesPathogenicMechanismRelationship_object, domain=DrugRepurposingHypothesisModulatesPathogenicMechanismRelationship, range=Optional[Union[str, PathogenicMechanismId]])

slots.DrugRepurposingHypothesisModulatesPathogenicMechanismRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="DrugRepurposingHypothesisModulatesPathogenicMechanismRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.DrugRepurposingHypothesisModulatesPathogenicMechanismRelationship_original_optimus_relationship_type, domain=DrugRepurposingHypothesisModulatesPathogenicMechanismRelationship, range=Optional[str])

slots.TherapeuticInterventionTestedInClinicalTrialRelationship_subject = Slot(uri=ALSKG.subject, name="TherapeuticInterventionTestedInClinicalTrialRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.TherapeuticInterventionTestedInClinicalTrialRelationship_subject, domain=TherapeuticInterventionTestedInClinicalTrialRelationship, range=Optional[Union[str, TherapeuticInterventionId]])

slots.TherapeuticInterventionTestedInClinicalTrialRelationship_object = Slot(uri=ALSKG.object, name="TherapeuticInterventionTestedInClinicalTrialRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.TherapeuticInterventionTestedInClinicalTrialRelationship_object, domain=TherapeuticInterventionTestedInClinicalTrialRelationship, range=Optional[Union[str, ClinicalTrialId]])

slots.TherapeuticInterventionTestedInClinicalTrialRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="TherapeuticInterventionTestedInClinicalTrialRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.TherapeuticInterventionTestedInClinicalTrialRelationship_original_optimus_relationship_type, domain=TherapeuticInterventionTestedInClinicalTrialRelationship, range=Optional[str])

slots.ClinicalTrialEnrollsSubtypeRelationship_subject = Slot(uri=ALSKG.subject, name="ClinicalTrialEnrollsSubtypeRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.ClinicalTrialEnrollsSubtypeRelationship_subject, domain=ClinicalTrialEnrollsSubtypeRelationship, range=Optional[Union[str, ClinicalTrialId]])

slots.ClinicalTrialEnrollsSubtypeRelationship_object = Slot(uri=ALSKG.object, name="ClinicalTrialEnrollsSubtypeRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.ClinicalTrialEnrollsSubtypeRelationship_object, domain=ClinicalTrialEnrollsSubtypeRelationship, range=Optional[Union[str, ALSSubtypeId]])

slots.ClinicalTrialEnrollsSubtypeRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="ClinicalTrialEnrollsSubtypeRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.ClinicalTrialEnrollsSubtypeRelationship_original_optimus_relationship_type, domain=ClinicalTrialEnrollsSubtypeRelationship, range=Optional[str])

slots.ModelSystemModelsSubtypeRelationship_subject = Slot(uri=ALSKG.subject, name="ModelSystemModelsSubtypeRelationship_subject", curie=ALSKG.curie('subject'),
                   model_uri=ALSKG.ModelSystemModelsSubtypeRelationship_subject, domain=ModelSystemModelsSubtypeRelationship, range=Optional[Union[str, ModelSystemId]])

slots.ModelSystemModelsSubtypeRelationship_object = Slot(uri=ALSKG.object, name="ModelSystemModelsSubtypeRelationship_object", curie=ALSKG.curie('object'),
                   model_uri=ALSKG.ModelSystemModelsSubtypeRelationship_object, domain=ModelSystemModelsSubtypeRelationship, range=Optional[Union[str, ALSSubtypeId]])

slots.ModelSystemModelsSubtypeRelationship_original_optimus_relationship_type = Slot(uri=ALSKG.original_optimus_relationship_type, name="ModelSystemModelsSubtypeRelationship_original_optimus_relationship_type", curie=ALSKG.curie('original_optimus_relationship_type'),
                   model_uri=ALSKG.ModelSystemModelsSubtypeRelationship_original_optimus_relationship_type, domain=ModelSystemModelsSubtypeRelationship, range=Optional[str])
