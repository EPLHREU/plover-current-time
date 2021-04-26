# Current time

> Plover plugin for inserting the current time in an `strftime()` format

This can be used to indicate the current time when writing, useful for keeping track of when a transcription started, or when notible events occur; such as breaks.

## Installation

Install from the Plover plugins manager.

## Usage and Examples

| Dictionary Entry | Description |
| ---- | ---- |
| `"T*EUPL": "{:time:%H:%M:%S}",` | Output current time in 24-Hour format. | 
| `"SO*FL": "{:time:%Y-%m-%dT%H:%M:%S.%f%z}",` | Output current time in ISO-8601 format. | 
| `"TKA*ET": "{:time:%A, %d %B, %Y},"` | Output current date in a nice human readable format. |
| `"PWRAEBG": "\n(break started: {:time:%H:%M:%S}{^})\n",` | Note that a break has started and at what time. |
| `"PWRA*EBG": "\n(break ended: {:time:%H:%M:%S}{^})\n",` | Note that the break has ended and at what time. |

Optionally, you can define a locale to get more specific output. The locale should be available on your system, and it can be specified after the separator `>>`, like this:

| Dictionary Entry | Description |
| ---- | ---- |
| `"TKA*/TUPL": "{:time:%A, %d %B, %Y>>de_DE}",` | Output current date in german. | 
| `"TP*E/KHA": "{:time:%A, %d %B, %Y>>es_ES}",` | Output current date in spanish. | 
