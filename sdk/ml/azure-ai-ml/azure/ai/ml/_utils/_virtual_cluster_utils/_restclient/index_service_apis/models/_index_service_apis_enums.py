# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.6.2, generator: @autorest/python@5.12.6)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from six import with_metaclass
from azure.core import CaseInsensitiveEnumMeta


class AssetContainerTypeFeedRename(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    WORKSPACE = "Workspace"
    FEED = "Feed"
    REGISTRY = "Registry"


class BatchendpointsUnversionedEntityKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    INVALID = "Invalid"
    LINEAGE_ROOT = "LineageRoot"
    VERSIONED = "Versioned"
    UNVERSIONED = "Unversioned"


class DatasetsVersionedEntityKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    INVALID = "Invalid"
    LINEAGE_ROOT = "LineageRoot"
    VERSIONED = "Versioned"
    UNVERSIONED = "Unversioned"


class DataStoreAnnotationsDataStoreType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    AZURE_BLOB = "AzureBlob"
    AZURE_FILE = "AzureFile"
    GLUSTER_FS = "GlusterFs"
    AZURE_DATA_LAKE = "AzureDataLake"
    AZURE_MY_SQL = "AzureMySql"
    CUSTOM = "Custom"
    HDFS = "Hdfs"
    AZURE_SQL_DATABASE = "AzureSqlDatabase"
    AZURE_POSTGRE_SQL = "AzurePostgreSql"
    DBFS = "DBFS"
    AZURE_DATA_LAKE_GEN2 = "AzureDataLakeGen2"


class DatastoresUnversionedEntityKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    INVALID = "Invalid"
    LINEAGE_ROOT = "LineageRoot"
    VERSIONED = "Versioned"
    UNVERSIONED = "Unversioned"


class EntityKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    INVALID = "Invalid"
    LINEAGE_ROOT = "LineageRoot"
    VERSIONED = "Versioned"
    UNVERSIONED = "Unversioned"


class EnvironmentsVersionedEntityKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    INVALID = "Invalid"
    LINEAGE_ROOT = "LineageRoot"
    VERSIONED = "Versioned"
    UNVERSIONED = "Unversioned"


class ExperimentStatusCode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    NOT_STARTED = "NotStarted"
    RUNNING = "Running"
    FAILED = "Failed"
    FINISHED = "Finished"
    CANCELED = "Canceled"
    FAILING = "Failing"


class FeatureDataType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    STRING = "String"
    INTEGER = "Integer"
    LONG = "Long"
    FLOAT = "Float"
    DOUBLE = "Double"
    BINARY = "Binary"
    DATETIME = "Datetime"
    BOOLEAN = "Boolean"


class FeatureentitiesVersionedEntityKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    INVALID = "Invalid"
    LINEAGE_ROOT = "LineageRoot"
    VERSIONED = "Versioned"
    UNVERSIONED = "Unversioned"


class FeaturesetsVersionedEntityKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    INVALID = "Invalid"
    LINEAGE_ROOT = "LineageRoot"
    VERSIONED = "Versioned"
    UNVERSIONED = "Unversioned"


class FeatureSourceDtoType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    MLTABLE = "mltable"
    CSV = "csv"
    PARQUET = "parquet"


class FeaturestoreentitiesVersionedEntityKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    INVALID = "Invalid"
    LINEAGE_ROOT = "LineageRoot"
    VERSIONED = "Versioned"
    UNVERSIONED = "Unversioned"


class GenericTriggerAnnotationsEntityStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    ACTIVE = "Active"
    DEPRECATED = "Deprecated"
    DISABLED = "Disabled"


class GenericTriggerAnnotationsManagedType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    CUSTOMER = "Customer"
    SYSTEM = "System"


class GenericTriggerAnnotationsProvisioningStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    COMPLETED = "Completed"
    PROVISIONING = "Provisioning"
    FAILED = "Failed"


class GenericTriggerAnnotationsScheduleActionType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    CREATE_JOB = "CreateJob"
    INVOKE_ENDPOINT = "InvokeEndpoint"
    IMPORT_DATA = "ImportData"
    MODEL_MONITOR = "ModelMonitor"


class GenericTriggerAnnotationsScheduleMethod(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    CRON = "Cron"
    RECURRENCE = "Recurrence"


class GenericTriggerAnnotationsTriggerType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    SCHEDULE = "Schedule"
    ONCE = "Once"


class GenerictriggersUnversionedEntityKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    INVALID = "Invalid"
    LINEAGE_ROOT = "LineageRoot"
    VERSIONED = "Versioned"
    UNVERSIONED = "Unversioned"


class IndependentPipelineAnnotationsEntityStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    ACTIVE = "Active"
    DEPRECATED = "Deprecated"
    DISABLED = "Disabled"


class IndependentPipelineAnnotationsLastRunStatusCode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    NOT_STARTED = "NotStarted"
    RUNNING = "Running"
    FAILED = "Failed"
    FINISHED = "Finished"
    CANCELED = "Canceled"
    FAILING = "Failing"
    QUEUED = "Queued"
    CANCEL_REQUESTED = "CancelRequested"


class IndependentpipelinesUnversionedEntityKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    INVALID = "Invalid"
    LINEAGE_ROOT = "LineageRoot"
    VERSIONED = "Versioned"
    UNVERSIONED = "Unversioned"


class IndexColumnDataType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    STRING = "String"
    INTEGER = "Integer"
    LONG = "Long"
    FLOAT = "Float"
    DOUBLE = "Double"
    BINARY = "Binary"
    DATETIME = "Datetime"
    BOOLEAN = "Boolean"


class IndexColumnDtoType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    STRING = "string"
    INTEGER = "integer"
    LONG = "long"
    FLOAT = "float"
    DOUBLE = "double"
    BINARY = "binary"
    DATETIME = "datetime"
    BOOLEAN = "boolean"


class IndexEntitiesRequestOrderDirection(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    ASC = "Asc"
    DESC = "Desc"


class MaterializationSettingsMaterializationStoreType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    NONE = "None"
    ONLINE = "Online"
    OFFLINE = "Offline"
    ONLINE_AND_OFFLINE = "OnlineAndOffline"


class ModelsVersionedEntityKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    INVALID = "Invalid"
    LINEAGE_ROOT = "LineageRoot"
    VERSIONED = "Versioned"
    UNVERSIONED = "Unversioned"


class ModuleAnnotationsAmlModuleEntityStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    ACTIVE = "Active"
    DEPRECATED = "Deprecated"
    DISABLED = "Disabled"


class ModuleAnnotationsEntityStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    ACTIVE = "Active"
    DEPRECATED = "Deprecated"
    DISABLED = "Disabled"


class ModuleAnnotationsModuleType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    USER = "User"
    BUILTIN = "Builtin"


class ModulesVersionedEntityKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    INVALID = "Invalid"
    LINEAGE_ROOT = "LineageRoot"
    VERSIONED = "Versioned"
    UNVERSIONED = "Unversioned"


class NotificationSettingEmailOnItem(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    JOB_COMPLETED = "JobCompleted"
    JOB_FAILED = "JobFailed"
    JOB_CANCELLED = "JobCancelled"


class OnlineendpointsUnversionedEntityKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    INVALID = "Invalid"
    LINEAGE_ROOT = "LineageRoot"
    VERSIONED = "Versioned"
    UNVERSIONED = "Unversioned"


class PipelineAnnotationsEntityStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    ACTIVE = "Active"
    DEPRECATED = "Deprecated"
    DISABLED = "Disabled"


class PipelineAnnotationsLastRunStatusCode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    NOT_STARTED = "NotStarted"
    RUNNING = "Running"
    FAILED = "Failed"
    FINISHED = "Finished"
    CANCELED = "Canceled"
    FAILING = "Failing"
    QUEUED = "Queued"
    CANCEL_REQUESTED = "CancelRequested"


class PipelineDraftAnnotationsEntityStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    ACTIVE = "Active"
    DEPRECATED = "Deprecated"
    DISABLED = "Disabled"


class PipelinedraftsUnversionedEntityKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    INVALID = "Invalid"
    LINEAGE_ROOT = "LineageRoot"
    VERSIONED = "Versioned"
    UNVERSIONED = "Unversioned"


class PipelineRunAnnotationsEntityStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    ACTIVE = "Active"
    DEPRECATED = "Deprecated"
    DISABLED = "Disabled"


class PipelinerunsUnversionedEntityKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    INVALID = "Invalid"
    LINEAGE_ROOT = "LineageRoot"
    VERSIONED = "Versioned"
    UNVERSIONED = "Unversioned"


class PipelinesVersionedEntityKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    INVALID = "Invalid"
    LINEAGE_ROOT = "LineageRoot"
    VERSIONED = "Versioned"
    UNVERSIONED = "Unversioned"


class RecurrenceFrequency(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    MONTH = "Month"
    WEEK = "Week"
    DAY = "Day"
    HOUR = "Hour"
    MINUTE = "Minute"


class RecurrenceScheduleWeekDaysItem(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"


class RecurrenceTriggerFrequency(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    MONTH = "Month"
    WEEK = "Week"
    DAY = "Day"
    HOUR = "Hour"
    MINUTE = "Minute"


class RunsUnversionedEntityKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    INVALID = "Invalid"
    LINEAGE_ROOT = "LineageRoot"
    VERSIONED = "Versioned"
    UNVERSIONED = "Unversioned"


class StructuredInterfaceParameterType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    INT = "Int"
    DOUBLE = "Double"
    BOOL = "Bool"
    STRING = "String"
    UNDEFINED = "Undefined"
