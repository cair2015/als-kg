# Auto generated from als_kg.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-04-28T14:41:28
# Schema: als_kg
#
# id: https://alskb.org/ontology/als_kg
# description: Comprehensive ontology model for the ALS Knowledge Graph (ALS-KG). Uses a local default namespace for ALS-specific classes and slots, explicit Biolink/ontology URIs only for externally defined concepts and predicates, direct object properties for canonical KG edges, and optional evidence-bearing association classes for provenance-rich statements.
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

from linkml_runtime.linkml_model.types import Boolean, Date, Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = "2.1.2"

# Namespaces
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
CAS = CurieNamespace('CAS', 'https://commonchemistry.cas.org/detail?cas_rn=')
CTD = CurieNamespace('CTD', 'http://ctdbase.org/detail.go?type=chem&acc=')
CHEMBL = CurieNamespace('ChEMBL', 'https://www.ebi.ac.uk/chembl/compound_report_card/')
CLINVAR = CurieNamespace('ClinVar', 'https://www.ncbi.nlm.nih.gov/clinvar/variation/')
DOI = CurieNamespace('DOI', 'https://doi.org/')
DRUGBANK = CurieNamespace('DrugBank', 'https://www.drugbank.ca/drugs/')
ECO = CurieNamespace('ECO', 'http://purl.obolibrary.org/obo/ECO_')
ENSEMBL = CurieNamespace('ENSEMBL', 'https://identifiers.org/ensembl/')
GO = CurieNamespace('GO', 'http://purl.obolibrary.org/obo/GO_')
HGNC = CurieNamespace('HGNC', 'https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/')
HP = CurieNamespace('HP', 'http://purl.obolibrary.org/obo/HP_')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
ICD10CM = CurieNamespace('ICD10CM', 'https://icd.codes/icd10cm/')
MONDO = CurieNamespace('MONDO', 'http://purl.obolibrary.org/obo/MONDO_')
MESH = CurieNamespace('MeSH', 'https://id.nlm.nih.gov/mesh/')
NCBIGENE = CurieNamespace('NCBIGene', 'https://www.ncbi.nlm.nih.gov/gene/')
OMIM = CurieNamespace('OMIM', 'https://omim.org/entry/')
ORPHANET = CurieNamespace('ORPHANET', 'http://www.orpha.net/ORDO/Orphanet_')
PMID = CurieNamespace('PMID', 'https://pubmed.ncbi.nlm.nih.gov/')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
REACTOME = CurieNamespace('Reactome', 'https://identifiers.org/reactome/')
SIO = CurieNamespace('SIO', 'http://semanticscience.org/resource/')
UBERON = CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_')
UMLS = CurieNamespace('UMLS', 'https://uts.nlm.nih.gov/uts/umls/concept/')
UNIPROTKB = CurieNamespace('UniProtKB', 'https://www.uniprot.org/uniprot/')
ALSKB = CurieNamespace('alskb', 'https://cair2015.github.io/als-kg/elements/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
DBSNP = CurieNamespace('dbSNP', 'https://www.ncbi.nlm.nih.gov/snp/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OBO = CurieNamespace('obo', 'http://purl.obolibrary.org/obo/')
OBOINOWL = CurieNamespace('oboInOwl', 'http://www.geneontology.org/formats/oboInOwl#')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = ALSKB


# Types
class MondoIdentifier(String):
    """ MONDO disease ontology identifier (e.g. MONDO:0007743) """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "MondoIdentifier"
    type_model_uri = ALSKB.MondoIdentifier


class HpoIdentifier(String):
    """ HPO phenotype term identifier (e.g. HP:0007354) """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "HpoIdentifier"
    type_model_uri = ALSKB.HpoIdentifier


class UberonIdentifier(String):
    """ UBERON anatomy ontology identifier """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "UberonIdentifier"
    type_model_uri = ALSKB.UberonIdentifier


class NcbiGeneIdentifier(String):
    """ NCBI Entrez Gene numeric ID """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "NcbiGeneIdentifier"
    type_model_uri = ALSKB.NcbiGeneIdentifier


class UniprotIdentifier(String):
    """ UniProt accession identifier """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "UniprotIdentifier"
    type_model_uri = ALSKB.UniprotIdentifier


class ClinvarIdentifier(String):
    """ ClinVar variation numeric ID """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "ClinvarIdentifier"
    type_model_uri = ALSKB.ClinvarIdentifier


class DrugBankIdentifier(String):
    """ DrugBank primary identifier (e.g. DB00533) """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "DrugBankIdentifier"
    type_model_uri = ALSKB.DrugBankIdentifier


class GoIdentifier(String):
    """ Gene Ontology term identifier (e.g. GO:0006810) """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "GoIdentifier"
    type_model_uri = ALSKB.GoIdentifier


class ReactomeIdentifier(String):
    """ Reactome stable pathway identifier as a CURIE (e.g. Reactome:R-HSA-5673001) """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "ReactomeIdentifier"
    type_model_uri = ALSKB.ReactomeIdentifier


class CtdIdentifier(String):
    """ CTD chemical/stressor identifier """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "CtdIdentifier"
    type_model_uri = ALSKB.CtdIdentifier


# Class references
class DiseaseMondoId(MondoIdentifier):
    pass


class PhenotypeHpoId(HpoIdentifier):
    pass


class AnatomyUberonId(UberonIdentifier):
    pass


class GeneNcbiGeneId(NcbiGeneIdentifier):
    pass


class TranscriptionFactorNcbiGeneId(GeneNcbiGeneId):
    pass


class ProteinUniprotId(UniprotIdentifier):
    pass


class VariantClinvarId(ClinvarIdentifier):
    pass


class DrugDrugbankId(DrugBankIdentifier):
    pass


class ExposureOrStressorCtdId(CtdIdentifier):
    pass


class BiologicalProcessGoId(GoIdentifier):
    pass


class MolecularFunctionGoId(GoIdentifier):
    pass


class CellularComponentGoId(GoIdentifier):
    pass


class PathwayReactomeId(ReactomeIdentifier):
    pass


class DiseaseSubtypeMondoId(DiseaseMondoId):
    pass


@dataclass(repr=False)
class NamedEntity(YAMLRoot):
    """
    Root class for all named entities in the ALS-KG ontology. Provides core ontology metadata (id, label, definition,
    synonyms, xrefs).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["NamedThing"]
    class_class_curie: ClassVar[str] = "biolink:NamedThing"
    class_name: ClassVar[str] = "NamedEntity"
    class_model_uri: ClassVar[URIRef] = ALSKB.NamedEntity

    id: str = None
    label: str = None
    definition: Optional[str] = None
    synonym: Optional[str] = None
    xref: Optional[str] = None
    comment: Optional[str] = None
    is_obsolete: Optional[str] = "false"
    source: Optional[str] = None
    last_updated: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, str):
            self.id = str(self.id)

        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, str):
            self.label = str(self.label)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.synonym is not None and not isinstance(self.synonym, str):
            self.synonym = str(self.synonym)

        if self.xref is not None and not isinstance(self.xref, str):
            self.xref = str(self.xref)

        if self.comment is not None and not isinstance(self.comment, str):
            self.comment = str(self.comment)

        if self.is_obsolete is not None and not isinstance(self.is_obsolete, str):
            self.is_obsolete = str(self.is_obsolete)

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        if self.last_updated is not None and not isinstance(self.last_updated, str):
            self.last_updated = str(self.last_updated)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OntologyClass(NamedEntity):
    """
    Abstract base for entity classes (nodes in knowledge graph). Inherits from NamedEntity with semantic web
    compatible metadata.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL["Class"]
    class_class_curie: ClassVar[str] = "owl:Class"
    class_name: ClassVar[str] = "OntologyClass"
    class_model_uri: ClassVar[URIRef] = ALSKB.OntologyClass

    id: str = None
    label: str = None
    source_version: Optional[str] = None
    ingest_date: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.source_version is not None and not isinstance(self.source_version, str):
            self.source_version = str(self.source_version)

        if self.ingest_date is not None and not isinstance(self.ingest_date, str):
            self.ingest_date = str(self.ingest_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Relationship(YAMLRoot):
    """
    Abstract base for reified relationships (edges with explicit properties). Follows RDF triple pattern: subject,
    predicate, object. Can carry additional metadata (confidence, evidence, provenance).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RDF["Statement"]
    class_class_curie: ClassVar[str] = "rdf:Statement"
    class_name: ClassVar[str] = "Relationship"
    class_model_uri: ClassVar[URIRef] = ALSKB.Relationship

    subject: str = None
    predicate: str = None
    object: str = None
    source: Optional[str] = None
    confidence: Optional[str] = None
    evidence_type: Optional[str] = None
    evidence_source: Optional[str] = None
    ingest_date: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, str):
            self.subject = str(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, str):
            self.object = str(self.object)

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        if self.confidence is not None and not isinstance(self.confidence, str):
            self.confidence = str(self.confidence)

        if self.evidence_type is not None and not isinstance(self.evidence_type, str):
            self.evidence_type = str(self.evidence_type)

        if self.evidence_source is not None and not isinstance(self.evidence_source, str):
            self.evidence_source = str(self.evidence_source)

        if self.ingest_date is not None and not isinstance(self.ingest_date, str):
            self.ingest_date = str(self.ingest_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DiseaseOrPhenotype(OntologyClass):
    """
    Abstract parent class for all disease/phenotype entities. Following MONDO and HPO ontology patterns.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["DiseaseOrPhenotypicFeature"]
    class_class_curie: ClassVar[str] = "biolink:DiseaseOrPhenotypicFeature"
    class_name: ClassVar[str] = "DiseaseOrPhenotype"
    class_model_uri: ClassVar[URIRef] = ALSKB.DiseaseOrPhenotype

    id: str = None
    label: str = None
    mondo_id: Optional[Union[str, MondoIdentifier]] = None
    hpo_id: Optional[Union[str, HpoIdentifier]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.mondo_id is not None and not isinstance(self.mondo_id, MondoIdentifier):
            self.mondo_id = MondoIdentifier(self.mondo_id)

        if self.hpo_id is not None and not isinstance(self.hpo_id, HpoIdentifier):
            self.hpo_id = HpoIdentifier(self.hpo_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Disease(DiseaseOrPhenotype):
    """
    Disease entity. Encompasses ALS (MONDO:0007743), related neurodegenerative disorders (FTD, PLS, PMA, SMA), and
    comorbidities. Follows MONDO disease hierarchy via is_a relationships.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Disease"]
    class_class_curie: ClassVar[str] = "biolink:Disease"
    class_name: ClassVar[str] = "Disease"
    class_model_uri: ClassVar[URIRef] = ALSKB.Disease

    mondo_id: Union[str, DiseaseMondoId] = None
    id: str = None
    label: str = None
    name: Optional[str] = None
    disease_type: Optional[Union[str, "DiseaseTypeEnum"]] = None
    onset_type: Optional[Union[str, "OnsetTypeEnum"]] = None
    umls_cui: Optional[str] = None
    omim_id: Optional[str] = None
    orphanet_id: Optional[str] = None
    icd10_code: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.mondo_id):
            self.MissingRequiredField("mondo_id")
        if not isinstance(self.mondo_id, DiseaseMondoId):
            self.mondo_id = DiseaseMondoId(self.mondo_id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.disease_type is not None and not isinstance(self.disease_type, DiseaseTypeEnum):
            self.disease_type = DiseaseTypeEnum(self.disease_type)

        if self.onset_type is not None and not isinstance(self.onset_type, OnsetTypeEnum):
            self.onset_type = OnsetTypeEnum(self.onset_type)

        if self.umls_cui is not None and not isinstance(self.umls_cui, str):
            self.umls_cui = str(self.umls_cui)

        if self.omim_id is not None and not isinstance(self.omim_id, str):
            self.omim_id = str(self.omim_id)

        if self.orphanet_id is not None and not isinstance(self.orphanet_id, str):
            self.orphanet_id = str(self.orphanet_id)

        if self.icd10_code is not None and not isinstance(self.icd10_code, str):
            self.icd10_code = str(self.icd10_code)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Phenotype(DiseaseOrPhenotype):
    """
    Phenotypic feature (HPO term). Represents observable/measurable characteristics associated with diseases. Distinct
    from drug side effects which are modeled via DrugCausesPhenotype relationships.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["PhenotypicFeature"]
    class_class_curie: ClassVar[str] = "biolink:PhenotypicFeature"
    class_name: ClassVar[str] = "Phenotype"
    class_model_uri: ClassVar[URIRef] = ALSKB.Phenotype

    hpo_id: Union[str, PhenotypeHpoId] = None
    id: str = None
    label: str = None
    frequency: Optional[str] = None
    severity: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.hpo_id):
            self.MissingRequiredField("hpo_id")
        if not isinstance(self.hpo_id, PhenotypeHpoId):
            self.hpo_id = PhenotypeHpoId(self.hpo_id)

        if self.frequency is not None and not isinstance(self.frequency, str):
            self.frequency = str(self.frequency)

        if self.severity is not None and not isinstance(self.severity, str):
            self.severity = str(self.severity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Anatomy(OntologyClass):
    """
    Anatomical structure (UBERON ontology). ALS-specific relevance: motor cortex, spinal cord, anterior horn cells,
    neuromuscular junction. Linked to gene expression and disease manifestation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["AnatomicalEntity"]
    class_class_curie: ClassVar[str] = "biolink:AnatomicalEntity"
    class_name: ClassVar[str] = "Anatomy"
    class_model_uri: ClassVar[URIRef] = ALSKB.Anatomy

    uberon_id: Union[str, AnatomyUberonId] = None
    id: str = None
    label: str = None
    bto_id: Optional[str] = None
    mesh_id: Optional[str] = None
    anatomical_system: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uberon_id):
            self.MissingRequiredField("uberon_id")
        if not isinstance(self.uberon_id, AnatomyUberonId):
            self.uberon_id = AnatomyUberonId(self.uberon_id)

        if self.bto_id is not None and not isinstance(self.bto_id, str):
            self.bto_id = str(self.bto_id)

        if self.mesh_id is not None and not isinstance(self.mesh_id, str):
            self.mesh_id = str(self.mesh_id)

        if self.anatomical_system is not None and not isinstance(self.anatomical_system, str):
            self.anatomical_system = str(self.anatomical_system)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MolecularEntity(OntologyClass):
    """
    Abstract base for molecular-level entities (genes, proteins, variants). Directly related to disease mechanisms via
    molecular interactions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["MolecularEntity"]
    class_class_curie: ClassVar[str] = "biolink:MolecularEntity"
    class_name: ClassVar[str] = "MolecularEntity"
    class_model_uri: ClassVar[URIRef] = ALSKB.MolecularEntity

    id: str = None
    label: str = None

@dataclass(repr=False)
class Gene(MolecularEntity):
    """
    Human gene entity (Entrez/NCBI model). Separate from protein product to properly distinguish genotype from
    phenotype. Key ALS genes: C9orf72, SOD1, TARDBP, FUS, TBK1, NEK1, SQSTM1, VCP, OPTN.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Gene"]
    class_class_curie: ClassVar[str] = "biolink:Gene"
    class_name: ClassVar[str] = "Gene"
    class_model_uri: ClassVar[URIRef] = ALSKB.Gene

    ncbi_gene_id: Union[str, GeneNcbiGeneId] = None
    id: str = None
    label: str = None
    hgnc_symbol: Optional[str] = None
    ensembl_id: Optional[str] = None
    chromosome: Optional[str] = None
    genomic_pos_start: Optional[int] = None
    genomic_pos_end: Optional[int] = None
    als_risk_tier: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ncbi_gene_id):
            self.MissingRequiredField("ncbi_gene_id")
        if not isinstance(self.ncbi_gene_id, GeneNcbiGeneId):
            self.ncbi_gene_id = GeneNcbiGeneId(self.ncbi_gene_id)

        if self.hgnc_symbol is not None and not isinstance(self.hgnc_symbol, str):
            self.hgnc_symbol = str(self.hgnc_symbol)

        if self.ensembl_id is not None and not isinstance(self.ensembl_id, str):
            self.ensembl_id = str(self.ensembl_id)

        if self.chromosome is not None and not isinstance(self.chromosome, str):
            self.chromosome = str(self.chromosome)

        if self.genomic_pos_start is not None and not isinstance(self.genomic_pos_start, int):
            self.genomic_pos_start = int(self.genomic_pos_start)

        if self.genomic_pos_end is not None and not isinstance(self.genomic_pos_end, int):
            self.genomic_pos_end = int(self.genomic_pos_end)

        if self.als_risk_tier is not None and not isinstance(self.als_risk_tier, str):
            self.als_risk_tier = str(self.als_risk_tier)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TranscriptionFactor(Gene):
    """
    Gene encoding a transcription factor (TF). Subclass of Gene, carries both :Gene and :TranscriptionFactor labels.
    Source: DoRothEA + ENCODE TF annotations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKB["TranscriptionFactor"]
    class_class_curie: ClassVar[str] = "alskb:TranscriptionFactor"
    class_name: ClassVar[str] = "TranscriptionFactor"
    class_model_uri: ClassVar[URIRef] = ALSKB.TranscriptionFactor

    ncbi_gene_id: Union[str, TranscriptionFactorNcbiGeneId] = None
    id: str = None
    label: str = None
    tf_family: Optional[str] = None
    dorothea_confidence: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ncbi_gene_id):
            self.MissingRequiredField("ncbi_gene_id")
        if not isinstance(self.ncbi_gene_id, TranscriptionFactorNcbiGeneId):
            self.ncbi_gene_id = TranscriptionFactorNcbiGeneId(self.ncbi_gene_id)

        if self.tf_family is not None and not isinstance(self.tf_family, str):
            self.tf_family = str(self.tf_family)

        if self.dorothea_confidence is not None and not isinstance(self.dorothea_confidence, str):
            self.dorothea_confidence = str(self.dorothea_confidence)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Protein(MolecularEntity):
    """
    Protein product (UniProt model). Distinct from Gene entity to capture protein-specific properties: aggregation
    propensity, prion-like domains, subcellular localization.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Protein"]
    class_class_curie: ClassVar[str] = "biolink:Protein"
    class_name: ClassVar[str] = "Protein"
    class_model_uri: ClassVar[URIRef] = ALSKB.Protein

    uniprot_id: Union[str, ProteinUniprotId] = None
    id: str = None
    label: str = None
    protein_name: Optional[str] = None
    hgnc_symbol: Optional[str] = None
    molecular_weight_kda: Optional[float] = None
    protein_family: Optional[str] = None
    subcellular_location: Optional[Union[str, list[str]]] = empty_list()
    aggregation_prone: Optional[Union[bool, Bool]] = None
    has_prion_like_domain: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.uniprot_id):
            self.MissingRequiredField("uniprot_id")
        if not isinstance(self.uniprot_id, ProteinUniprotId):
            self.uniprot_id = ProteinUniprotId(self.uniprot_id)

        if self.protein_name is not None and not isinstance(self.protein_name, str):
            self.protein_name = str(self.protein_name)

        if self.hgnc_symbol is not None and not isinstance(self.hgnc_symbol, str):
            self.hgnc_symbol = str(self.hgnc_symbol)

        if self.molecular_weight_kda is not None and not isinstance(self.molecular_weight_kda, float):
            self.molecular_weight_kda = float(self.molecular_weight_kda)

        if self.protein_family is not None and not isinstance(self.protein_family, str):
            self.protein_family = str(self.protein_family)

        if not isinstance(self.subcellular_location, list):
            self.subcellular_location = [self.subcellular_location] if self.subcellular_location is not None else []
        self.subcellular_location = [v if isinstance(v, str) else str(v) for v in self.subcellular_location]

        if self.aggregation_prone is not None and not isinstance(self.aggregation_prone, Bool):
            self.aggregation_prone = Bool(self.aggregation_prone)

        if self.has_prion_like_domain is not None and not isinstance(self.has_prion_like_domain, Bool):
            self.has_prion_like_domain = Bool(self.has_prion_like_domain)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Variant(MolecularEntity):
    """
    Genetic sequence variant (ClinVar model). Includes SNVs, indels, repeat expansions (C9orf72), and structural
    variants. Links to genes, proteins, and disease associations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["SequenceVariant"]
    class_class_curie: ClassVar[str] = "biolink:SequenceVariant"
    class_name: ClassVar[str] = "Variant"
    class_model_uri: ClassVar[URIRef] = ALSKB.Variant

    clinvar_id: Union[str, VariantClinvarId] = None
    id: str = None
    label: str = None
    rsid: Optional[str] = None
    hgvs_c: Optional[str] = None
    hgvs_p: Optional[str] = None
    variant_type: Optional[Union[str, "VariantTypeEnum"]] = None
    clinical_significance: Optional[str] = None
    als_class: Optional[str] = None
    maf: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.clinvar_id):
            self.MissingRequiredField("clinvar_id")
        if not isinstance(self.clinvar_id, VariantClinvarId):
            self.clinvar_id = VariantClinvarId(self.clinvar_id)

        if self.rsid is not None and not isinstance(self.rsid, str):
            self.rsid = str(self.rsid)

        if self.hgvs_c is not None and not isinstance(self.hgvs_c, str):
            self.hgvs_c = str(self.hgvs_c)

        if self.hgvs_p is not None and not isinstance(self.hgvs_p, str):
            self.hgvs_p = str(self.hgvs_p)

        if self.variant_type is not None and not isinstance(self.variant_type, VariantTypeEnum):
            self.variant_type = VariantTypeEnum(self.variant_type)

        if self.clinical_significance is not None and not isinstance(self.clinical_significance, str):
            self.clinical_significance = str(self.clinical_significance)

        if self.als_class is not None and not isinstance(self.als_class, str):
            self.als_class = str(self.als_class)

        if self.maf is not None and not isinstance(self.maf, float):
            self.maf = float(self.maf)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalEntity(OntologyClass):
    """
    Abstract base for chemical and pharmacological entities (drugs, exposures, metabolites).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ChemicalEntity"]
    class_class_curie: ClassVar[str] = "biolink:ChemicalEntity"
    class_name: ClassVar[str] = "ChemicalEntity"
    class_model_uri: ClassVar[URIRef] = ALSKB.ChemicalEntity

    id: str = None
    label: str = None

@dataclass(repr=False)
class Drug(ChemicalEntity):
    """
    Pharmaceutical compound (DrugBank model). ALS-approved drugs: Riluzole, Edaravone, Tofersen, AMX0035. Includes
    mechanism, targets, side effects.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Drug"]
    class_class_curie: ClassVar[str] = "biolink:Drug"
    class_name: ClassVar[str] = "Drug"
    class_model_uri: ClassVar[URIRef] = ALSKB.Drug

    drugbank_id: Union[str, DrugDrugbankId] = None
    id: str = None
    label: str = None
    drug_name: Optional[str] = None
    chembl_id: Optional[str] = None
    inchi_key: Optional[str] = None
    smiles: Optional[str] = None
    drug_type: Optional[str] = None
    als_approved: Optional[Union[bool, Bool]] = None
    trial_status: Optional[str] = None
    mechanism: Optional[str] = None
    indication: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.drugbank_id):
            self.MissingRequiredField("drugbank_id")
        if not isinstance(self.drugbank_id, DrugDrugbankId):
            self.drugbank_id = DrugDrugbankId(self.drugbank_id)

        if self.drug_name is not None and not isinstance(self.drug_name, str):
            self.drug_name = str(self.drug_name)

        if self.chembl_id is not None and not isinstance(self.chembl_id, str):
            self.chembl_id = str(self.chembl_id)

        if self.inchi_key is not None and not isinstance(self.inchi_key, str):
            self.inchi_key = str(self.inchi_key)

        if self.smiles is not None and not isinstance(self.smiles, str):
            self.smiles = str(self.smiles)

        if self.drug_type is not None and not isinstance(self.drug_type, str):
            self.drug_type = str(self.drug_type)

        if self.als_approved is not None and not isinstance(self.als_approved, Bool):
            self.als_approved = Bool(self.als_approved)

        if self.trial_status is not None and not isinstance(self.trial_status, str):
            self.trial_status = str(self.trial_status)

        if self.mechanism is not None and not isinstance(self.mechanism, str):
            self.mechanism = str(self.mechanism)

        if self.indication is not None and not isinstance(self.indication, str):
            self.indication = str(self.indication)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExposureOrStressor(ChemicalEntity):
    """
    Environmental exposure or chemical stressor from CTD ontology. ALS-relevant: BMAA, organophosphate pesticides,
    heavy metals, solvents.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["ChemicalSubstance"]
    class_class_curie: ClassVar[str] = "biolink:ChemicalSubstance"
    class_name: ClassVar[str] = "ExposureOrStressor"
    class_model_uri: ClassVar[URIRef] = ALSKB.ExposureOrStressor

    ctd_id: Union[str, ExposureOrStressorCtdId] = None
    id: str = None
    label: str = None
    exposure_name: Optional[str] = None
    exposure_type: Optional[str] = None
    mesh_id: Optional[str] = None
    cas_number: Optional[str] = None
    als_relevance: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ctd_id):
            self.MissingRequiredField("ctd_id")
        if not isinstance(self.ctd_id, ExposureOrStressorCtdId):
            self.ctd_id = ExposureOrStressorCtdId(self.ctd_id)

        if self.exposure_name is not None and not isinstance(self.exposure_name, str):
            self.exposure_name = str(self.exposure_name)

        if self.exposure_type is not None and not isinstance(self.exposure_type, str):
            self.exposure_type = str(self.exposure_type)

        if self.mesh_id is not None and not isinstance(self.mesh_id, str):
            self.mesh_id = str(self.mesh_id)

        if self.cas_number is not None and not isinstance(self.cas_number, str):
            self.cas_number = str(self.cas_number)

        if self.als_relevance is not None and not isinstance(self.als_relevance, Bool):
            self.als_relevance = Bool(self.als_relevance)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiologicalConcept(OntologyClass):
    """
    Abstract base for functional/biological concepts from GO and related ontologies. Represents processes, functions,
    and compartments involved in ALS pathology.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKB["BiologicalConcept"]
    class_class_curie: ClassVar[str] = "alskb:BiologicalConcept"
    class_name: ClassVar[str] = "BiologicalConcept"
    class_model_uri: ClassVar[URIRef] = ALSKB.BiologicalConcept

    id: str = None
    label: str = None

@dataclass(repr=False)
class BiologicalProcess(BiologicalConcept):
    """
    Gene Ontology Biological Process term. ALS-relevant: protein aggregation, oxidative stress, neuroinflammation,
    axonal transport, neurodegeneration, apoptosis.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["BiologicalProcess"]
    class_class_curie: ClassVar[str] = "biolink:BiologicalProcess"
    class_name: ClassVar[str] = "BiologicalProcess"
    class_model_uri: ClassVar[URIRef] = ALSKB.BiologicalProcess

    go_id: Union[str, BiologicalProcessGoId] = None
    id: str = None
    label: str = None
    process_name: Optional[str] = None
    go_definition: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.go_id):
            self.MissingRequiredField("go_id")
        if not isinstance(self.go_id, BiologicalProcessGoId):
            self.go_id = BiologicalProcessGoId(self.go_id)

        if self.process_name is not None and not isinstance(self.process_name, str):
            self.process_name = str(self.process_name)

        if self.go_definition is not None and not isinstance(self.go_definition, str):
            self.go_definition = str(self.go_definition)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MolecularFunction(BiologicalConcept):
    """
    Gene Ontology Molecular Function term. Describes biochemical activities (catalytic, binding, etc.) performed by
    gene products.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["MolecularActivity"]
    class_class_curie: ClassVar[str] = "biolink:MolecularActivity"
    class_name: ClassVar[str] = "MolecularFunction"
    class_model_uri: ClassVar[URIRef] = ALSKB.MolecularFunction

    go_id: Union[str, MolecularFunctionGoId] = None
    id: str = None
    label: str = None
    function_name: Optional[str] = None
    go_definition: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.go_id):
            self.MissingRequiredField("go_id")
        if not isinstance(self.go_id, MolecularFunctionGoId):
            self.go_id = MolecularFunctionGoId(self.go_id)

        if self.function_name is not None and not isinstance(self.function_name, str):
            self.function_name = str(self.function_name)

        if self.go_definition is not None and not isinstance(self.go_definition, str):
            self.go_definition = str(self.go_definition)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CellularComponent(BiologicalConcept):
    """
    Gene Ontology Cellular Component term. ALS-critical compartments: stress granule, P-body, cytoplasm, nucleus,
    axon, neuromuscular junction, mitochondrion.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["CellularComponent"]
    class_class_curie: ClassVar[str] = "biolink:CellularComponent"
    class_name: ClassVar[str] = "CellularComponent"
    class_model_uri: ClassVar[URIRef] = ALSKB.CellularComponent

    go_id: Union[str, CellularComponentGoId] = None
    id: str = None
    label: str = None
    component_name: Optional[str] = None
    go_definition: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.go_id):
            self.MissingRequiredField("go_id")
        if not isinstance(self.go_id, CellularComponentGoId):
            self.go_id = CellularComponentGoId(self.go_id)

        if self.component_name is not None and not isinstance(self.component_name, str):
            self.component_name = str(self.component_name)

        if self.go_definition is not None and not isinstance(self.go_definition, str):
            self.go_definition = str(self.go_definition)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Pathway(BiologicalConcept):
    """
    Reactome pathway entity representing a curated biological pathway or reaction-level pathway context relevant to
    ALS mechanisms, including neuroinflammation, RNA metabolism, protein homeostasis, mitochondrial dysfunction, and
    axonal transport.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Pathway"]
    class_class_curie: ClassVar[str] = "biolink:Pathway"
    class_name: ClassVar[str] = "Pathway"
    class_model_uri: ClassVar[URIRef] = ALSKB.Pathway

    reactome_id: Union[str, PathwayReactomeId] = None
    id: str = None
    label: str = None
    pathway_name: Optional[str] = None
    pathway_definition: Optional[str] = None
    species: Optional[str] = None
    parent_pathway: Optional[Union[Union[str, ReactomeIdentifier], list[Union[str, ReactomeIdentifier]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.reactome_id):
            self.MissingRequiredField("reactome_id")
        if not isinstance(self.reactome_id, PathwayReactomeId):
            self.reactome_id = PathwayReactomeId(self.reactome_id)

        if self.pathway_name is not None and not isinstance(self.pathway_name, str):
            self.pathway_name = str(self.pathway_name)

        if self.pathway_definition is not None and not isinstance(self.pathway_definition, str):
            self.pathway_definition = str(self.pathway_definition)

        if self.species is not None and not isinstance(self.species, str):
            self.species = str(self.species)

        if not isinstance(self.parent_pathway, list):
            self.parent_pathway = [self.parent_pathway] if self.parent_pathway is not None else []
        self.parent_pathway = [v if isinstance(v, ReactomeIdentifier) else ReactomeIdentifier(v) for v in self.parent_pathway]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DiseaseSubtype(Disease):
    """
    Molecularly-defined disease subtype derived from clustering analysis (transcriptomics, proteomics, multi-omics).
    Represents cohort stratification. Links to Disease via is_a relationship; carries distinct clinical correlates.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKB["DiseaseSubtype"]
    class_class_curie: ClassVar[str] = "alskb:DiseaseSubtype"
    class_name: ClassVar[str] = "DiseaseSubtype"
    class_model_uri: ClassVar[URIRef] = ALSKB.DiseaseSubtype

    mondo_id: Union[str, DiseaseSubtypeMondoId] = None
    id: str = None
    label: str = None
    subtype_id: Optional[str] = None
    cluster_method: Optional[str] = None
    cluster_id: Optional[int] = None
    signature_genes: Optional[Union[str, list[str]]] = empty_list()
    n_patients: Optional[int] = None
    cohort: Optional[str] = None
    clinical_correlate: Optional[str] = None
    median_survival_months: Optional[float] = None
    source_publication: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.mondo_id):
            self.MissingRequiredField("mondo_id")
        if not isinstance(self.mondo_id, DiseaseSubtypeMondoId):
            self.mondo_id = DiseaseSubtypeMondoId(self.mondo_id)

        if self.subtype_id is not None and not isinstance(self.subtype_id, str):
            self.subtype_id = str(self.subtype_id)

        if self.cluster_method is not None and not isinstance(self.cluster_method, str):
            self.cluster_method = str(self.cluster_method)

        if self.cluster_id is not None and not isinstance(self.cluster_id, int):
            self.cluster_id = int(self.cluster_id)

        if not isinstance(self.signature_genes, list):
            self.signature_genes = [self.signature_genes] if self.signature_genes is not None else []
        self.signature_genes = [v if isinstance(v, str) else str(v) for v in self.signature_genes]

        if self.n_patients is not None and not isinstance(self.n_patients, int):
            self.n_patients = int(self.n_patients)

        if self.cohort is not None and not isinstance(self.cohort, str):
            self.cohort = str(self.cohort)

        if self.clinical_correlate is not None and not isinstance(self.clinical_correlate, str):
            self.clinical_correlate = str(self.clinical_correlate)

        if self.median_survival_months is not None and not isinstance(self.median_survival_months, float):
            self.median_survival_months = float(self.median_survival_months)

        if self.source_publication is not None and not isinstance(self.source_publication, str):
            self.source_publication = str(self.source_publication)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Association(Relationship):
    """
    Abstract base for optional evidence-bearing associations. Use when a relationship cannot be represented
    sufficiently by a direct object property because the edge needs provenance, evidence, confidence, or additional
    qualifiers. The subject/predicate/object fields allow the association to be materialized as an RDF triple or
    property-graph edge.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Association"]
    class_class_curie: ClassVar[str] = "biolink:Association"
    class_name: ClassVar[str] = "Association"
    class_model_uri: ClassVar[URIRef] = ALSKB.Association

    subject: str = None
    predicate: str = None
    object: str = None
    association_id: Optional[Union[str, URIorCURIE]] = None
    association_label: Optional[str] = None
    source: Optional[str] = None
    source_version: Optional[str] = None
    evidence_type: Optional[str] = None
    evidence_source: Optional[str] = None
    confidence: Optional[str] = None
    ingest_date: Optional[str] = None
    last_updated: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, str):
            self.subject = str(self.subject)

        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, str):
            self.object = str(self.object)

        if self.association_id is not None and not isinstance(self.association_id, URIorCURIE):
            self.association_id = URIorCURIE(self.association_id)

        if self.association_label is not None and not isinstance(self.association_label, str):
            self.association_label = str(self.association_label)

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        if self.source_version is not None and not isinstance(self.source_version, str):
            self.source_version = str(self.source_version)

        if self.evidence_type is not None and not isinstance(self.evidence_type, str):
            self.evidence_type = str(self.evidence_type)

        if self.evidence_source is not None and not isinstance(self.evidence_source, str):
            self.evidence_source = str(self.evidence_source)

        if self.confidence is not None and not isinstance(self.confidence, str):
            self.confidence = str(self.confidence)

        if self.ingest_date is not None and not isinstance(self.ingest_date, str):
            self.ingest_date = str(self.ingest_date)

        if self.last_updated is not None and not isinstance(self.last_updated, str):
            self.last_updated = str(self.last_updated)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DiseasePhenotypeAssociation(Association):
    """
    Optional association for Disease -> Phenotype when the clinical feature requires edge metadata such as frequency,
    onset, severity, source cohort, or evidence. Materializes to disease_manifests_as_phenotype.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKB["DiseasePhenotypeAssociation"]
    class_class_curie: ClassVar[str] = "alskb:DiseasePhenotypeAssociation"
    class_name: ClassVar[str] = "DiseasePhenotypeAssociation"
    class_model_uri: ClassVar[URIRef] = ALSKB.DiseasePhenotypeAssociation

    subject: str = None
    object: str = None
    has_disease: Union[str, DiseaseMondoId] = None
    has_phenotype: Union[str, PhenotypeHpoId] = None
    predicate: Optional[str] = "alskb:disease_manifests_as_phenotype"
    frequency: Optional[str] = None
    severity: Optional[str] = None
    onset_type: Optional[Union[str, "OnsetTypeEnum"]] = None
    cohort: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.has_disease):
            self.MissingRequiredField("has_disease")
        if not isinstance(self.has_disease, DiseaseMondoId):
            self.has_disease = DiseaseMondoId(self.has_disease)

        if self._is_empty(self.has_phenotype):
            self.MissingRequiredField("has_phenotype")
        if not isinstance(self.has_phenotype, PhenotypeHpoId):
            self.has_phenotype = PhenotypeHpoId(self.has_phenotype)

        if self.predicate is not None and not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self.frequency is not None and not isinstance(self.frequency, str):
            self.frequency = str(self.frequency)

        if self.severity is not None and not isinstance(self.severity, str):
            self.severity = str(self.severity)

        if self.onset_type is not None and not isinstance(self.onset_type, OnsetTypeEnum):
            self.onset_type = OnsetTypeEnum(self.onset_type)

        if self.cohort is not None and not isinstance(self.cohort, str):
            self.cohort = str(self.cohort)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneDiseaseAssociation(Association):
    """
    Optional association for Gene -> Disease when causal/risk/protective or correlative gene-disease edges need
    evidence, scores, statistics, or source-specific qualifiers. Materializes to gene_associated_with_disease.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKB["GeneDiseaseAssociation"]
    class_class_curie: ClassVar[str] = "alskb:GeneDiseaseAssociation"
    class_name: ClassVar[str] = "GeneDiseaseAssociation"
    class_model_uri: ClassVar[URIRef] = ALSKB.GeneDiseaseAssociation

    subject: str = None
    object: str = None
    has_gene: Union[str, GeneNcbiGeneId] = None
    has_disease: Union[str, DiseaseMondoId] = None
    predicate: Optional[str] = "alskb:gene_associated_with_disease"
    association_type: Optional[str] = None
    association_score: Optional[float] = None
    p_value: Optional[float] = None
    odds_ratio: Optional[float] = None
    effect_direction: Optional[str] = None
    evidence_count: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.has_gene):
            self.MissingRequiredField("has_gene")
        if not isinstance(self.has_gene, GeneNcbiGeneId):
            self.has_gene = GeneNcbiGeneId(self.has_gene)

        if self._is_empty(self.has_disease):
            self.MissingRequiredField("has_disease")
        if not isinstance(self.has_disease, DiseaseMondoId):
            self.has_disease = DiseaseMondoId(self.has_disease)

        if self.predicate is not None and not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self.association_type is not None and not isinstance(self.association_type, str):
            self.association_type = str(self.association_type)

        if self.association_score is not None and not isinstance(self.association_score, float):
            self.association_score = float(self.association_score)

        if self.p_value is not None and not isinstance(self.p_value, float):
            self.p_value = float(self.p_value)

        if self.odds_ratio is not None and not isinstance(self.odds_ratio, float):
            self.odds_ratio = float(self.odds_ratio)

        if self.effect_direction is not None and not isinstance(self.effect_direction, str):
            self.effect_direction = str(self.effect_direction)

        if self.evidence_count is not None and not isinstance(self.evidence_count, int):
            self.evidence_count = int(self.evidence_count)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VariantDiseaseAssociation(Association):
    """
    Optional association for Variant -> Disease when variant-level evidence, clinical significance, inheritance,
    penetrance, or source assertions are needed. Materializes to variant_associated_with_disease.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKB["VariantDiseaseAssociation"]
    class_class_curie: ClassVar[str] = "alskb:VariantDiseaseAssociation"
    class_name: ClassVar[str] = "VariantDiseaseAssociation"
    class_model_uri: ClassVar[URIRef] = ALSKB.VariantDiseaseAssociation

    subject: str = None
    object: str = None
    has_variant: Union[str, VariantClinvarId] = None
    has_disease: Union[str, DiseaseMondoId] = None
    predicate: Optional[str] = "alskb:variant_associated_with_disease"
    clinical_significance: Optional[str] = None
    inheritance_mode: Optional[str] = None
    penetrance: Optional[str] = None
    association_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.has_variant):
            self.MissingRequiredField("has_variant")
        if not isinstance(self.has_variant, VariantClinvarId):
            self.has_variant = VariantClinvarId(self.has_variant)

        if self._is_empty(self.has_disease):
            self.MissingRequiredField("has_disease")
        if not isinstance(self.has_disease, DiseaseMondoId):
            self.has_disease = DiseaseMondoId(self.has_disease)

        if self.predicate is not None and not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self.clinical_significance is not None and not isinstance(self.clinical_significance, str):
            self.clinical_significance = str(self.clinical_significance)

        if self.inheritance_mode is not None and not isinstance(self.inheritance_mode, str):
            self.inheritance_mode = str(self.inheritance_mode)

        if self.penetrance is not None and not isinstance(self.penetrance, str):
            self.penetrance = str(self.penetrance)

        if self.association_type is not None and not isinstance(self.association_type, str):
            self.association_type = str(self.association_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VariantProteinEffectAssociation(Association):
    """
    Optional association for Variant -> Protein when protein consequence, predicted effect, assay result, or
    functional evidence is needed. Materializes to variant_affects_protein.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKB["VariantProteinEffectAssociation"]
    class_class_curie: ClassVar[str] = "alskb:VariantProteinEffectAssociation"
    class_name: ClassVar[str] = "VariantProteinEffectAssociation"
    class_model_uri: ClassVar[URIRef] = ALSKB.VariantProteinEffectAssociation

    subject: str = None
    object: str = None
    has_variant: Union[str, VariantClinvarId] = None
    has_protein: Union[str, ProteinUniprotId] = None
    predicate: Optional[str] = "alskb:variant_affects_protein"
    functional_consequence: Optional[str] = None
    predicted_effect: Optional[str] = None
    assay: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.has_variant):
            self.MissingRequiredField("has_variant")
        if not isinstance(self.has_variant, VariantClinvarId):
            self.has_variant = VariantClinvarId(self.has_variant)

        if self._is_empty(self.has_protein):
            self.MissingRequiredField("has_protein")
        if not isinstance(self.has_protein, ProteinUniprotId):
            self.has_protein = ProteinUniprotId(self.has_protein)

        if self.predicate is not None and not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self.functional_consequence is not None and not isinstance(self.functional_consequence, str):
            self.functional_consequence = str(self.functional_consequence)

        if self.predicted_effect is not None and not isinstance(self.predicted_effect, str):
            self.predicted_effect = str(self.predicted_effect)

        if self.assay is not None and not isinstance(self.assay, str):
            self.assay = str(self.assay)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProteinProteinInteractionAssociation(Association):
    """
    Optional association for Protein -> Protein when interaction score, interaction type, database evidence, or assay
    metadata are needed. Materializes to protein_interacts_with_protein.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKB["ProteinProteinInteractionAssociation"]
    class_class_curie: ClassVar[str] = "alskb:ProteinProteinInteractionAssociation"
    class_name: ClassVar[str] = "ProteinProteinInteractionAssociation"
    class_model_uri: ClassVar[URIRef] = ALSKB.ProteinProteinInteractionAssociation

    subject: str = None
    object: str = None
    protein_1: Union[str, ProteinUniprotId] = None
    protein_2: Union[str, ProteinUniprotId] = None
    predicate: Optional[str] = "alskb:protein_interacts_with_protein"
    interaction_score: Optional[float] = None
    interaction_type: Optional[str] = None
    assay: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.protein_1):
            self.MissingRequiredField("protein_1")
        if not isinstance(self.protein_1, ProteinUniprotId):
            self.protein_1 = ProteinUniprotId(self.protein_1)

        if self._is_empty(self.protein_2):
            self.MissingRequiredField("protein_2")
        if not isinstance(self.protein_2, ProteinUniprotId):
            self.protein_2 = ProteinUniprotId(self.protein_2)

        if self.predicate is not None and not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self.interaction_score is not None and not isinstance(self.interaction_score, float):
            self.interaction_score = float(self.interaction_score)

        if self.interaction_type is not None and not isinstance(self.interaction_type, str):
            self.interaction_type = str(self.interaction_type)

        if self.assay is not None and not isinstance(self.assay, str):
            self.assay = str(self.assay)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProteinPathwayAssociation(Association):
    """
    Optional association for Protein -> Pathway when Reactome evidence code, source release, pathway hierarchy,
    species, or annotation provenance are needed. Materializes to protein_participates_in_pathway.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKB["ProteinPathwayAssociation"]
    class_class_curie: ClassVar[str] = "alskb:ProteinPathwayAssociation"
    class_name: ClassVar[str] = "ProteinPathwayAssociation"
    class_model_uri: ClassVar[URIRef] = ALSKB.ProteinPathwayAssociation

    subject: str = None
    object: str = None
    has_protein: Union[str, ProteinUniprotId] = None
    has_pathway: Union[str, PathwayReactomeId] = None
    predicate: Optional[str] = "alskb:protein_participates_in_pathway"
    reactome_evidence_code: Optional[str] = None
    pathway_role: Optional[str] = None
    species: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.has_protein):
            self.MissingRequiredField("has_protein")
        if not isinstance(self.has_protein, ProteinUniprotId):
            self.has_protein = ProteinUniprotId(self.has_protein)

        if self._is_empty(self.has_pathway):
            self.MissingRequiredField("has_pathway")
        if not isinstance(self.has_pathway, PathwayReactomeId):
            self.has_pathway = PathwayReactomeId(self.has_pathway)

        if self.predicate is not None and not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self.reactome_evidence_code is not None and not isinstance(self.reactome_evidence_code, str):
            self.reactome_evidence_code = str(self.reactome_evidence_code)

        if self.pathway_role is not None and not isinstance(self.pathway_role, str):
            self.pathway_role = str(self.pathway_role)

        if self.species is not None and not isinstance(self.species, str):
            self.species = str(self.species)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugTargetAssociation(Association):
    """
    Optional association for Drug -> MolecularEntity when action type, binding affinity, target class, or mechanism
    evidence is needed. Materializes to drug_targets_molecular_entity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKB["DrugTargetAssociation"]
    class_class_curie: ClassVar[str] = "alskb:DrugTargetAssociation"
    class_name: ClassVar[str] = "DrugTargetAssociation"
    class_model_uri: ClassVar[URIRef] = ALSKB.DrugTargetAssociation

    subject: str = None
    object: str = None
    has_drug: Union[str, DrugDrugbankId] = None
    target: Union[dict, MolecularEntity] = None
    predicate: Optional[str] = "alskb:drug_targets_molecular_entity"
    action_type: Optional[str] = None
    binding_affinity_nm: Optional[float] = None
    mechanism: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.has_drug):
            self.MissingRequiredField("has_drug")
        if not isinstance(self.has_drug, DrugDrugbankId):
            self.has_drug = DrugDrugbankId(self.has_drug)

        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, MolecularEntity):
            self.target = MolecularEntity(**as_dict(self.target))

        if self.predicate is not None and not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self.action_type is not None and not isinstance(self.action_type, str):
            self.action_type = str(self.action_type)

        if self.binding_affinity_nm is not None and not isinstance(self.binding_affinity_nm, float):
            self.binding_affinity_nm = float(self.binding_affinity_nm)

        if self.mechanism is not None and not isinstance(self.mechanism, str):
            self.mechanism = str(self.mechanism)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DrugDiseaseTherapeuticAssociation(Association):
    """
    Optional association for Drug -> Disease when therapeutic indication, approval status, clinical-trial evidence, or
    outcome metadata are needed. Materializes to drug_treats_or_modulates_disease.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKB["DrugDiseaseTherapeuticAssociation"]
    class_class_curie: ClassVar[str] = "alskb:DrugDiseaseTherapeuticAssociation"
    class_name: ClassVar[str] = "DrugDiseaseTherapeuticAssociation"
    class_model_uri: ClassVar[URIRef] = ALSKB.DrugDiseaseTherapeuticAssociation

    subject: str = None
    object: str = None
    has_drug: Union[str, DrugDrugbankId] = None
    has_disease: Union[str, DiseaseMondoId] = None
    predicate: Optional[str] = "alskb:drug_treats_or_modulates_disease"
    relation_type: Optional[str] = None
    approval_status: Optional[str] = None
    clinical_phase: Optional[str] = None
    outcome_measure: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.has_drug):
            self.MissingRequiredField("has_drug")
        if not isinstance(self.has_drug, DrugDrugbankId):
            self.has_drug = DrugDrugbankId(self.has_drug)

        if self._is_empty(self.has_disease):
            self.MissingRequiredField("has_disease")
        if not isinstance(self.has_disease, DiseaseMondoId):
            self.has_disease = DiseaseMondoId(self.has_disease)

        if self.predicate is not None and not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self.relation_type is not None and not isinstance(self.relation_type, str):
            self.relation_type = str(self.relation_type)

        if self.approval_status is not None and not isinstance(self.approval_status, str):
            self.approval_status = str(self.approval_status)

        if self.clinical_phase is not None and not isinstance(self.clinical_phase, str):
            self.clinical_phase = str(self.clinical_phase)

        if self.outcome_measure is not None and not isinstance(self.outcome_measure, str):
            self.outcome_measure = str(self.outcome_measure)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExposureDiseaseAssociation(Association):
    """
    Optional association for ExposureOrStressor -> Disease when epidemiology, mechanism, dose, duration, population,
    or study design metadata are needed. Materializes to exposure_associated_with_disease.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKB["ExposureDiseaseAssociation"]
    class_class_curie: ClassVar[str] = "alskb:ExposureDiseaseAssociation"
    class_name: ClassVar[str] = "ExposureDiseaseAssociation"
    class_model_uri: ClassVar[URIRef] = ALSKB.ExposureDiseaseAssociation

    subject: str = None
    object: str = None
    exposure: Union[str, ExposureOrStressorCtdId] = None
    has_disease: Union[str, DiseaseMondoId] = None
    predicate: Optional[str] = "alskb:exposure_associated_with_disease"
    association_type: Optional[str] = None
    mechanism: Optional[str] = None
    epidemiological_support: Optional[Union[bool, Bool]] = None
    odds_ratio: Optional[float] = None
    population: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.exposure):
            self.MissingRequiredField("exposure")
        if not isinstance(self.exposure, ExposureOrStressorCtdId):
            self.exposure = ExposureOrStressorCtdId(self.exposure)

        if self._is_empty(self.has_disease):
            self.MissingRequiredField("has_disease")
        if not isinstance(self.has_disease, DiseaseMondoId):
            self.has_disease = DiseaseMondoId(self.has_disease)

        if self.predicate is not None and not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self.association_type is not None and not isinstance(self.association_type, str):
            self.association_type = str(self.association_type)

        if self.mechanism is not None and not isinstance(self.mechanism, str):
            self.mechanism = str(self.mechanism)

        if self.epidemiological_support is not None and not isinstance(self.epidemiological_support, Bool):
            self.epidemiological_support = Bool(self.epidemiological_support)

        if self.odds_ratio is not None and not isinstance(self.odds_ratio, float):
            self.odds_ratio = float(self.odds_ratio)

        if self.population is not None and not isinstance(self.population, str):
            self.population = str(self.population)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TranscriptionFactorRegulationAssociation(Association):
    """
    Optional association for TranscriptionFactor -> Gene when direction, confidence, tissue/cell context, or assay
    evidence are needed. Materializes to transcription_factor_regulates_gene.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKB["TranscriptionFactorRegulationAssociation"]
    class_class_curie: ClassVar[str] = "alskb:TranscriptionFactorRegulationAssociation"
    class_name: ClassVar[str] = "TranscriptionFactorRegulationAssociation"
    class_model_uri: ClassVar[URIRef] = ALSKB.TranscriptionFactorRegulationAssociation

    subject: str = None
    object: str = None
    transcription_factor: Union[str, TranscriptionFactorNcbiGeneId] = None
    target_gene: Union[str, GeneNcbiGeneId] = None
    predicate: Optional[str] = "alskb:transcription_factor_regulates_gene"
    regulation_type: Optional[str] = None
    confidence_level: Optional[str] = None
    tissue_or_cell_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.transcription_factor):
            self.MissingRequiredField("transcription_factor")
        if not isinstance(self.transcription_factor, TranscriptionFactorNcbiGeneId):
            self.transcription_factor = TranscriptionFactorNcbiGeneId(self.transcription_factor)

        if self._is_empty(self.target_gene):
            self.MissingRequiredField("target_gene")
        if not isinstance(self.target_gene, GeneNcbiGeneId):
            self.target_gene = GeneNcbiGeneId(self.target_gene)

        if self.predicate is not None and not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self.regulation_type is not None and not isinstance(self.regulation_type, str):
            self.regulation_type = str(self.regulation_type)

        if self.confidence_level is not None and not isinstance(self.confidence_level, str):
            self.confidence_level = str(self.confidence_level)

        if self.tissue_or_cell_type is not None and not isinstance(self.tissue_or_cell_type, str):
            self.tissue_or_cell_type = str(self.tissue_or_cell_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneExpressionAssociation(Association):
    """
    Optional association for Gene -> Anatomy when expression level, specificity, tissue, cell type, disease stage, or
    differential-expression qualifiers are needed. Materializes to gene_expressed_in_anatomy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKB["GeneExpressionAssociation"]
    class_class_curie: ClassVar[str] = "alskb:GeneExpressionAssociation"
    class_name: ClassVar[str] = "GeneExpressionAssociation"
    class_model_uri: ClassVar[URIRef] = ALSKB.GeneExpressionAssociation

    subject: str = None
    object: str = None
    has_gene: Union[str, GeneNcbiGeneId] = None
    has_anatomy: Union[str, AnatomyUberonId] = None
    predicate: Optional[str] = "alskb:gene_expressed_in_anatomy"
    expression_level: Optional[str] = None
    specificity_index: Optional[float] = None
    log2_fold_change: Optional[float] = None
    adjusted_p_value: Optional[float] = None
    tissue_or_cell_type: Optional[str] = None
    disease_stage: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.has_gene):
            self.MissingRequiredField("has_gene")
        if not isinstance(self.has_gene, GeneNcbiGeneId):
            self.has_gene = GeneNcbiGeneId(self.has_gene)

        if self._is_empty(self.has_anatomy):
            self.MissingRequiredField("has_anatomy")
        if not isinstance(self.has_anatomy, AnatomyUberonId):
            self.has_anatomy = AnatomyUberonId(self.has_anatomy)

        if self.predicate is not None and not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self.expression_level is not None and not isinstance(self.expression_level, str):
            self.expression_level = str(self.expression_level)

        if self.specificity_index is not None and not isinstance(self.specificity_index, float):
            self.specificity_index = float(self.specificity_index)

        if self.log2_fold_change is not None and not isinstance(self.log2_fold_change, float):
            self.log2_fold_change = float(self.log2_fold_change)

        if self.adjusted_p_value is not None and not isinstance(self.adjusted_p_value, float):
            self.adjusted_p_value = float(self.adjusted_p_value)

        if self.tissue_or_cell_type is not None and not isinstance(self.tissue_or_cell_type, str):
            self.tissue_or_cell_type = str(self.tissue_or_cell_type)

        if self.disease_stage is not None and not isinstance(self.disease_stage, str):
            self.disease_stage = str(self.disease_stage)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DiseaseDiseaseAssociation(Association):
    """
    Optional association for Disease -> Disease when disease-disease edges need relation type, similarity score,
    shared mechanism, or comorbidity statistics. Materializes to disease_related_to_disease.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSKB["DiseaseDiseaseAssociation"]
    class_class_curie: ClassVar[str] = "alskb:DiseaseDiseaseAssociation"
    class_name: ClassVar[str] = "DiseaseDiseaseAssociation"
    class_model_uri: ClassVar[URIRef] = ALSKB.DiseaseDiseaseAssociation

    subject: str = None
    object: str = None
    disease_1: Union[str, DiseaseMondoId] = None
    disease_2: Union[str, DiseaseMondoId] = None
    predicate: Optional[str] = "alskb:disease_related_to_disease"
    relation_type: Optional[str] = None
    similarity_score: Optional[float] = None
    shared_mechanism: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.disease_1):
            self.MissingRequiredField("disease_1")
        if not isinstance(self.disease_1, DiseaseMondoId):
            self.disease_1 = DiseaseMondoId(self.disease_1)

        if self._is_empty(self.disease_2):
            self.MissingRequiredField("disease_2")
        if not isinstance(self.disease_2, DiseaseMondoId):
            self.disease_2 = DiseaseMondoId(self.disease_2)

        if self.predicate is not None and not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self.relation_type is not None and not isinstance(self.relation_type, str):
            self.relation_type = str(self.relation_type)

        if self.similarity_score is not None and not isinstance(self.similarity_score, float):
            self.similarity_score = float(self.similarity_score)

        if self.shared_mechanism is not None and not isinstance(self.shared_mechanism, str):
            self.shared_mechanism = str(self.shared_mechanism)

        super().__post_init__(**kwargs)


