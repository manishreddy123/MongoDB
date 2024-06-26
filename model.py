# model.py

daily_usage_schema = {
"_id",
"identity/LineItemId",
"identity/TimeInterval",
"bill/InvoiceId",
"bill/InvoicingEntity",
"bill/BillingEntity",
"bill/BillType",
"bill/PayerAccountId",
"bill/BillingPeriodStartDate",
"bill/BillingPeriodEndDate",
"lineItem/UsageAccountId",
"lineItem/LineItemType",
"lineItem/UsageStartDate",
"lineItem/UsageEndDate",
"lineItem/ProductCode",
"lineItem/UsageType",
"lineItem/Operation",
"lineItem/AvailabilityZone",
"lineItem/ResourceId",
"lineItem/UsageAmount",
"lineItem/NormalizationFactor",
"lineItem/NormalizedUsageAmount",
"lineItem/CurrencyCode",
"lineItem/UnblendedRate",
"lineItem/UnblendedCost",
"lineItem/BlendedRate",
"lineItem/BlendedCost",
"lineItem/LineItemDescription",
"lineItem/TaxType",
"lineItem/NetUnblendedRate",
"lineItem/NetUnblendedCost",
"lineItem/LegalEntity",
"product/ProductName",
"product/PurchaseOption",
"product/SizeFlex",
"product/accessType",
"product/accountAssistance",
"product/alarmType",
"product/apiType",
"product/architecturalReview",
"product/architectureSupport",
"product/attachmentType",
"product/availability",
"product/availabilityZone",
"product/backupservice",
"product/bestPractices",
"product/brokerEngine",
"product/bundle",
"product/bundleDescription",
"product/bundleGroup",
"product/cacheEngine",
"product/capacity",
"product/capacitystatus",
"product/caseSeverityresponseTimes",
"product/category",
"product/ciType",
"product/classicnetworkingsupport",
"product/clientLocation",
"product/clockSpeed",
"product/cloudSearchVersion",
"product/component",
"product/computeFamily",
"product/computeType",
"product/connectionType",
"product/contentType",
"product/cputype",
"product/currentGeneration",
"product/customerServiceAndCommunities",
"product/data",
"product/databaseEngine",
"product/dedicatedEbsThroughput",
"product/deploymentOption",
"product/description",
"product/destinationCountryIsoCode",
"product/directConnectLocation",
"product/directorySize",
"product/directoryType",
"product/directoryTypeDescription",
"product/dominantnondominant",
"product/durability",
"product/ecu",
"product/edition",
"product/endpoint",
"product/endpointType",
"product/engineCode",
"product/engineMajorVersion",
"product/enhancedNetworkingSupport",
"product/enhancedNetworkingSupported",
"product/entityType",
"product/equivalentondemandsku",
"product/eventType",
"product/extendedSupportPricingYear",
"product/feeCode",
"product/feeDescription",
"product/findingGroup",
"product/findingSource",
"product/findingStorage",
"product/freeQueryTypes",
"product/fromLocation",
"product/fromLocationType",
"product/fromRegionCode",
"product/georegioncode",
"product/gpu",
"product/gpuMemory",
"product/granularity",
"product/group",
"product/groupDescription",
"product/includedServices",
"product/insightstype",
"product/instance",
"product/instanceFamily",
"product/instanceName",
"product/instanceType",
"product/instanceTypeFamily",
"product/intelAvx2Available",
"product/intelAvxAvailable",
"product/intelTurboAvailable",
"product/iso",
"product/launchSupport",
"product/license",
"product/licenseModel",
"product/location",
"product/locationType",
"product/logsDestination",
"product/marketoption",
"product/maxIopsBurstPerformance",
"product/maxIopsvolume",
"product/maxThroughputvolume",
"product/maxVolumeSize",
"product/maximumExtendedStorage",
"product/memory",
"product/memoryGib",
"product/memorytype",
"product/messageCountfee",
"product/messageDeliveryFrequency",
"product/messageDeliveryOrder",
"product/messageType",
"product/meteringType",
"product/minVolumeSize",
"product/networkPerformance",
"product/normalizationSizeFactor",
"product/operatingSystem",
"product/operation",
"product/operationsSupport",
"product/origin",
"product/originationId",
"product/originationIdType",
"product/overhead",
"product/packSize",
"product/physicalCpu",
"product/physicalGpu",
"product/physicalProcessor",
"product/platoclassificationtype",
"product/platoinstancename",
"product/platoinstancetype",
"product/platopagedatatype",
"product/platopricingtype",
"product/portSpeed",
"product/preInstalledSw",
"product/pricingUnit",
"product/pricingplan",
"product/proactiveGuidance",
"product/processorArchitecture",
"product/processorFeatures",
"product/productFamily",
"product/productType",
"product/programmaticCaseManagement",
"product/provider",
"product/provisioned",
"product/purchaseterm",
"product/qPresent",
"product/queueType",
"product/recipient",
"product/region",
"product/regionCode",
"product/requestDescription",
"product/requestType",
"product/resourceEndpoint",
"product/resourceType",
"product/rootvolume",
"product/routeType",
"product/routingTarget",
"product/routingType",
"product/runningMode",
"product/servicecode",
"product/servicename",
"product/sku",
"product/softwareIncluded",
"product/standardGroup",
"product/standardStorage",
"product/standardStorageRetentionIncluded",
"product/storage",
"product/storageClass",
"product/storageFamily",
"product/storageMedia",
"product/storageType",
"product/subscriptionType",
"product/subservice",
"product/technicalSupport",
"product/tenancy",
"product/thirdpartySoftwareSupport",
"product/tickettype",
"product/tiertype",
"product/toLocation",
"product/toLocationType",
"product/toRegionCode",
"product/trafficDirection",
"product/training",
"product/transferType",
"product/trialProduct",
"product/type",
"product/typeDescription",
"product/upfrontCommitment",
"product/usageFamily",
"product/usageGroup",
"product/usagetype",
"product/uservolume",
"product/vaulttype",
"product/vcpu",
"product/version",
"product/virtualInterfaceType",
"product/volumeApiName",
"product/volumeType",
"product/vpcnetworkingsupport",
"product/whoCanOpenCases",
"pricing/LeaseContractLength",
"pricing/OfferingClass",
"pricing/PurchaseOption",
"pricing/RateCode",
"pricing/RateId",
"pricing/currency",
"pricing/publicOnDemandCost",
"pricing/publicOnDemandRate",
"pricing/term",
"pricing/unit",
"reservation/AmortizedUpfrontCostForUsage",
"reservation/AmortizedUpfrontFeeForBillingPeriod",
"reservation/EffectiveCost",
"reservation/EndTime",
"reservation/ModificationStatus",
"reservation/NetAmortizedUpfrontCostForUsage",
"reservation/NetAmortizedUpfrontFeeForBillingPeriod",
"reservation/NetEffectiveCost",
"reservation/NetRecurringFeeForUsage",
"reservation/NetUnusedAmortizedUpfrontFeeForBillingPeriod",
"reservation/NetUnusedRecurringFee",
"reservation/NetUpfrontValue",
"reservation/NormalizedUnitsPerReservation",
"reservation/NumberOfReservations",
"reservation/RecurringFeeForUsage",
"reservation/ReservationARN",
"reservation/StartTime",
"reservation/SubscriptionId",
"reservation/TotalReservedNormalizedUnits",
"reservation/TotalReservedUnits",
"reservation/UnitsPerReservation",
"reservation/UnusedAmortizedUpfrontFeeForBillingPeriod",
"reservation/UnusedNormalizedUnitQuantity",
"reservation/UnusedQuantity",
"reservation/UnusedRecurringFee",
"reservation/UpfrontValue",
"discount/EdpDiscount",
"discount/TotalDiscount",
"savingsPlan/TotalCommitmentToDate",
"savingsPlan/SavingsPlanARN",
"savingsPlan/SavingsPlanRate",
"savingsPlan/UsedCommitment",
"savingsPlan/SavingsPlanEffectiveCost",
"savingsPlan/AmortizedUpfrontCommitmentForBillingPeriod",
"savingsPlan/RecurringCommitmentForBillingPeriod",
"savingsPlan/StartTime",
"savingsPlan/EndTime",
"savingsPlan/OfferingType",
"savingsPlan/PaymentOption",
"savingsPlan/PurchaseTerm",
"savingsPlan/Region",
"savingsPlan/NetSavingsPlanEffectiveCost",
"savingsPlan/NetAmortizedUpfrontCommitmentForBillingPeriod",
"savingsPlan/NetRecurringCommitmentForBillingPeriod",
"resourceTags/aws:autoscaling:groupName",
"resourceTags/aws:cloudformation:stack-id",
"resourceTags/aws:createdBy",
"resourceTags/aws:eks:cluster-name",
"resourceTags/user:ClusterName",
"resourceTags/user:Name",
"resourceTags/user:Vendor",
"resourceTags/user:karpenter.sh/managed-by",
"resourceTags/user:karpenter.sh/nodepool",
"resourceTags/user:karpenter.sh/provisioner-name",
"resourceTags/user:s3_bucket",
"resourceTags/user:user:Application",
"resourceTags/user:user:Product",
"resourceTags/user:user:Stack",
"resourceTags/user:user:Team",
"lineItem/UsageDate"
}

