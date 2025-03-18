# Airtable Plugin

A plugin tool for operating Airtable, supporting record creation and other operations.

## What's Airtable?

[Airtable](https://airtable.com/) is a cloud-based project management tool that blends a traditional spreadsheet with the robust features of a database. It allows businesses to organize their workflow, data, and records in a flexible and visually appealing way without the need for any coding.

## Features

- Support creating records in Airtable
- Support get all records from existing table
- Simple and easy-to-use API interface

## Prerequisites

- Airtable account
- Airtable API Token
- Created Airtable Base and Table

## Configuration Guide

### Getting Required Information

1. **Airtable Token**
   - Visit [Airtable Token Creation Page](https://airtable.com/create/tokens)
   - Create and save your API Token

2. **Base ID and Table ID**
   - Can be obtained from Airtable URL
   - For detailed instructions, refer to: [Finding Airtable IDs](https://support.airtable.com/v1/docs/finding-airtable-ids#finding-base-table-and-view-ids-from-urls)

### Setup Steps

1. Configure Airtable Token
   - Enter your Airtable Token in the plugin configuration
   - Token will be securely stored and used for API authentication

2. Using the Plugin
   - Provide Base ID
   - Provide Table ID
   - Provide record data to create (in JSON format)

## Usage Example

### Create a record

#### Start by creating your own table in Airtable, something like this

![table](_assets/table.png)

Add fields according to your needs

Example of creating a record:

```json
{
  "Spend": 52,
  "Store": "Gas station",
  "Item": "Gas",
  "DateTime": "2025-03-15",
  "Memo": "Filled up 52 yuan worth of gas at the gas station"
}
```

#### Get all records

All the records can be returned by providing baseId and tableId in the tool.

The output results are printed in text. The following is an example of the output:

```json
[
  {
    "id": "rec123",
    "fields": {
      "Spend": 52,
      "Store": "Gas station",
      "Item": "Gas",
      "DateTime": "2025-03-15",
      "Memo": "Filled up 52 yuan worth of gas at the gas station"
    },
    {
      "id": "rec456",
      "fields": {
        "Spend": 100,
        "Store": "Supermarket",
        "Item": "Milk",
        "DateTime": "2025-03-16",
        "Memo": "Bought 100 yuan worth of milk at the supermarket"
      }
    }
]
```