# Enumerations
class DiseaseTypeEnum(EnumDefinitionImpl):

    sporadic = PermissibleValue(
        text="sporadic",
        description="Occurs without family history")
    familial = PermissibleValue(
        text="familial",
        description="Inherited pattern of occurrence")
    syndromic = PermissibleValue(
        text="syndromic",
        description="Part of larger syndrome")

    _defn = EnumDefinition(
        name="DiseaseTypeEnum",
    )

class OnsetTypeEnum(EnumDefinitionImpl):

    bulbar = PermissibleValue(
        text="bulbar",
        description="Facial/tongue muscles affected first")
    limb = PermissibleValue(
        text="limb",
        description="Arm or leg muscles affected first")
    respiratory = PermissibleValue(
        text="respiratory",
        description="Breathing muscles affected first")
    generalized = PermissibleValue(
        text="generalized",
        description="Multiple sites affected simultaneously")
    unknown = PermissibleValue(
        text="unknown",
        description="Onset location unknown")

    _defn = EnumDefinition(
        name="OnsetTypeEnum",
    )

class GeneTypeEnum(EnumDefinitionImpl):

    protein_coding = PermissibleValue(text="protein_coding")
    lncRNA = PermissibleValue(text="lncRNA")
    miRNA = PermissibleValue(text="miRNA")
    pseudogene = PermissibleValue(text="pseudogene")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="GeneTypeEnum",
    )