usage_summary_schema = {
"_id",
"identity/LineItemId",
"identity/TimeInterval",
"bill/InvoiceId",
"bill/InvoicingEntity",
"bill/BillingEntity",
"bill/BillType",
"bill/PayerAccountId",
"bill/BillingPeriodStartDate",
"bill/BillingPeriodEndDate",
"lineItem/UsageAccountId",
"lineItem/LineItemType",
"lineItem/UsageStartDate",
"lineItem/UsageEndDate",
"lineItem/ProductCode",
"lineItem/UsageType",
"lineItem/Operation",
"lineItem/AvailabilityZone",
"lineItem/ResourceId",
"lineItem/UsageAmount",
"lineItem/NormalizationFactor",
"lineItem/NormalizedUsageAmount",
"lineItem/CurrencyCode",
"lineItem/UnblendedRate",
"lineItem/UnblendedCost",
"lineItem/BlendedRate",
"lineItem/BlendedCost",
"lineItem/LineItemDescription",
"lineItem/TaxType",
"lineItem/NetUnblendedRate",
"lineItem/NetUnblendedCost",
"lineItem/LegalEntity",
"product/ProductName",
"product/PurchaseOption",
"product/SizeFlex",
"product/accessType",
"product/accountAssistance",
"product/alarmType",
"product/apiType",
"product/architecturalReview",
"product/architectureSupport",
"product/attachmentType",
"product/availability",
"product/availabilityZone",
"product/backupservice",
"product/bestPractices",
"product/brokerEngine",
"product/bundle",
"product/bundleDescription",
"product/bundleGroup",
"product/cacheEngine",
"product/capacity",
"product/capacitystatus",
"product/caseSeverityresponseTimes",
"product/category",
"product/ciType",
"product/classicnetworkingsupport",
"product/clientLocation",
"product/clockSpeed",
"product/cloudSearchVersion",
"product/component",
"product/computeFamily",
"product/computeType",
"product/connectionType",
"product/contentType",
"product/cputype",
"product/currentGeneration",
"product/customerServiceAndCommunities",
"product/data",
"product/databaseEngine",
"product/dedicatedEbsThroughput",
"product/deploymentOption",
"product/description",
"product/destinationCountryIsoCode",
"product/directConnectLocation",
"product/directorySize",
"product/directoryType",
"product/directoryTypeDescription",
"product/dominantnondominant",
"product/durability",
"product/ecu",
"product/edition",
"product/endpoint",
"product/endpointType",
"product/engineCode",
"product/engineMajorVersion",
"product/enhancedNetworkingSupport",
"product/enhancedNetworkingSupported",
"product/entityType",
"product/equivalentondemandsku",
"product/eventType",
"product/extendedSupportPricingYear",
"product/feeCode",
"product/feeDescription",
"product/findingGroup",
"product/findingSource",
"product/findingStorage",
"product/freeQueryTypes",
"product/fromLocation",
"product/fromLocationType",
"product/fromRegionCode",
"product/georegioncode",
"product/gpu",
"product/gpuMemory",
"product/granularity",
"product/group",
"product/groupDescription",
"product/includedServices",
"product/insightstype",
"product/instance",
"product/instanceFamily",
"product/instanceName",
"product/instanceType",
"product/instanceTypeFamily",
"product/intelAvx2Available",
"product/intelAvxAvailable",
"product/intelTurboAvailable",
"product/iso",
"product/launchSupport",
"product/license",
"product/licenseModel",
"product/location",
"product/locationType",
"product/logsDestination",
"product/marketoption",
"product/maxIopsBurstPerformance",
"product/maxIopsvolume",
"product/maxThroughputvolume",
"product/maxVolumeSize",
"product/maximumExtendedStorage",
"product/memory",
"product/memoryGib",
"product/memorytype",
"product/messageCountfee",
"product/messageDeliveryFrequency",
"product/messageDeliveryOrder",
"product/messageType",
"product/meteringType",
"product/minVolumeSize",
"product/networkPerformance",
"product/normalizationSizeFactor",
"product/operatingSystem",
"product/operation",
"product/operationsSupport",
"product/origin",
"product/originationId",
"product/originationIdType",
"product/overhead",
"product/packSize",
"product/physicalCpu",
"product/physicalGpu",
"product/physicalProcessor",
"product/platoclassificationtype",
"product/platoinstancename",
"product/platoinstancetype",
"product/platopagedatatype",
"product/platopricingtype",
"product/portSpeed",
"product/preInstalledSw",
"product/pricingUnit",
"product/pricingplan",
"product/proactiveGuidance",
"product/processorArchitecture",
"product/processorFeatures",
"product/productFamily",
"product/productType",
"product/programmaticCaseManagement",
"product/provider",
"product/provisioned",
"product/purchaseterm",
"product/qPresent",
"product/queueType",
"product/recipient",
"product/region",
"product/regionCode",
"product/requestDescription",
"product/requestType",
"product/resourceEndpoint",
"product/resourceType",
"product/rootvolume",
"product/routeType",
"product/routingTarget",
"product/routingType",
"product/runningMode",
"product/servicecode",
"product/servicename",
"product/sku",
"product/softwareIncluded",
"product/standardGroup",
"product/standardStorage",
"product/standardStorageRetentionIncluded",
"product/storage",
"product/storageClass",
"product/storageFamily",
"product/storageMedia",
"product/storageType",
"product/subscriptionType",
"product/subservice",
"product/technicalSupport",
"product/tenancy",
"product/thirdpartySoftwareSupport",
"product/tickettype",
"product/tiertype",
"product/toLocation",
"product/toLocationType",
"product/toRegionCode",
"product/trafficDirection",
"product/training",
"product/transferType",
"product/trialProduct",
"product/type",
"product/typeDescription",
"product/upfrontCommitment",
"product/usageFamily",
"product/usageGroup",
"product/usagetype",
"product/uservolume",
"product/vaulttype",
"product/vcpu",
"product/version",
"product/virtualInterfaceType",
"product/volumeApiName",
"product/volumeType",
"product/vpcnetworkingsupport",
"product/whoCanOpenCases",
"pricing/LeaseContractLength",
"pricing/OfferingClass",
"pricing/PurchaseOption",
"pricing/RateCode",
"pricing/RateId",
"pricing/currency",
"pricing/publicOnDemandCost",
"pricing/publicOnDemandRate",
"pricing/term",
"pricing/unit",
"reservation/AmortizedUpfrontCostForUsage",
"reservation/AmortizedUpfrontFeeForBillingPeriod",
"reservation/EffectiveCost",
"reservation/EndTime",
"reservation/ModificationStatus",
"reservation/NetAmortizedUpfrontCostForUsage",
"reservation/NetAmortizedUpfrontFeeForBillingPeriod",
"reservation/NetEffectiveCost",
"reservation/NetRecurringFeeForUsage",
"reservation/NetUnusedAmortizedUpfrontFeeForBillingPeriod",
"reservation/NetUnusedRecurringFee",
"reservation/NetUpfrontValue",
"reservation/NormalizedUnitsPerReservation",
"reservation/NumberOfReservations",
"reservation/RecurringFeeForUsage",
"reservation/ReservationARN",
"reservation/StartTime",
"reservation/SubscriptionId",
"reservation/TotalReservedNormalizedUnits",
"reservation/TotalReservedUnits",
"reservation/UnitsPerReservation",
"reservation/UnusedAmortizedUpfrontFeeForBillingPeriod",
"reservation/UnusedNormalizedUnitQuantity",
"reservation/UnusedQuantity",
"reservation/UnusedRecurringFee",
"reservation/UpfrontValue",
"discount/EdpDiscount",
"discount/TotalDiscount",
"savingsPlan/TotalCommitmentToDate",
"savingsPlan/SavingsPlanARN",
"savingsPlan/SavingsPlanRate",
"savingsPlan/UsedCommitment",
"savingsPlan/SavingsPlanEffectiveCost",
"savingsPlan/AmortizedUpfrontCommitmentForBillingPeriod",
"savingsPlan/RecurringCommitmentForBillingPeriod",
"savingsPlan/StartTime",
"savingsPlan/EndTime",
"savingsPlan/OfferingType",
"savingsPlan/PaymentOption",
"savingsPlan/PurchaseTerm",
"savingsPlan/Region",
"savingsPlan/NetSavingsPlanEffectiveCost",
"savingsPlan/NetAmortizedUpfrontCommitmentForBillingPeriod",
"savingsPlan/NetRecurringCommitmentForBillingPeriod",
"resourceTags/aws:autoscaling:groupName",
"resourceTags/aws:cloudformation:stack-id",
"resourceTags/aws:createdBy",
"resourceTags/aws:eks:cluster-name",
"resourceTags/user:ClusterName",
"resourceTags/user:Name",
"resourceTags/user:Vendor",
"resourceTags/user:karpenter.sh/managed-by",
"resourceTags/user:karpenter.sh/nodepool",
"resourceTags/user:karpenter.sh/provisioner-name",
"resourceTags/user:s3_bucket",
"resourceTags/user:user:Application",
"resourceTags/user:user:Product",
"resourceTags/user:user:Stack",
"resourceTags/user:user:Team"
}

class SchemaValidator:
   
    def validation(self, expected_schema, actual_document):
        actual_keys = set(actual_document.keys())
        if not actual_keys.issubset(expected_schema):
            raise Exception(f"\nSchema mismatch detected. \n\nExpected keys: {expected_schema},\n\nActual keys: {actual_keys}")

    def validate_schema(self, function, actual_document):
        if function == "daily_usage":
            schema = daily_usage_schema
        elif function == "usage_summary":
            schema = usage_summary_schema
        else:
            print(f"Unknown function: {function}")
            return

        try:
            self.validation(schema, actual_document)
        except Exception as e:
            print(e)


#  code to be used in main function
'''actual_document = {
    "lineItem/UsageDate": "2023-01-01",
    "lineItem/ResourceId": "resource-123",
    "lineItem/UsageAmount": 100,
    "lineItem/UnblendedRate": 0.2,
    "lineItem/UnblendedCost": 20,
    "lineItem/BlendedRate": 0.15,
    "lineItem/BlendedCost": 15,
    "lineItem/UsageEndDate": "2023-01-02",
    "lineItem/BlendedPrice": 15
}

validator = SchemaValidator()
func = "daily_usage"
validator.validate_schema(func, actual_document)'''

