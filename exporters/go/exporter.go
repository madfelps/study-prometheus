package main

import (
	"log"
	"net/http"

	"github.com/pbnjay/memory"
	"gitub.com/prometheus/client_golang/prometheus"
)

func freeMemory() float64 {
	free_memory := memory.Freememory()
	return float64(free_memory)
}

func totalMemory() float64 {
	total_memory := memory.TotalMemory()
	return float64(total_memory)
}

var (
	freeMemoryBytesGauge = prometheus.NewGauge(prometheus.GaugeOpts{
		Name: "free_memory_bytes",
		Help: "Total free memory available in bytes",
	})

	freeMemoryMegasGauge = prometheus.NewGauge(prometheus.GaugeOpts{
		Name: "free_memory_megas",
		Help: "Total free memory available in megas",
	})

	totalMemoryBytesGauge = prometheus.NewGauge(prometheus.GaugeOpts{
		Name: "total_memory_bytes",
		Help: "Total memory in bytes",
	})

	totalMemoryGigasGauge = prometheus.NewGauge(prometheus.GaugeOpts{
		Name: "total_memory_gigas",
		Help: "Total memory in gigas",
	})
)

func init() {
	prometheus.MustRegister(freeMemoryBytesGauge)
	prometheus.MustRegister(freeMemoryMegasGauge)
	prometheus.MustRegister(totalMemoryBytesGauge)
	prometheus.MustRegister(totalMemoryGigasGauge)
}

func main() {
	freeMemoryBytesGauge.Set(freeMemory())
	freeMemoryMegasGauge.Set(freeMemory() / 1024 / 1024)
	totalMemoryBytesGauge.Set(totalMemory())
	totalMemoryGigasGauge.Set(totalMemory() / 1024 / 1024 / 1024)
	http.Handle("/metrics", promhttp.Handler())
	log.Fatal(http.ListenAndServe(":7788", nil))

}