class VariantTypeEnum(EnumDefinitionImpl):

    SNV = PermissibleValue(
        text="SNV",
        description="Single nucleotide variant")
    indel = PermissibleValue(
        text="indel",
        description="Insertion or deletion")
    repeat_expansion = PermissibleValue(
        text="repeat_expansion",
        description="Trinucleotide repeat expansion")
    CNV = PermissibleValue(
        text="CNV",
        description="Copy number variation")
    structural = PermissibleValue(
        text="structural",
        description="Structural variant (inversion, translocation)")

    _defn = EnumDefinition(
        name="VariantTypeEnum",
    )

class RelationshipTypeEnum(EnumDefinitionImpl):
    """
    Standard relationship types following RDF/OWL semantics
    """
    is_a = PermissibleValue(
        text="is_a",
        description="Subclass relationship (taxonomic)")
    part_of = PermissibleValue(
        text="part_of",
        description="Mereological (compositional) relationship")
    proper_part_of = PermissibleValue(
        text="proper_part_of",
        description="Strict part-of (excludes identity)")
    participates_in = PermissibleValue(
        text="participates_in",
        description="Agent participates in process")
    has_participant = PermissibleValue(
        text="has_participant",
        description="Process has participant")
    regulates = PermissibleValue(
        text="regulates",
        description="Regulatory relationship (direction unspecified)")
    positively_regulates = PermissibleValue(
        text="positively_regulates",
        description="Upregulation/activation")
    negatively_regulates = PermissibleValue(
        text="negatively_regulates",
        description="Downregulation/inhibition")
    associated_with = PermissibleValue(
        text="associated_with",
        description="Statistical/empirical association")
    affects = PermissibleValue(
        text="affects",
        description="Causal or functional modification")

    _defn = EnumDefinition(
        name="RelationshipTypeEnum",
        description="Standard relationship types following RDF/OWL semantics",
    )

