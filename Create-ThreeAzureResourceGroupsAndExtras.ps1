# Here is a PowerShell script that creates three Azure resource groups for env1, env2, env3. It creates a VNet in each resource group and a subnet in each environment for each of the following services: service1, service2, service3. It ensures these subnets can only talk with each other in their environments and no other VNets. They must accept traffic from only the 172.32.0.0/27 network.

#```powershell
# Create resource groups
$resourceGroupNames = @("env1", "env2", "env3")

foreach ($resourceGroupName in $resourceGroupNames) {
    New-AzResourceGroup -Name $resourceGroupName -Location "East US"
}

# Create VNets and subnets
foreach ($resourceGroupName in $resourceGroupNames) {
    # Create VNet
    $vnetName = "$($resourceGroupName)-vnet"
    $vnet = New-AzVirtualNetwork `
        -Name $vnetName `
        -ResourceGroupName $resourceGroupName `
        -Location "East US" `
        -AddressPrefix "172.32.0.0/16"

    # Create subnets
    $subnetNames = @("service1", "service2", "service3")
    foreach ($subnetName in $subnetNames) {
        $subnet = New-AzVirtualNetworkSubnetConfig `
            -Name $subnetName `
            -AddressPrefix "172.32.0.0/27"

        # Add subnet to VNet
        Add-AzVirtualNetworkSubnetConfig `
            -Name $subnetName `
            -VirtualNetwork $vnet `
            -AddressPrefix "172.32.0.0/16" `
            -Subnet $subnet

        # Set up network security group (NSG) rules to allow traffic between subnets
        $nsg = New-AzNetworkSecurityGroup `
            -ResourceGroupName $resourceGroupName `
            -Location "East US" `
            -Name "$($subnetName)-nsg"

        # Allow traffic from subnet to subnet within the same VNet
        New-AzNetworkSecurityRuleConfig `
            -Name "Allow-$($subnetName)-to-$($subnetName)" `
            -Description "Allow traffic from $($subnetName) to $($subnetName)" `
            -Access Allow `
            -Protocol '*' `
            -Direction Inbound `
            -Priority 100 `
            -SourceAddressPrefix "172.32.0.0/27" `
            -SourcePortRange '*' `
            -DestinationAddressPrefix "172.32.0.0/27" `
            -DestinationPortRange '*'
    }
}

# Clean up resources created
foreach ($resourceGroupName in $resourceGroupNames) {
    Remove-AzResourceGroup -Name $resourceGroupName -Force
}
# ```

# You can modify the `$resourceGroupNames` array to your preferred names for the resource groups.

#Source: Conversation with Bing, 5/3/2023
#(1) az network vnet subnet | Microsoft Learn. https://learn.microsoft.com/en-us/cli/azure/network/vnet/subnet?view=azure-cli-latest.
#(2) Azure Powershell - Applying multiple service endpoints to a subnet .... https://stackoverflow.com/questions/54579309/azure-powershell-applying-multiple-service-endpoints-to-a-subnet.
#(3) Quickstart: Use Azure PowerShell to create a virtual network. https://learn.microsoft.com/en-us/azure/virtual-network/quick-create-powershell.
#(4) powershell - Can virtual network be in different Resource Group while .... https://stackoverflow.com/questions/52051134/can-virtual-network-be-in-different-resource-group-while-creating-a-vm-in-azure.
#(5) Create a Azure Virtual Network with Subnet using PowerShell. http://vcloud-lab.com/entries/blog/create-a-azure-virtual-network-with-subnet-using-powershell.
