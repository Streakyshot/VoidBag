// recon.go - Amateur Tool: Basic Subdomain Bruteforcer
package main

import (
	"fmt"
	"net/http"
	"os"
	"sync"
)

func checkSubdomain(sub string, wg *sync.WaitGroup) {
	defer wg.Done()
	resp, err := http.Get("http://" + sub)
	if err == nil && resp.StatusCode < 400 {
		fmt.Printf("[+] Live: %s\n", sub)
	}
}

func main() {
	fmt.Println("[*] Recon Tool (Go): Subdomain Checker")
	if len(os.Args) < 3 {
		fmt.Println("Usage: go run recon.go <domain> <wordlist.txt>")
		return
	}

	domain := os.Args[1]
	wordlist := os.Args[2]

	file, err := os.Open(wordlist)
	if err != nil {
		fmt.Println("[-] Failed to open wordlist")
		return
	}
	defer file.Close()

	var subs []string
	var wg sync.WaitGroup
	var word string

	for {
		_, err := fmt.Fscanln(file, &word)
		if err != nil {
			break
		}
		url := word + "." + domain
		subs = append(subs, url)
	}

	for _, sub := range subs {
		wg.Add(1)
		go checkSubdomain(sub, &wg)
	}
	wg.Wait()
}
