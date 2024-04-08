*** Settings ***
Documentation     A simple test to open example.com and click on the first link.
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        Chrome
${URL}            https://example.com
${LINK_TEXT}      More information...

*** Test Cases ***
Open Example And Click Link
    Open Browser    ${URL}    ${BROWSER}
    ${link}=    Get Webelement    xpath://a[contains(text(), "${LINK_TEXT}")]
    Click Element    ${link}
    [Teardown]    Close Browser