class EvidenceTypeEnum(EnumDefinitionImpl):

    curated = PermissibleValue(
        text="curated",
        description="Manually curated from literature")
    experimental = PermissibleValue(
        text="experimental",
        description="Derived from wet-lab experiments")
    computational = PermissibleValue(
        text="computational",
        description="Result of computational analysis")
    inferred = PermissibleValue(
        text="inferred",
        description="Inferred from other statements")
    predicted = PermissibleValue(
        text="predicted",
        description="Machine learning prediction")
    text_mined = PermissibleValue(
        text="text_mined",
        description="Extracted via natural language processing")

    _defn = EnumDefinition(
        name="EvidenceTypeEnum",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=ALSKB.id, domain=None, range=URIRef)

slots.label = Slot(uri=RDFS.label, name="label", curie=RDFS.curie('label'),
                   model_uri=ALSKB.label, domain=None, range=str)

slots.definition = Slot(uri=IAO['0000115'], name="definition", curie=IAO.curie('0000115'),
                   model_uri=ALSKB.definition, domain=None, range=Optional[str])

slots.synonym = Slot(uri=OBOINOWL.hasRelatedSynonym, name="synonym", curie=OBOINOWL.curie('hasRelatedSynonym'),
                   model_uri=ALSKB.synonym, domain=None, range=Optional[Union[str, list[str]]])

slots.xref = Slot(uri=OBOINOWL.hasDbXref, name="xref", curie=OBOINOWL.curie('hasDbXref'),
                   model_uri=ALSKB.xref, domain=None, range=Optional[Union[str, list[str]]])

slots.comment = Slot(uri=RDFS.comment, name="comment", curie=RDFS.curie('comment'),
                   model_uri=ALSKB.comment, domain=None, range=Optional[str])

slots.is_obsolete = Slot(uri=OWL.deprecated, name="is_obsolete", curie=OWL.curie('deprecated'),
                   model_uri=ALSKB.is_obsolete, domain=None, range=Optional[Union[bool, Bool]])

slots.subject = Slot(uri=RDF.subject, name="subject", curie=RDF.curie('subject'),
                   model_uri=ALSKB.subject, domain=None, range=str)

slots.predicate = Slot(uri=RDF.predicate, name="predicate", curie=RDF.curie('predicate'),
                   model_uri=ALSKB.predicate, domain=None, range=Union[str, URIorCURIE])

slots.object = Slot(uri=RDF.object, name="object", curie=RDF.curie('object'),
                   model_uri=ALSKB.object, domain=None, range=str)

slots.has_anatomy = Slot(uri=ALSKB.has_anatomy, name="has_anatomy", curie=ALSKB.curie('has_anatomy'),
                   model_uri=ALSKB.has_anatomy, domain=None, range=Optional[Union[str, AnatomyUberonId]])

slots.has_disease = Slot(uri=ALSKB.has_disease, name="has_disease", curie=ALSKB.curie('has_disease'),
                   model_uri=ALSKB.has_disease, domain=None, range=Optional[Union[str, DiseaseMondoId]])

