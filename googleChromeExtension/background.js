// TimeLogger in Google Chrome! this is an extension for it
// created: 19.07.2021

chrome.runtime.onInstalled.addListener(function() {
  chrome.storage.sync.set({color: '#10d8e3'}, function() {
    console.log("The color is light blue");
  });

  chrome.declarativeContent.onPageChanged.removeRules(undefined,function(){
    chrome.declarativeContent.onPageChanged.addRules([{
      conditions: [new chrome.declarativeContent.PageStateMatcher({
        pageUrl: {hostEquals: 'developer.chrome.com'},
      })
    ],
      actions: [new chrome.declarativeContent.ShowPageAction()]
    }]);
  });
});
