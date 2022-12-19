# Script to load json, return the newest version of stellaris
import sys, json

# ddsPayload.json uses a format like
"""
{
    "build_id": "name",
    "10063376": "orion-3.6.1"
}
"""
# Requiring a calculation to find the largest value (by build_i via steamdb.io)
# In this case, we just use python's native "max", as all buildid's are treated as ints in this manner
payloadFile = open('ddsPayload.json')
payloadFileData = json.load(payloadFile)
payloadNewest = max(payloadFileData)

payloadNewestDirectory = payloadFileData[payloadNewest]

print(payloadNewestDirectory)
sys.exit(0)