slots.has_drug = Slot(uri=ALSKB.has_drug, name="has_drug", curie=ALSKB.curie('has_drug'),
                   model_uri=ALSKB.has_drug, domain=None, range=Optional[Union[str, DrugDrugbankId]])

slots.has_gene = Slot(uri=ALSKB.has_gene, name="has_gene", curie=ALSKB.curie('has_gene'),
                   model_uri=ALSKB.has_gene, domain=None, range=Optional[Union[str, GeneNcbiGeneId]])

slots.has_phenotype = Slot(uri=ALSKB.has_phenotype, name="has_phenotype", curie=ALSKB.curie('has_phenotype'),
                   model_uri=ALSKB.has_phenotype, domain=None, range=Optional[Union[str, PhenotypeHpoId]])

slots.has_protein = Slot(uri=ALSKB.has_protein, name="has_protein", curie=ALSKB.curie('has_protein'),
                   model_uri=ALSKB.has_protein, domain=None, range=Optional[Union[str, ProteinUniprotId]])

slots.has_pathway = Slot(uri=ALSKB.has_pathway, name="has_pathway", curie=ALSKB.curie('has_pathway'),
                   model_uri=ALSKB.has_pathway, domain=None, range=Optional[Union[str, PathwayReactomeId]])

slots.has_variant = Slot(uri=ALSKB.has_variant, name="has_variant", curie=ALSKB.curie('has_variant'),
                   model_uri=ALSKB.has_variant, domain=None, range=Optional[Union[str, VariantClinvarId]])

slots.disease_manifests_as_phenotype = Slot(uri=BIOLINK.has_phenotype, name="disease_manifests_as_phenotype", curie=BIOLINK.curie('has_phenotype'),
                   model_uri=ALSKB.disease_manifests_as_phenotype, domain=Disease, range=Optional[Union[Union[str, PhenotypeHpoId], list[Union[str, PhenotypeHpoId]]]])

slots.disease_affects_anatomy = Slot(uri=ALSKB.disease_affects_anatomy, name="disease_affects_anatomy", curie=ALSKB.curie('disease_affects_anatomy'),
                   model_uri=ALSKB.disease_affects_anatomy, domain=Disease, range=Optional[Union[Union[str, AnatomyUberonId], list[Union[str, AnatomyUberonId]]]])

slots.gene_associated_with_disease = Slot(uri=BIOLINK.gene_associated_with_condition, name="gene_associated_with_disease", curie=BIOLINK.curie('gene_associated_with_condition'),
                   model_uri=ALSKB.gene_associated_with_disease, domain=Gene, range=Optional[Union[Union[str, DiseaseMondoId], list[Union[str, DiseaseMondoId]]]])

slots.variant_associated_with_disease = Slot(uri=BIOLINK.variant_associated_with_condition, name="variant_associated_with_disease", curie=BIOLINK.curie('variant_associated_with_condition'),
                   model_uri=ALSKB.variant_associated_with_disease, domain=Variant, range=Optional[Union[Union[str, DiseaseMondoId], list[Union[str, DiseaseMondoId]]]])

slots.variant_affects_protein = Slot(uri=ALSKB.variant_affects_protein, name="variant_affects_protein", curie=ALSKB.curie('variant_affects_protein'),
                   model_uri=ALSKB.variant_affects_protein, domain=Variant, range=Optional[Union[Union[str, ProteinUniprotId], list[Union[str, ProteinUniprotId]]]])

slots.gene_encodes_protein = Slot(uri=RO['0002205'], name="gene_encodes_protein", curie=RO.curie('0002205'),
                   model_uri=ALSKB.gene_encodes_protein, domain=Gene, range=Optional[Union[Union[str, ProteinUniprotId], list[Union[str, ProteinUniprotId]]]])

slots.protein_interacts_with_protein = Slot(uri=BIOLINK.interacts_with, name="protein_interacts_with_protein", curie=BIOLINK.curie('interacts_with'),
                   model_uri=ALSKB.protein_interacts_with_protein, domain=Protein, range=Optional[Union[Union[str, ProteinUniprotId], list[Union[str, ProteinUniprotId]]]])

slots.protein_participates_in_pathway = Slot(uri=BIOLINK.participates_in, name="protein_participates_in_pathway", curie=BIOLINK.curie('participates_in'),
                   model_uri=ALSKB.protein_participates_in_pathway, domain=Protein, range=Optional[Union[Union[str, PathwayReactomeId], list[Union[str, PathwayReactomeId]]]])

slots.drug_targets_molecular_entity = Slot(uri=BIOLINK.targets, name="drug_targets_molecular_entity", curie=BIOLINK.curie('targets'),
                   model_uri=ALSKB.drug_targets_molecular_entity, domain=Drug, range=Optional[Union[Union[dict, MolecularEntity], list[Union[dict, MolecularEntity]]]])

slots.drug_treats_or_modulates_disease = Slot(uri=ALSKB.drug_treats_or_modulates_disease, name="drug_treats_or_modulates_disease", curie=ALSKB.curie('drug_treats_or_modulates_disease'),
                   model_uri=ALSKB.drug_treats_or_modulates_disease, domain=Drug, range=Optional[Union[Union[str, DiseaseMondoId], list[Union[str, DiseaseMondoId]]]])

slots.exposure_associated_with_disease = Slot(uri=ALSKB.exposure_associated_with_disease, name="exposure_associated_with_disease", curie=ALSKB.curie('exposure_associated_with_disease'),
                   model_uri=ALSKB.exposure_associated_with_disease, domain=ExposureOrStressor, range=Optional[Union[Union[str, DiseaseMondoId], list[Union[str, DiseaseMondoId]]]])

slots.transcription_factor_regulates_gene = Slot(uri=BIOLINK.regulates, name="transcription_factor_regulates_gene", curie=BIOLINK.curie('regulates'),
                   model_uri=ALSKB.transcription_factor_regulates_gene, domain=TranscriptionFactor, range=Optional[Union[Union[str, GeneNcbiGeneId], list[Union[str, GeneNcbiGeneId]]]])

slots.gene_expressed_in_anatomy = Slot(uri=BIOLINK.expressed_in, name="gene_expressed_in_anatomy", curie=BIOLINK.curie('expressed_in'),
                   model_uri=ALSKB.gene_expressed_in_anatomy, domain=Gene, range=Optional[Union[Union[str, AnatomyUberonId], list[Union[str, AnatomyUberonId]]]])

slots.disease_related_to_disease = Slot(uri=BIOLINK.related_to, name="disease_related_to_disease", curie=BIOLINK.curie('related_to'),
                   model_uri=ALSKB.disease_related_to_disease, domain=Disease, range=Optional[Union[Union[str, DiseaseMondoId], list[Union[str, DiseaseMondoId]]]])

slots.gene_participates_in_process = Slot(uri=BIOLINK.participates_in, name="gene_participates_in_process", curie=BIOLINK.curie('participates_in'),
                   model_uri=ALSKB.gene_participates_in_process, domain=Gene, range=Optional[Union[Union[str, BiologicalProcessGoId], list[Union[str, BiologicalProcessGoId]]]])

slots.gene_has_molecular_function = Slot(uri=RO['0000085'], name="gene_has_molecular_function", curie=RO.curie('0000085'),
                   model_uri=ALSKB.gene_has_molecular_function, domain=Gene, range=Optional[Union[Union[str, MolecularFunctionGoId], list[Union[str, MolecularFunctionGoId]]]])

slots.protein_localized_to_cellular_component = Slot(uri=BIOLINK.located_in, name="protein_localized_to_cellular_component", curie=BIOLINK.curie('located_in'),
                   model_uri=ALSKB.protein_localized_to_cellular_component, domain=Protein, range=Optional[Union[Union[str, CellularComponentGoId], list[Union[str, CellularComponentGoId]]]])

slots.source = Slot(uri=DCTERMS.source, name="source", curie=DCTERMS.curie('source'),
                   model_uri=ALSKB.source, domain=None, range=Optional[str])

slots.source_version = Slot(uri=DCTERMS.hasVersion, name="source_version", curie=DCTERMS.curie('hasVersion'),
                   model_uri=ALSKB.source_version, domain=None, range=Optional[str])

slots.source_url = Slot(uri=SCHEMA.url, name="source_url", curie=SCHEMA.curie('url'),
                   model_uri=ALSKB.source_url, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.confidence = Slot(uri=ALSKB.confidence, name="confidence", curie=ALSKB.curie('confidence'),
                   model_uri=ALSKB.confidence, domain=None, range=Optional[float])

slots.evidence_type = Slot(uri=ECO['0000000'], name="evidence_type", curie=ECO.curie('0000000'),
                   model_uri=ALSKB.evidence_type, domain=None, range=Optional[Union[str, "EvidenceTypeEnum"]])

slots.evidence_source = Slot(uri=ALSKB.evidence_source, name="evidence_source", curie=ALSKB.curie('evidence_source'),
                   model_uri=ALSKB.evidence_source, domain=None, range=Optional[str])

slots.ingest_date = Slot(uri=ALSKB.ingest_date, name="ingest_date", curie=ALSKB.curie('ingest_date'),
                   model_uri=ALSKB.ingest_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.last_updated = Slot(uri=DCTERMS.modified, name="last_updated", curie=DCTERMS.curie('modified'),
                   model_uri=ALSKB.last_updated, domain=None, range=Optional[Union[str, XSDDate]])

slots.namedEntity__id = Slot(uri=SCHEMA.identifier, name="namedEntity__id", curie=SCHEMA.curie('identifier'),
                   model_uri=ALSKB.namedEntity__id, domain=None, range=str)

slots.namedEntity__label = Slot(uri=RDFS.label, name="namedEntity__label", curie=RDFS.curie('label'),
                   model_uri=ALSKB.namedEntity__label, domain=None, range=str)

slots.namedEntity__definition = Slot(uri=IAO['0000115'], name="namedEntity__definition", curie=IAO.curie('0000115'),
                   model_uri=ALSKB.namedEntity__definition, domain=None, range=Optional[str])

slots.namedEntity__synonym = Slot(uri=OBOINOWL.hasRelatedSynonym, name="namedEntity__synonym", curie=OBOINOWL.curie('hasRelatedSynonym'),
                   model_uri=ALSKB.namedEntity__synonym, domain=None, range=Optional[str])

slots.namedEntity__xref = Slot(uri=OBOINOWL.hasDbXref, name="namedEntity__xref", curie=OBOINOWL.curie('hasDbXref'),
                   model_uri=ALSKB.namedEntity__xref, domain=None, range=Optional[str])

slots.namedEntity__comment = Slot(uri=RDFS.comment, name="namedEntity__comment", curie=RDFS.curie('comment'),
                   model_uri=ALSKB.namedEntity__comment, domain=None, range=Optional[str])

slots.namedEntity__is_obsolete = Slot(uri=OWL.deprecated, name="namedEntity__is_obsolete", curie=OWL.curie('deprecated'),
                   model_uri=ALSKB.namedEntity__is_obsolete, domain=None, range=Optional[str])

slots.namedEntity__source = Slot(uri=DCTERMS.source, name="namedEntity__source", curie=DCTERMS.curie('source'),
                   model_uri=ALSKB.namedEntity__source, domain=None, range=Optional[str])

slots.namedEntity__last_updated = Slot(uri=DCTERMS.modified, name="namedEntity__last_updated", curie=DCTERMS.curie('modified'),
                   model_uri=ALSKB.namedEntity__last_updated, domain=None, range=Optional[str])

slots.ontologyClass__source_version = Slot(uri=DCTERMS.hasVersion, name="ontologyClass__source_version", curie=DCTERMS.curie('hasVersion'),
                   model_uri=ALSKB.ontologyClass__source_version, domain=None, range=Optional[str])

slots.ontologyClass__ingest_date = Slot(uri=ALSKB.ingest_date, name="ontologyClass__ingest_date", curie=ALSKB.curie('ingest_date'),
                   model_uri=ALSKB.ontologyClass__ingest_date, domain=None, range=Optional[str])

slots.relationship__subject = Slot(uri=RDF.subject, name="relationship__subject", curie=RDF.curie('subject'),
                   model_uri=ALSKB.relationship__subject, domain=None, range=str)

slots.relationship__predicate = Slot(uri=RDF.predicate, name="relationship__predicate", curie=RDF.curie('predicate'),
                   model_uri=ALSKB.relationship__predicate, domain=None, range=str)

slots.relationship__object = Slot(uri=RDF.object, name="relationship__object", curie=RDF.curie('object'),
                   model_uri=ALSKB.relationship__object, domain=None, range=str)

slots.relationship__source = Slot(uri=DCTERMS.source, name="relationship__source", curie=DCTERMS.curie('source'),
                   model_uri=ALSKB.relationship__source, domain=None, range=Optional[str])

slots.relationship__confidence = Slot(uri=ALSKB.confidence, name="relationship__confidence", curie=ALSKB.curie('confidence'),
                   model_uri=ALSKB.relationship__confidence, domain=None, range=Optional[str])

slots.relationship__evidence_type = Slot(uri=ECO['0000000'], name="relationship__evidence_type", curie=ECO.curie('0000000'),
                   model_uri=ALSKB.relationship__evidence_type, domain=None, range=Optional[str])

slots.relationship__evidence_source = Slot(uri=ALSKB.evidence_source, name="relationship__evidence_source", curie=ALSKB.curie('evidence_source'),
                   model_uri=ALSKB.relationship__evidence_source, domain=None, range=Optional[str])

slots.relationship__ingest_date = Slot(uri=ALSKB.ingest_date, name="relationship__ingest_date", curie=ALSKB.curie('ingest_date'),
                   model_uri=ALSKB.relationship__ingest_date, domain=None, range=Optional[str])

slots.diseaseOrPhenotype__mondo_id = Slot(uri=ALSKB.mondo_id, name="diseaseOrPhenotype__mondo_id", curie=ALSKB.curie('mondo_id'),
                   model_uri=ALSKB.diseaseOrPhenotype__mondo_id, domain=None, range=Optional[Union[str, MondoIdentifier]])

slots.diseaseOrPhenotype__hpo_id = Slot(uri=ALSKB.hpo_id, name="diseaseOrPhenotype__hpo_id", curie=ALSKB.curie('hpo_id'),
                   model_uri=ALSKB.diseaseOrPhenotype__hpo_id, domain=None, range=Optional[Union[str, HpoIdentifier]])

slots.disease__mondo_id = Slot(uri=ALSKB.mondo_id, name="disease__mondo_id", curie=ALSKB.curie('mondo_id'),
                   model_uri=ALSKB.disease__mondo_id, domain=None, range=URIRef)

slots.disease__name = Slot(uri=SCHEMA.name, name="disease__name", curie=SCHEMA.curie('name'),
                   model_uri=ALSKB.disease__name, domain=None, range=Optional[str])

slots.disease__disease_type = Slot(uri=ALSKB.disease_type, name="disease__disease_type", curie=ALSKB.curie('disease_type'),
                   model_uri=ALSKB.disease__disease_type, domain=None, range=Optional[Union[str, "DiseaseTypeEnum"]])

slots.disease__onset_type = Slot(uri=ALSKB.onset_type, name="disease__onset_type", curie=ALSKB.curie('onset_type'),
                   model_uri=ALSKB.disease__onset_type, domain=None, range=Optional[Union[str, "OnsetTypeEnum"]])

slots.disease__umls_cui = Slot(uri=ALSKB.umls_cui, name="disease__umls_cui", curie=ALSKB.curie('umls_cui'),
                   model_uri=ALSKB.disease__umls_cui, domain=None, range=Optional[str])

slots.disease__omim_id = Slot(uri=ALSKB.omim_id, name="disease__omim_id", curie=ALSKB.curie('omim_id'),
                   model_uri=ALSKB.disease__omim_id, domain=None, range=Optional[str])

slots.disease__orphanet_id = Slot(uri=ALSKB.orphanet_id, name="disease__orphanet_id", curie=ALSKB.curie('orphanet_id'),
                   model_uri=ALSKB.disease__orphanet_id, domain=None, range=Optional[str])

slots.disease__icd10_code = Slot(uri=ALSKB.icd10_code, name="disease__icd10_code", curie=ALSKB.curie('icd10_code'),
                   model_uri=ALSKB.disease__icd10_code, domain=None, range=Optional[str])

slots.phenotype__hpo_id = Slot(uri=ALSKB.hpo_id, name="phenotype__hpo_id", curie=ALSKB.curie('hpo_id'),
                   model_uri=ALSKB.phenotype__hpo_id, domain=None, range=URIRef)

slots.phenotype__frequency = Slot(uri=ALSKB.frequency, name="phenotype__frequency", curie=ALSKB.curie('frequency'),
                   model_uri=ALSKB.phenotype__frequency, domain=None, range=Optional[str])

slots.phenotype__severity = Slot(uri=ALSKB.severity, name="phenotype__severity", curie=ALSKB.curie('severity'),
                   model_uri=ALSKB.phenotype__severity, domain=None, range=Optional[str])

slots.anatomy__uberon_id = Slot(uri=ALSKB.uberon_id, name="anatomy__uberon_id", curie=ALSKB.curie('uberon_id'),
                   model_uri=ALSKB.anatomy__uberon_id, domain=None, range=URIRef)

slots.anatomy__bto_id = Slot(uri=ALSKB.bto_id, name="anatomy__bto_id", curie=ALSKB.curie('bto_id'),
                   model_uri=ALSKB.anatomy__bto_id, domain=None, range=Optional[str])

slots.anatomy__mesh_id = Slot(uri=ALSKB.mesh_id, name="anatomy__mesh_id", curie=ALSKB.curie('mesh_id'),
                   model_uri=ALSKB.anatomy__mesh_id, domain=None, range=Optional[str])

slots.anatomy__anatomical_system = Slot(uri=ALSKB.anatomical_system, name="anatomy__anatomical_system", curie=ALSKB.curie('anatomical_system'),
                   model_uri=ALSKB.anatomy__anatomical_system, domain=None, range=Optional[str])

slots.gene__ncbi_gene_id = Slot(uri=ALSKB.ncbi_gene_id, name="gene__ncbi_gene_id", curie=ALSKB.curie('ncbi_gene_id'),
                   model_uri=ALSKB.gene__ncbi_gene_id, domain=None, range=URIRef)

slots.gene__hgnc_symbol = Slot(uri=ALSKB.hgnc_symbol, name="gene__hgnc_symbol", curie=ALSKB.curie('hgnc_symbol'),
                   model_uri=ALSKB.gene__hgnc_symbol, domain=None, range=Optional[str])

slots.gene__ensembl_id = Slot(uri=ALSKB.ensembl_id, name="gene__ensembl_id", curie=ALSKB.curie('ensembl_id'),
                   model_uri=ALSKB.gene__ensembl_id, domain=None, range=Optional[str])

slots.gene__chromosome = Slot(uri=ALSKB.chromosome, name="gene__chromosome", curie=ALSKB.curie('chromosome'),
                   model_uri=ALSKB.gene__chromosome, domain=None, range=Optional[str])

slots.gene__genomic_pos_start = Slot(uri=ALSKB.genomic_pos_start, name="gene__genomic_pos_start", curie=ALSKB.curie('genomic_pos_start'),
                   model_uri=ALSKB.gene__genomic_pos_start, domain=None, range=Optional[int])

slots.gene__genomic_pos_end = Slot(uri=ALSKB.genomic_pos_end, name="gene__genomic_pos_end", curie=ALSKB.curie('genomic_pos_end'),
                   model_uri=ALSKB.gene__genomic_pos_end, domain=None, range=Optional[int])

slots.gene__als_risk_tier = Slot(uri=ALSKB.als_risk_tier, name="gene__als_risk_tier", curie=ALSKB.curie('als_risk_tier'),
                   model_uri=ALSKB.gene__als_risk_tier, domain=None, range=Optional[str])

slots.transcriptionFactor__tf_family = Slot(uri=ALSKB.tf_family, name="transcriptionFactor__tf_family", curie=ALSKB.curie('tf_family'),
                   model_uri=ALSKB.transcriptionFactor__tf_family, domain=None, range=Optional[str])

slots.transcriptionFactor__dorothea_confidence = Slot(uri=ALSKB.dorothea_confidence, name="transcriptionFactor__dorothea_confidence", curie=ALSKB.curie('dorothea_confidence'),
                   model_uri=ALSKB.transcriptionFactor__dorothea_confidence, domain=None, range=Optional[str])

slots.protein__uniprot_id = Slot(uri=UNIPROTKB[''], name="protein__uniprot_id", curie=UNIPROTKB.curie(''),
                   model_uri=ALSKB.protein__uniprot_id, domain=None, range=URIRef)

slots.protein__protein_name = Slot(uri=SCHEMA.name, name="protein__protein_name", curie=SCHEMA.curie('name'),
                   model_uri=ALSKB.protein__protein_name, domain=None, range=Optional[str])

slots.protein__hgnc_symbol = Slot(uri=ALSKB.hgnc_symbol, name="protein__hgnc_symbol", curie=ALSKB.curie('hgnc_symbol'),
                   model_uri=ALSKB.protein__hgnc_symbol, domain=None, range=Optional[str])

slots.protein__molecular_weight_kda = Slot(uri=ALSKB.molecular_weight_kda, name="protein__molecular_weight_kda", curie=ALSKB.curie('molecular_weight_kda'),
                   model_uri=ALSKB.protein__molecular_weight_kda, domain=None, range=Optional[float])

slots.protein__protein_family = Slot(uri=ALSKB.protein_family, name="protein__protein_family", curie=ALSKB.curie('protein_family'),
                   model_uri=ALSKB.protein__protein_family, domain=None, range=Optional[str])

slots.protein__subcellular_location = Slot(uri=ALSKB.subcellular_location, name="protein__subcellular_location", curie=ALSKB.curie('subcellular_location'),
                   model_uri=ALSKB.protein__subcellular_location, domain=None, range=Optional[Union[str, list[str]]])

slots.protein__aggregation_prone = Slot(uri=ALSKB.aggregation_prone, name="protein__aggregation_prone", curie=ALSKB.curie('aggregation_prone'),
                   model_uri=ALSKB.protein__aggregation_prone, domain=None, range=Optional[Union[bool, Bool]])

slots.protein__has_prion_like_domain = Slot(uri=ALSKB.has_prion_like_domain, name="protein__has_prion_like_domain", curie=ALSKB.curie('has_prion_like_domain'),
                   model_uri=ALSKB.protein__has_prion_like_domain, domain=None, range=Optional[Union[bool, Bool]])

slots.variant__clinvar_id = Slot(uri=ALSKB.clinvar_id, name="variant__clinvar_id", curie=ALSKB.curie('clinvar_id'),
                   model_uri=ALSKB.variant__clinvar_id, domain=None, range=URIRef)

slots.variant__rsid = Slot(uri=ALSKB.rsid, name="variant__rsid", curie=ALSKB.curie('rsid'),
                   model_uri=ALSKB.variant__rsid, domain=None, range=Optional[str])

slots.variant__hgvs_c = Slot(uri=ALSKB.hgvs_c, name="variant__hgvs_c", curie=ALSKB.curie('hgvs_c'),
                   model_uri=ALSKB.variant__hgvs_c, domain=None, range=Optional[str])

slots.variant__hgvs_p = Slot(uri=ALSKB.hgvs_p, name="variant__hgvs_p", curie=ALSKB.curie('hgvs_p'),
                   model_uri=ALSKB.variant__hgvs_p, domain=None, range=Optional[str])

slots.variant__variant_type = Slot(uri=ALSKB.variant_type, name="variant__variant_type", curie=ALSKB.curie('variant_type'),
                   model_uri=ALSKB.variant__variant_type, domain=None, range=Optional[Union[str, "VariantTypeEnum"]])

slots.variant__clinical_significance = Slot(uri=ALSKB.clinical_significance, name="variant__clinical_significance", curie=ALSKB.curie('clinical_significance'),
                   model_uri=ALSKB.variant__clinical_significance, domain=None, range=Optional[str])

slots.variant__als_class = Slot(uri=ALSKB.als_class, name="variant__als_class", curie=ALSKB.curie('als_class'),
                   model_uri=ALSKB.variant__als_class, domain=None, range=Optional[str])

slots.variant__maf = Slot(uri=ALSKB.maf, name="variant__maf", curie=ALSKB.curie('maf'),
                   model_uri=ALSKB.variant__maf, domain=None, range=Optional[float])

slots.drug__drugbank_id = Slot(uri=ALSKB.drugbank_id, name="drug__drugbank_id", curie=ALSKB.curie('drugbank_id'),
                   model_uri=ALSKB.drug__drugbank_id, domain=None, range=URIRef)

slots.drug__drug_name = Slot(uri=SCHEMA.name, name="drug__drug_name", curie=SCHEMA.curie('name'),
                   model_uri=ALSKB.drug__drug_name, domain=None, range=Optional[str])

slots.drug__chembl_id = Slot(uri=ALSKB.chembl_id, name="drug__chembl_id", curie=ALSKB.curie('chembl_id'),
                   model_uri=ALSKB.drug__chembl_id, domain=None, range=Optional[str])

slots.drug__inchi_key = Slot(uri=ALSKB.inchi_key, name="drug__inchi_key", curie=ALSKB.curie('inchi_key'),
                   model_uri=ALSKB.drug__inchi_key, domain=None, range=Optional[str])

slots.drug__smiles = Slot(uri=ALSKB.smiles, name="drug__smiles", curie=ALSKB.curie('smiles'),
                   model_uri=ALSKB.drug__smiles, domain=None, range=Optional[str])

slots.drug__drug_type = Slot(uri=ALSKB.drug_type, name="drug__drug_type", curie=ALSKB.curie('drug_type'),
                   model_uri=ALSKB.drug__drug_type, domain=None, range=Optional[str])

slots.drug__als_approved = Slot(uri=ALSKB.als_approved, name="drug__als_approved", curie=ALSKB.curie('als_approved'),
                   model_uri=ALSKB.drug__als_approved, domain=None, range=Optional[Union[bool, Bool]])

slots.drug__trial_status = Slot(uri=ALSKB.trial_status, name="drug__trial_status", curie=ALSKB.curie('trial_status'),
                   model_uri=ALSKB.drug__trial_status, domain=None, range=Optional[str])

slots.drug__mechanism = Slot(uri=ALSKB.mechanism, name="drug__mechanism", curie=ALSKB.curie('mechanism'),
                   model_uri=ALSKB.drug__mechanism, domain=None, range=Optional[str])

slots.drug__indication = Slot(uri=ALSKB.indication, name="drug__indication", curie=ALSKB.curie('indication'),
                   model_uri=ALSKB.drug__indication, domain=None, range=Optional[str])

slots.exposureOrStressor__ctd_id = Slot(uri=ALSKB.ctd_id, name="exposureOrStressor__ctd_id", curie=ALSKB.curie('ctd_id'),
                   model_uri=ALSKB.exposureOrStressor__ctd_id, domain=None, range=URIRef)

slots.exposureOrStressor__exposure_name = Slot(uri=SCHEMA.name, name="exposureOrStressor__exposure_name", curie=SCHEMA.curie('name'),
                   model_uri=ALSKB.exposureOrStressor__exposure_name, domain=None, range=Optional[str])

slots.exposureOrStressor__exposure_type = Slot(uri=ALSKB.exposure_type, name="exposureOrStressor__exposure_type", curie=ALSKB.curie('exposure_type'),
                   model_uri=ALSKB.exposureOrStressor__exposure_type, domain=None, range=Optional[str])

slots.exposureOrStressor__mesh_id = Slot(uri=ALSKB.mesh_id, name="exposureOrStressor__mesh_id", curie=ALSKB.curie('mesh_id'),
                   model_uri=ALSKB.exposureOrStressor__mesh_id, domain=None, range=Optional[str])

slots.exposureOrStressor__cas_number = Slot(uri=ALSKB.cas_number, name="exposureOrStressor__cas_number", curie=ALSKB.curie('cas_number'),
                   model_uri=ALSKB.exposureOrStressor__cas_number, domain=None, range=Optional[str])

slots.exposureOrStressor__als_relevance = Slot(uri=ALSKB.als_relevance, name="exposureOrStressor__als_relevance", curie=ALSKB.curie('als_relevance'),
                   model_uri=ALSKB.exposureOrStressor__als_relevance, domain=None, range=Optional[Union[bool, Bool]])

slots.biologicalProcess__go_id = Slot(uri=ALSKB.go_id, name="biologicalProcess__go_id", curie=ALSKB.curie('go_id'),
                   model_uri=ALSKB.biologicalProcess__go_id, domain=None, range=URIRef)

slots.biologicalProcess__process_name = Slot(uri=SCHEMA.name, name="biologicalProcess__process_name", curie=SCHEMA.curie('name'),
                   model_uri=ALSKB.biologicalProcess__process_name, domain=None, range=Optional[str])

slots.biologicalProcess__go_definition = Slot(uri=IAO['0000115'], name="biologicalProcess__go_definition", curie=IAO.curie('0000115'),
                   model_uri=ALSKB.biologicalProcess__go_definition, domain=None, range=Optional[str])

slots.molecularFunction__go_id = Slot(uri=ALSKB.go_id, name="molecularFunction__go_id", curie=ALSKB.curie('go_id'),
                   model_uri=ALSKB.molecularFunction__go_id, domain=None, range=URIRef)

slots.molecularFunction__function_name = Slot(uri=SCHEMA.name, name="molecularFunction__function_name", curie=SCHEMA.curie('name'),
                   model_uri=ALSKB.molecularFunction__function_name, domain=None, range=Optional[str])

slots.molecularFunction__go_definition = Slot(uri=IAO['0000115'], name="molecularFunction__go_definition", curie=IAO.curie('0000115'),
                   model_uri=ALSKB.molecularFunction__go_definition, domain=None, range=Optional[str])

slots.cellularComponent__go_id = Slot(uri=ALSKB.go_id, name="cellularComponent__go_id", curie=ALSKB.curie('go_id'),
                   model_uri=ALSKB.cellularComponent__go_id, domain=None, range=URIRef)

slots.cellularComponent__component_name = Slot(uri=SCHEMA.name, name="cellularComponent__component_name", curie=SCHEMA.curie('name'),
                   model_uri=ALSKB.cellularComponent__component_name, domain=None, range=Optional[str])

slots.cellularComponent__go_definition = Slot(uri=IAO['0000115'], name="cellularComponent__go_definition", curie=IAO.curie('0000115'),
                   model_uri=ALSKB.cellularComponent__go_definition, domain=None, range=Optional[str])

slots.pathway__reactome_id = Slot(uri=ALSKB.reactome_id, name="pathway__reactome_id", curie=ALSKB.curie('reactome_id'),
                   model_uri=ALSKB.pathway__reactome_id, domain=None, range=URIRef)

slots.pathway__pathway_name = Slot(uri=SCHEMA.name, name="pathway__pathway_name", curie=SCHEMA.curie('name'),
                   model_uri=ALSKB.pathway__pathway_name, domain=None, range=Optional[str])

slots.pathway__pathway_definition = Slot(uri=IAO['0000115'], name="pathway__pathway_definition", curie=IAO.curie('0000115'),
                   model_uri=ALSKB.pathway__pathway_definition, domain=None, range=Optional[str])

slots.pathway__species = Slot(uri=ALSKB.species, name="pathway__species", curie=ALSKB.curie('species'),
                   model_uri=ALSKB.pathway__species, domain=None, range=Optional[str])

slots.pathway__parent_pathway = Slot(uri=ALSKB.parent_pathway, name="pathway__parent_pathway", curie=ALSKB.curie('parent_pathway'),
                   model_uri=ALSKB.pathway__parent_pathway, domain=None, range=Optional[Union[Union[str, ReactomeIdentifier], list[Union[str, ReactomeIdentifier]]]])

slots.diseaseSubtype__subtype_id = Slot(uri=ALSKB.subtype_id, name="diseaseSubtype__subtype_id", curie=ALSKB.curie('subtype_id'),
                   model_uri=ALSKB.diseaseSubtype__subtype_id, domain=None, range=Optional[str])

slots.diseaseSubtype__cluster_method = Slot(uri=ALSKB.cluster_method, name="diseaseSubtype__cluster_method", curie=ALSKB.curie('cluster_method'),
                   model_uri=ALSKB.diseaseSubtype__cluster_method, domain=None, range=Optional[str])

slots.diseaseSubtype__cluster_id = Slot(uri=ALSKB.cluster_id, name="diseaseSubtype__cluster_id", curie=ALSKB.curie('cluster_id'),
                   model_uri=ALSKB.diseaseSubtype__cluster_id, domain=None, range=Optional[int])

slots.diseaseSubtype__signature_genes = Slot(uri=ALSKB.signature_genes, name="diseaseSubtype__signature_genes", curie=ALSKB.curie('signature_genes'),
                   model_uri=ALSKB.diseaseSubtype__signature_genes, domain=None, range=Optional[Union[str, list[str]]])

slots.diseaseSubtype__n_patients = Slot(uri=ALSKB.n_patients, name="diseaseSubtype__n_patients", curie=ALSKB.curie('n_patients'),
                   model_uri=ALSKB.diseaseSubtype__n_patients, domain=None, range=Optional[int])

slots.diseaseSubtype__cohort = Slot(uri=ALSKB.cohort, name="diseaseSubtype__cohort", curie=ALSKB.curie('cohort'),
                   model_uri=ALSKB.diseaseSubtype__cohort, domain=None, range=Optional[str])

slots.diseaseSubtype__clinical_correlate = Slot(uri=ALSKB.clinical_correlate, name="diseaseSubtype__clinical_correlate", curie=ALSKB.curie('clinical_correlate'),
                   model_uri=ALSKB.diseaseSubtype__clinical_correlate, domain=None, range=Optional[str])

slots.diseaseSubtype__median_survival_months = Slot(uri=ALSKB.median_survival_months, name="diseaseSubtype__median_survival_months", curie=ALSKB.curie('median_survival_months'),
                   model_uri=ALSKB.diseaseSubtype__median_survival_months, domain=None, range=Optional[float])

slots.diseaseSubtype__source_publication = Slot(uri=DCTERMS.bibliographicCitation, name="diseaseSubtype__source_publication", curie=DCTERMS.curie('bibliographicCitation'),
                   model_uri=ALSKB.diseaseSubtype__source_publication, domain=None, range=Optional[str])

slots.association__association_id = Slot(uri=SCHEMA.identifier, name="association__association_id", curie=SCHEMA.curie('identifier'),
                   model_uri=ALSKB.association__association_id, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.association__association_label = Slot(uri=RDFS.label, name="association__association_label", curie=RDFS.curie('label'),
                   model_uri=ALSKB.association__association_label, domain=None, range=Optional[str])

slots.association__subject = Slot(uri=RDF.subject, name="association__subject", curie=RDF.curie('subject'),
                   model_uri=ALSKB.association__subject, domain=None, range=str)

slots.association__predicate = Slot(uri=RDF.predicate, name="association__predicate", curie=RDF.curie('predicate'),
                   model_uri=ALSKB.association__predicate, domain=None, range=str)

slots.association__object = Slot(uri=RDF.object, name="association__object", curie=RDF.curie('object'),
                   model_uri=ALSKB.association__object, domain=None, range=str)

slots.association__source = Slot(uri=DCTERMS.source, name="association__source", curie=DCTERMS.curie('source'),
                   model_uri=ALSKB.association__source, domain=None, range=Optional[str])

slots.association__source_version = Slot(uri=DCTERMS.hasVersion, name="association__source_version", curie=DCTERMS.curie('hasVersion'),
                   model_uri=ALSKB.association__source_version, domain=None, range=Optional[str])

slots.association__evidence_type = Slot(uri=ECO['0000000'], name="association__evidence_type", curie=ECO.curie('0000000'),
                   model_uri=ALSKB.association__evidence_type, domain=None, range=Optional[str])

slots.association__evidence_source = Slot(uri=ALSKB.evidence_source, name="association__evidence_source", curie=ALSKB.curie('evidence_source'),
                   model_uri=ALSKB.association__evidence_source, domain=None, range=Optional[str])

slots.association__confidence = Slot(uri=ALSKB.confidence, name="association__confidence", curie=ALSKB.curie('confidence'),
                   model_uri=ALSKB.association__confidence, domain=None, range=Optional[str])

slots.association__ingest_date = Slot(uri=ALSKB.ingest_date, name="association__ingest_date", curie=ALSKB.curie('ingest_date'),
                   model_uri=ALSKB.association__ingest_date, domain=None, range=Optional[str])

slots.association__last_updated = Slot(uri=DCTERMS.modified, name="association__last_updated", curie=DCTERMS.curie('modified'),
                   model_uri=ALSKB.association__last_updated, domain=None, range=Optional[str])

slots.diseasePhenotypeAssociation__has_disease = Slot(uri=ALSKB.has_disease, name="diseasePhenotypeAssociation__has_disease", curie=ALSKB.curie('has_disease'),
                   model_uri=ALSKB.diseasePhenotypeAssociation__has_disease, domain=None, range=Union[str, DiseaseMondoId])

slots.diseasePhenotypeAssociation__has_phenotype = Slot(uri=ALSKB.has_phenotype, name="diseasePhenotypeAssociation__has_phenotype", curie=ALSKB.curie('has_phenotype'),
                   model_uri=ALSKB.diseasePhenotypeAssociation__has_phenotype, domain=None, range=Union[str, PhenotypeHpoId])

slots.diseasePhenotypeAssociation__predicate = Slot(uri=RDF.predicate, name="diseasePhenotypeAssociation__predicate", curie=RDF.curie('predicate'),
                   model_uri=ALSKB.diseasePhenotypeAssociation__predicate, domain=None, range=Optional[str])

slots.diseasePhenotypeAssociation__frequency = Slot(uri=ALSKB.frequency, name="diseasePhenotypeAssociation__frequency", curie=ALSKB.curie('frequency'),
                   model_uri=ALSKB.diseasePhenotypeAssociation__frequency, domain=None, range=Optional[str])

slots.diseasePhenotypeAssociation__severity = Slot(uri=ALSKB.severity, name="diseasePhenotypeAssociation__severity", curie=ALSKB.curie('severity'),
                   model_uri=ALSKB.diseasePhenotypeAssociation__severity, domain=None, range=Optional[str])

slots.diseasePhenotypeAssociation__onset_type = Slot(uri=ALSKB.onset_type, name="diseasePhenotypeAssociation__onset_type", curie=ALSKB.curie('onset_type'),
                   model_uri=ALSKB.diseasePhenotypeAssociation__onset_type, domain=None, range=Optional[Union[str, "OnsetTypeEnum"]])

slots.diseasePhenotypeAssociation__cohort = Slot(uri=ALSKB.cohort, name="diseasePhenotypeAssociation__cohort", curie=ALSKB.curie('cohort'),
                   model_uri=ALSKB.diseasePhenotypeAssociation__cohort, domain=None, range=Optional[str])

slots.geneDiseaseAssociation__has_gene = Slot(uri=ALSKB.has_gene, name="geneDiseaseAssociation__has_gene", curie=ALSKB.curie('has_gene'),
                   model_uri=ALSKB.geneDiseaseAssociation__has_gene, domain=None, range=Union[str, GeneNcbiGeneId])

slots.geneDiseaseAssociation__has_disease = Slot(uri=ALSKB.has_disease, name="geneDiseaseAssociation__has_disease", curie=ALSKB.curie('has_disease'),
                   model_uri=ALSKB.geneDiseaseAssociation__has_disease, domain=None, range=Union[str, DiseaseMondoId])

slots.geneDiseaseAssociation__predicate = Slot(uri=RDF.predicate, name="geneDiseaseAssociation__predicate", curie=RDF.curie('predicate'),
                   model_uri=ALSKB.geneDiseaseAssociation__predicate, domain=None, range=Optional[str])

slots.geneDiseaseAssociation__association_type = Slot(uri=ALSKB.association_type, name="geneDiseaseAssociation__association_type", curie=ALSKB.curie('association_type'),
                   model_uri=ALSKB.geneDiseaseAssociation__association_type, domain=None, range=Optional[str])

slots.geneDiseaseAssociation__association_score = Slot(uri=ALSKB.association_score, name="geneDiseaseAssociation__association_score", curie=ALSKB.curie('association_score'),
                   model_uri=ALSKB.geneDiseaseAssociation__association_score, domain=None, range=Optional[float])

slots.geneDiseaseAssociation__p_value = Slot(uri=ALSKB.p_value, name="geneDiseaseAssociation__p_value", curie=ALSKB.curie('p_value'),
                   model_uri=ALSKB.geneDiseaseAssociation__p_value, domain=None, range=Optional[float])

slots.geneDiseaseAssociation__odds_ratio = Slot(uri=ALSKB.odds_ratio, name="geneDiseaseAssociation__odds_ratio", curie=ALSKB.curie('odds_ratio'),
                   model_uri=ALSKB.geneDiseaseAssociation__odds_ratio, domain=None, range=Optional[float])

slots.geneDiseaseAssociation__effect_direction = Slot(uri=ALSKB.effect_direction, name="geneDiseaseAssociation__effect_direction", curie=ALSKB.curie('effect_direction'),
                   model_uri=ALSKB.geneDiseaseAssociation__effect_direction, domain=None, range=Optional[str])

slots.geneDiseaseAssociation__evidence_count = Slot(uri=ALSKB.evidence_count, name="geneDiseaseAssociation__evidence_count", curie=ALSKB.curie('evidence_count'),
                   model_uri=ALSKB.geneDiseaseAssociation__evidence_count, domain=None, range=Optional[int])

slots.variantDiseaseAssociation__has_variant = Slot(uri=ALSKB.has_variant, name="variantDiseaseAssociation__has_variant", curie=ALSKB.curie('has_variant'),
                   model_uri=ALSKB.variantDiseaseAssociation__has_variant, domain=None, range=Union[str, VariantClinvarId])

slots.variantDiseaseAssociation__has_disease = Slot(uri=ALSKB.has_disease, name="variantDiseaseAssociation__has_disease", curie=ALSKB.curie('has_disease'),
                   model_uri=ALSKB.variantDiseaseAssociation__has_disease, domain=None, range=Union[str, DiseaseMondoId])

slots.variantDiseaseAssociation__predicate = Slot(uri=RDF.predicate, name="variantDiseaseAssociation__predicate", curie=RDF.curie('predicate'),
                   model_uri=ALSKB.variantDiseaseAssociation__predicate, domain=None, range=Optional[str])

slots.variantDiseaseAssociation__clinical_significance = Slot(uri=ALSKB.clinical_significance, name="variantDiseaseAssociation__clinical_significance", curie=ALSKB.curie('clinical_significance'),
                   model_uri=ALSKB.variantDiseaseAssociation__clinical_significance, domain=None, range=Optional[str])

slots.variantDiseaseAssociation__inheritance_mode = Slot(uri=ALSKB.inheritance_mode, name="variantDiseaseAssociation__inheritance_mode", curie=ALSKB.curie('inheritance_mode'),
                   model_uri=ALSKB.variantDiseaseAssociation__inheritance_mode, domain=None, range=Optional[str])

slots.variantDiseaseAssociation__penetrance = Slot(uri=ALSKB.penetrance, name="variantDiseaseAssociation__penetrance", curie=ALSKB.curie('penetrance'),
                   model_uri=ALSKB.variantDiseaseAssociation__penetrance, domain=None, range=Optional[str])

slots.variantDiseaseAssociation__association_type = Slot(uri=ALSKB.association_type, name="variantDiseaseAssociation__association_type", curie=ALSKB.curie('association_type'),
                   model_uri=ALSKB.variantDiseaseAssociation__association_type, domain=None, range=Optional[str])

slots.variantProteinEffectAssociation__has_variant = Slot(uri=ALSKB.has_variant, name="variantProteinEffectAssociation__has_variant", curie=ALSKB.curie('has_variant'),
                   model_uri=ALSKB.variantProteinEffectAssociation__has_variant, domain=None, range=Union[str, VariantClinvarId])

slots.variantProteinEffectAssociation__has_protein = Slot(uri=ALSKB.has_protein, name="variantProteinEffectAssociation__has_protein", curie=ALSKB.curie('has_protein'),
                   model_uri=ALSKB.variantProteinEffectAssociation__has_protein, domain=None, range=Union[str, ProteinUniprotId])

slots.variantProteinEffectAssociation__predicate = Slot(uri=RDF.predicate, name="variantProteinEffectAssociation__predicate", curie=RDF.curie('predicate'),
                   model_uri=ALSKB.variantProteinEffectAssociation__predicate, domain=None, range=Optional[str])

slots.variantProteinEffectAssociation__functional_consequence = Slot(uri=ALSKB.functional_consequence, name="variantProteinEffectAssociation__functional_consequence", curie=ALSKB.curie('functional_consequence'),
                   model_uri=ALSKB.variantProteinEffectAssociation__functional_consequence, domain=None, range=Optional[str])

slots.variantProteinEffectAssociation__predicted_effect = Slot(uri=ALSKB.predicted_effect, name="variantProteinEffectAssociation__predicted_effect", curie=ALSKB.curie('predicted_effect'),
                   model_uri=ALSKB.variantProteinEffectAssociation__predicted_effect, domain=None, range=Optional[str])

slots.variantProteinEffectAssociation__assay = Slot(uri=ALSKB.assay, name="variantProteinEffectAssociation__assay", curie=ALSKB.curie('assay'),
                   model_uri=ALSKB.variantProteinEffectAssociation__assay, domain=None, range=Optional[str])

slots.proteinProteinInteractionAssociation__protein_1 = Slot(uri=ALSKB.protein_1, name="proteinProteinInteractionAssociation__protein_1", curie=ALSKB.curie('protein_1'),
                   model_uri=ALSKB.proteinProteinInteractionAssociation__protein_1, domain=None, range=Union[str, ProteinUniprotId])

slots.proteinProteinInteractionAssociation__protein_2 = Slot(uri=ALSKB.protein_2, name="proteinProteinInteractionAssociation__protein_2", curie=ALSKB.curie('protein_2'),
                   model_uri=ALSKB.proteinProteinInteractionAssociation__protein_2, domain=None, range=Union[str, ProteinUniprotId])

slots.proteinProteinInteractionAssociation__predicate = Slot(uri=RDF.predicate, name="proteinProteinInteractionAssociation__predicate", curie=RDF.curie('predicate'),
                   model_uri=ALSKB.proteinProteinInteractionAssociation__predicate, domain=None, range=Optional[str])

slots.proteinProteinInteractionAssociation__interaction_score = Slot(uri=ALSKB.interaction_score, name="proteinProteinInteractionAssociation__interaction_score", curie=ALSKB.curie('interaction_score'),
                   model_uri=ALSKB.proteinProteinInteractionAssociation__interaction_score, domain=None, range=Optional[float])

slots.proteinProteinInteractionAssociation__interaction_type = Slot(uri=ALSKB.interaction_type, name="proteinProteinInteractionAssociation__interaction_type", curie=ALSKB.curie('interaction_type'),
                   model_uri=ALSKB.proteinProteinInteractionAssociation__interaction_type, domain=None, range=Optional[str])

slots.proteinProteinInteractionAssociation__assay = Slot(uri=ALSKB.assay, name="proteinProteinInteractionAssociation__assay", curie=ALSKB.curie('assay'),
                   model_uri=ALSKB.proteinProteinInteractionAssociation__assay, domain=None, range=Optional[str])

slots.proteinPathwayAssociation__has_protein = Slot(uri=ALSKB.has_protein, name="proteinPathwayAssociation__has_protein", curie=ALSKB.curie('has_protein'),
                   model_uri=ALSKB.proteinPathwayAssociation__has_protein, domain=None, range=Union[str, ProteinUniprotId])

slots.proteinPathwayAssociation__has_pathway = Slot(uri=ALSKB.has_pathway, name="proteinPathwayAssociation__has_pathway", curie=ALSKB.curie('has_pathway'),
                   model_uri=ALSKB.proteinPathwayAssociation__has_pathway, domain=None, range=Union[str, PathwayReactomeId])

slots.proteinPathwayAssociation__predicate = Slot(uri=RDF.predicate, name="proteinPathwayAssociation__predicate", curie=RDF.curie('predicate'),
                   model_uri=ALSKB.proteinPathwayAssociation__predicate, domain=None, range=Optional[str])

slots.proteinPathwayAssociation__reactome_evidence_code = Slot(uri=ALSKB.reactome_evidence_code, name="proteinPathwayAssociation__reactome_evidence_code", curie=ALSKB.curie('reactome_evidence_code'),
                   model_uri=ALSKB.proteinPathwayAssociation__reactome_evidence_code, domain=None, range=Optional[str])

slots.proteinPathwayAssociation__pathway_role = Slot(uri=ALSKB.pathway_role, name="proteinPathwayAssociation__pathway_role", curie=ALSKB.curie('pathway_role'),
                   model_uri=ALSKB.proteinPathwayAssociation__pathway_role, domain=None, range=Optional[str])

slots.proteinPathwayAssociation__species = Slot(uri=ALSKB.species, name="proteinPathwayAssociation__species", curie=ALSKB.curie('species'),
                   model_uri=ALSKB.proteinPathwayAssociation__species, domain=None, range=Optional[str])

slots.drugTargetAssociation__has_drug = Slot(uri=ALSKB.has_drug, name="drugTargetAssociation__has_drug", curie=ALSKB.curie('has_drug'),
                   model_uri=ALSKB.drugTargetAssociation__has_drug, domain=None, range=Union[str, DrugDrugbankId])

slots.drugTargetAssociation__target = Slot(uri=ALSKB.target, name="drugTargetAssociation__target", curie=ALSKB.curie('target'),
                   model_uri=ALSKB.drugTargetAssociation__target, domain=None, range=Union[dict, MolecularEntity])

slots.drugTargetAssociation__predicate = Slot(uri=RDF.predicate, name="drugTargetAssociation__predicate", curie=RDF.curie('predicate'),
                   model_uri=ALSKB.drugTargetAssociation__predicate, domain=None, range=Optional[str])

slots.drugTargetAssociation__action_type = Slot(uri=ALSKB.action_type, name="drugTargetAssociation__action_type", curie=ALSKB.curie('action_type'),
                   model_uri=ALSKB.drugTargetAssociation__action_type, domain=None, range=Optional[str])

slots.drugTargetAssociation__binding_affinity_nm = Slot(uri=ALSKB.binding_affinity_nm, name="drugTargetAssociation__binding_affinity_nm", curie=ALSKB.curie('binding_affinity_nm'),
                   model_uri=ALSKB.drugTargetAssociation__binding_affinity_nm, domain=None, range=Optional[float])

slots.drugTargetAssociation__mechanism = Slot(uri=ALSKB.mechanism, name="drugTargetAssociation__mechanism", curie=ALSKB.curie('mechanism'),
                   model_uri=ALSKB.drugTargetAssociation__mechanism, domain=None, range=Optional[str])

slots.drugDiseaseTherapeuticAssociation__has_drug = Slot(uri=ALSKB.has_drug, name="drugDiseaseTherapeuticAssociation__has_drug", curie=ALSKB.curie('has_drug'),
                   model_uri=ALSKB.drugDiseaseTherapeuticAssociation__has_drug, domain=None, range=Union[str, DrugDrugbankId])

slots.drugDiseaseTherapeuticAssociation__has_disease = Slot(uri=ALSKB.has_disease, name="drugDiseaseTherapeuticAssociation__has_disease", curie=ALSKB.curie('has_disease'),
                   model_uri=ALSKB.drugDiseaseTherapeuticAssociation__has_disease, domain=None, range=Union[str, DiseaseMondoId])

slots.drugDiseaseTherapeuticAssociation__predicate = Slot(uri=RDF.predicate, name="drugDiseaseTherapeuticAssociation__predicate", curie=RDF.curie('predicate'),
                   model_uri=ALSKB.drugDiseaseTherapeuticAssociation__predicate, domain=None, range=Optional[str])

slots.drugDiseaseTherapeuticAssociation__relation_type = Slot(uri=ALSKB.relation_type, name="drugDiseaseTherapeuticAssociation__relation_type", curie=ALSKB.curie('relation_type'),
                   model_uri=ALSKB.drugDiseaseTherapeuticAssociation__relation_type, domain=None, range=Optional[str])

slots.drugDiseaseTherapeuticAssociation__approval_status = Slot(uri=ALSKB.approval_status, name="drugDiseaseTherapeuticAssociation__approval_status", curie=ALSKB.curie('approval_status'),
                   model_uri=ALSKB.drugDiseaseTherapeuticAssociation__approval_status, domain=None, range=Optional[str])

slots.drugDiseaseTherapeuticAssociation__clinical_phase = Slot(uri=ALSKB.clinical_phase, name="drugDiseaseTherapeuticAssociation__clinical_phase", curie=ALSKB.curie('clinical_phase'),
                   model_uri=ALSKB.drugDiseaseTherapeuticAssociation__clinical_phase, domain=None, range=Optional[str])

slots.drugDiseaseTherapeuticAssociation__outcome_measure = Slot(uri=ALSKB.outcome_measure, name="drugDiseaseTherapeuticAssociation__outcome_measure", curie=ALSKB.curie('outcome_measure'),
                   model_uri=ALSKB.drugDiseaseTherapeuticAssociation__outcome_measure, domain=None, range=Optional[str])

slots.exposureDiseaseAssociation__exposure = Slot(uri=ALSKB.exposure, name="exposureDiseaseAssociation__exposure", curie=ALSKB.curie('exposure'),
                   model_uri=ALSKB.exposureDiseaseAssociation__exposure, domain=None, range=Union[str, ExposureOrStressorCtdId])

slots.exposureDiseaseAssociation__has_disease = Slot(uri=ALSKB.has_disease, name="exposureDiseaseAssociation__has_disease", curie=ALSKB.curie('has_disease'),
                   model_uri=ALSKB.exposureDiseaseAssociation__has_disease, domain=None, range=Union[str, DiseaseMondoId])

slots.exposureDiseaseAssociation__predicate = Slot(uri=RDF.predicate, name="exposureDiseaseAssociation__predicate", curie=RDF.curie('predicate'),
                   model_uri=ALSKB.exposureDiseaseAssociation__predicate, domain=None, range=Optional[str])

slots.exposureDiseaseAssociation__association_type = Slot(uri=ALSKB.association_type, name="exposureDiseaseAssociation__association_type", curie=ALSKB.curie('association_type'),
                   model_uri=ALSKB.exposureDiseaseAssociation__association_type, domain=None, range=Optional[str])

slots.exposureDiseaseAssociation__mechanism = Slot(uri=ALSKB.mechanism, name="exposureDiseaseAssociation__mechanism", curie=ALSKB.curie('mechanism'),
                   model_uri=ALSKB.exposureDiseaseAssociation__mechanism, domain=None, range=Optional[str])

slots.exposureDiseaseAssociation__epidemiological_support = Slot(uri=ALSKB.epidemiological_support, name="exposureDiseaseAssociation__epidemiological_support", curie=ALSKB.curie('epidemiological_support'),
                   model_uri=ALSKB.exposureDiseaseAssociation__epidemiological_support, domain=None, range=Optional[Union[bool, Bool]])

slots.exposureDiseaseAssociation__odds_ratio = Slot(uri=ALSKB.odds_ratio, name="exposureDiseaseAssociation__odds_ratio", curie=ALSKB.curie('odds_ratio'),
                   model_uri=ALSKB.exposureDiseaseAssociation__odds_ratio, domain=None, range=Optional[float])

slots.exposureDiseaseAssociation__population = Slot(uri=ALSKB.population, name="exposureDiseaseAssociation__population", curie=ALSKB.curie('population'),
                   model_uri=ALSKB.exposureDiseaseAssociation__population, domain=None, range=Optional[str])

slots.transcriptionFactorRegulationAssociation__transcription_factor = Slot(uri=ALSKB.transcription_factor, name="transcriptionFactorRegulationAssociation__transcription_factor", curie=ALSKB.curie('transcription_factor'),
                   model_uri=ALSKB.transcriptionFactorRegulationAssociation__transcription_factor, domain=None, range=Union[str, TranscriptionFactorNcbiGeneId])

slots.transcriptionFactorRegulationAssociation__target_gene = Slot(uri=ALSKB.target_gene, name="transcriptionFactorRegulationAssociation__target_gene", curie=ALSKB.curie('target_gene'),
                   model_uri=ALSKB.transcriptionFactorRegulationAssociation__target_gene, domain=None, range=Union[str, GeneNcbiGeneId])

slots.transcriptionFactorRegulationAssociation__predicate = Slot(uri=RDF.predicate, name="transcriptionFactorRegulationAssociation__predicate", curie=RDF.curie('predicate'),
                   model_uri=ALSKB.transcriptionFactorRegulationAssociation__predicate, domain=None, range=Optional[str])

slots.transcriptionFactorRegulationAssociation__regulation_type = Slot(uri=ALSKB.regulation_type, name="transcriptionFactorRegulationAssociation__regulation_type", curie=ALSKB.curie('regulation_type'),
                   model_uri=ALSKB.transcriptionFactorRegulationAssociation__regulation_type, domain=None, range=Optional[str])

slots.transcriptionFactorRegulationAssociation__confidence_level = Slot(uri=ALSKB.confidence_level, name="transcriptionFactorRegulationAssociation__confidence_level", curie=ALSKB.curie('confidence_level'),
                   model_uri=ALSKB.transcriptionFactorRegulationAssociation__confidence_level, domain=None, range=Optional[str])

slots.transcriptionFactorRegulationAssociation__tissue_or_cell_type = Slot(uri=ALSKB.tissue_or_cell_type, name="transcriptionFactorRegulationAssociation__tissue_or_cell_type", curie=ALSKB.curie('tissue_or_cell_type'),
                   model_uri=ALSKB.transcriptionFactorRegulationAssociation__tissue_or_cell_type, domain=None, range=Optional[str])

slots.geneExpressionAssociation__has_gene = Slot(uri=ALSKB.has_gene, name="geneExpressionAssociation__has_gene", curie=ALSKB.curie('has_gene'),
                   model_uri=ALSKB.geneExpressionAssociation__has_gene, domain=None, range=Union[str, GeneNcbiGeneId])

slots.geneExpressionAssociation__has_anatomy = Slot(uri=ALSKB.has_anatomy, name="geneExpressionAssociation__has_anatomy", curie=ALSKB.curie('has_anatomy'),
                   model_uri=ALSKB.geneExpressionAssociation__has_anatomy, domain=None, range=Union[str, AnatomyUberonId])

slots.geneExpressionAssociation__predicate = Slot(uri=RDF.predicate, name="geneExpressionAssociation__predicate", curie=RDF.curie('predicate'),
                   model_uri=ALSKB.geneExpressionAssociation__predicate, domain=None, range=Optional[str])

slots.geneExpressionAssociation__expression_level = Slot(uri=ALSKB.expression_level, name="geneExpressionAssociation__expression_level", curie=ALSKB.curie('expression_level'),
                   model_uri=ALSKB.geneExpressionAssociation__expression_level, domain=None, range=Optional[str])

slots.geneExpressionAssociation__specificity_index = Slot(uri=ALSKB.specificity_index, name="geneExpressionAssociation__specificity_index", curie=ALSKB.curie('specificity_index'),
                   model_uri=ALSKB.geneExpressionAssociation__specificity_index, domain=None, range=Optional[float])

slots.geneExpressionAssociation__log2_fold_change = Slot(uri=ALSKB.log2_fold_change, name="geneExpressionAssociation__log2_fold_change", curie=ALSKB.curie('log2_fold_change'),
                   model_uri=ALSKB.geneExpressionAssociation__log2_fold_change, domain=None, range=Optional[float])

slots.geneExpressionAssociation__adjusted_p_value = Slot(uri=ALSKB.adjusted_p_value, name="geneExpressionAssociation__adjusted_p_value", curie=ALSKB.curie('adjusted_p_value'),
                   model_uri=ALSKB.geneExpressionAssociation__adjusted_p_value, domain=None, range=Optional[float])

slots.geneExpressionAssociation__tissue_or_cell_type = Slot(uri=ALSKB.tissue_or_cell_type, name="geneExpressionAssociation__tissue_or_cell_type", curie=ALSKB.curie('tissue_or_cell_type'),
                   model_uri=ALSKB.geneExpressionAssociation__tissue_or_cell_type, domain=None, range=Optional[str])

slots.geneExpressionAssociation__disease_stage = Slot(uri=ALSKB.disease_stage, name="geneExpressionAssociation__disease_stage", curie=ALSKB.curie('disease_stage'),
                   model_uri=ALSKB.geneExpressionAssociation__disease_stage, domain=None, range=Optional[str])

slots.diseaseDiseaseAssociation__disease_1 = Slot(uri=ALSKB.disease_1, name="diseaseDiseaseAssociation__disease_1", curie=ALSKB.curie('disease_1'),
                   model_uri=ALSKB.diseaseDiseaseAssociation__disease_1, domain=None, range=Union[str, DiseaseMondoId])

slots.diseaseDiseaseAssociation__disease_2 = Slot(uri=ALSKB.disease_2, name="diseaseDiseaseAssociation__disease_2", curie=ALSKB.curie('disease_2'),
                   model_uri=ALSKB.diseaseDiseaseAssociation__disease_2, domain=None, range=Union[str, DiseaseMondoId])

slots.diseaseDiseaseAssociation__predicate = Slot(uri=RDF.predicate, name="diseaseDiseaseAssociation__predicate", curie=RDF.curie('predicate'),
                   model_uri=ALSKB.diseaseDiseaseAssociation__predicate, domain=None, range=Optional[str])

slots.diseaseDiseaseAssociation__relation_type = Slot(uri=ALSKB.relation_type, name="diseaseDiseaseAssociation__relation_type", curie=ALSKB.curie('relation_type'),
                   model_uri=ALSKB.diseaseDiseaseAssociation__relation_type, domain=None, range=Optional[str])

slots.diseaseDiseaseAssociation__similarity_score = Slot(uri=ALSKB.similarity_score, name="diseaseDiseaseAssociation__similarity_score", curie=ALSKB.curie('similarity_score'),
                   model_uri=ALSKB.diseaseDiseaseAssociation__similarity_score, domain=None, range=Optional[float])

slots.diseaseDiseaseAssociation__shared_mechanism = Slot(uri=ALSKB.shared_mechanism, name="diseaseDiseaseAssociation__shared_mechanism", curie=ALSKB.curie('shared_mechanism'),
                   model_uri=ALSKB.diseaseDiseaseAssociation__shared_mechanism, domain=None, range=Optional[str])
