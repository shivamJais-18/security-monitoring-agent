#!/usr/bin/env python3
"""
Dataset Manager - Generate, compare, and manage security log datasets
Useful for testing different threat scenarios and pipeline performance
"""

import json
import os
import sys
from pathlib import Path
from datetime import datetime

class DatasetManager:
    def __init__(self, base_dir="data/raw_logs"):
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(parents=True, exist_ok=True)
    
    def count_logs(self, filename):
        """Count total log entries in a file"""
        filepath = self.base_dir / filename
        if not filepath.exists():
            return 0
        return sum(1 for _ in open(filepath))
    
    def file_size_mb(self, filename):
        """Get file size in MB"""
        filepath = self.base_dir / filename
        if not filepath.exists():
            return 0
        return os.path.getsize(filepath) / (1024 * 1024)
    
    def analyze_dataset(self, filename):
        """Analyze event distribution in a dataset"""
        filepath = self.base_dir / filename
        if not filepath.exists():
            print(f"❌ File not found: {filename}")
            return
        
        event_counts = {}
        severity_counts = {}
        
        with open(filepath, "r") as f:
            for line in f:
                try:
                    log = json.loads(line.strip())
                    event_type = log.get("event_type", "UNKNOWN")
                    severity = log.get("severity", 0)
                    
                    event_counts[event_type] = event_counts.get(event_type, 0) + 1
                    severity_counts[severity] = severity_counts.get(severity, 0) + 1
                except:
                    continue
        
        print(f"\n📊 Dataset Analysis: {filename}")
        print(f"   Total entries: {self.count_logs(filename):,}")
        print(f"   File size: {self.file_size_mb(filename):.2f} MB")
        
        print(f"\n   Event Type Distribution:")
        for event_type in sorted(event_counts.items(), key=lambda x: x[1], reverse=True):
            pct = (event_type[1] / sum(event_counts.values())) * 100
            print(f"     {event_type[0]:30} : {event_type[1]:6,} ({pct:5.1f}%)")
        
        print(f"\n   Severity Distribution:")
        for severity in sorted(severity_counts.keys()):
            count = severity_counts[severity]
            pct = (count / sum(severity_counts.values())) * 100
            print(f"     Level {severity}: {count:6,} ({pct:5.1f}%)")
    
    def list_datasets(self):
        """List all available datasets"""
        datasets = [f.name for f in self.base_dir.glob("*.json")]
        
        if not datasets:
            print(f"ℹ️  No datasets found in {self.base_dir}")
            return
        
        print(f"\n📁 Available Datasets in {self.base_dir}:\n")
        print(f"{'Dataset Name':<40} {'Entries':>15} {'Size':>12}")
        print("=" * 67)
        
        total_entries = 0
        total_size = 0
        
        for dataset in sorted(datasets):
            count = self.count_logs(dataset)
            size = self.file_size_mb(dataset)
            print(f"{dataset:<40} {count:>15,} {size:>11.2f} MB")
            total_entries += count
            total_size += size
        
        print("=" * 67)
        print(f"{'TOTAL':<40} {total_entries:>15,} {total_size:>11.2f} MB\n")
    
    def compare_datasets(self, *filenames):
        """Compare event distributions across multiple datasets"""
        if len(filenames) < 2:
            print("❌ Please provide at least 2 datasets to compare")
            return
        
        all_events = set()
        dataset_data = {}
        
        for filename in filenames:
            if not (self.base_dir / filename).exists():
                print(f"⚠️  File not found: {filename}, skipping...")
                continue
            
            event_counts = {}
            with open(self.base_dir / filename, "r") as f:
                for line in f:
                    try:
                        log = json.loads(line.strip())
                        event_type = log.get("event_type", "UNKNOWN")
                        event_counts[event_type] = event_counts.get(event_type, 0) + 1
                        all_events.add(event_type)
                    except:
                        continue
            
            dataset_data[filename] = event_counts
        
        print(f"\n🔍 Dataset Comparison\n")
        print(f"{'Event Type':<30}", end="")
        for filename in filenames:
            print(f"{filename:<20}", end="")
        print("\n" + "=" * (30 + len(filenames) * 20))
        
        for event in sorted(all_events):
            print(f"{event:<30}", end="")
            for filename in filenames:
                count = dataset_data[filename].get(event, 0)
                print(f"{count:<20}", end="")
            print()
    
    def regenerate_all(self):
        """Regenerate all datasets"""
        print("\n🔄 Regenerating datasets...\n")
        
        # Import the generator functions
        try:
            sys.path.insert(0, str(self.base_dir))
            from generate_logs import *
            from generate_extended_datasets import *
            
            print("✓ Running generate_logs.py...")
            # This will create siem_logs.json
            
            print("✓ Running generate_extended_datasets.py...")
            # This will create extended datasets
            
            print("\n✅ All datasets regenerated!")
            self.list_datasets()
        
        except Exception as e:
            print(f"❌ Error during regeneration: {e}")
    
    def estimate_threat_detection(self, filename):
        """Estimate potential threat detection based on event types"""
        filepath = self.base_dir / filename
        if not filepath.exists():
            print(f"❌ File not found: {filename}")
            return
        
        threat_events = {"SQL_INJECTION", "DDoS_DETECTED", "MALWARE_ALERT", 
                        "DATA_EXFILTRATION", "PRIVILEGE_ESCALATION"}
        normal_events = {"AUTH_SUCCESS", "FILE_ACCESS"}
        suspicious_events = {"AUTH_FAIL", "PORT_SCAN", "FIREWALL_BLOCK"}
        
        threat_count = 0
        normal_count = 0
        suspicious_count = 0
        high_severity = 0
        
        with open(filepath, "r") as f:
            for line in f:
                try:
                    log = json.loads(line.strip())
                    event_type = log.get("event_type", "UNKNOWN")
                    severity = log.get("severity", 0)
                    
                    if event_type in threat_events:
                        threat_count += 1
                    elif event_type in normal_events:
                        normal_count += 1
                    elif event_type in suspicious_events:
                        suspicious_count += 1
                    
                    if severity >= 7:
                        high_severity += 1
                except:
                    continue
        
        total = threat_count + normal_count + suspicious_count
        if total == 0:
            return
        
        print(f"\n📈 Threat Detection Estimate for {filename}:")
        print(f"   Total events: {total:,}")
        print(f"   High-confidence threats: {threat_count:,} ({threat_count/total*100:5.1f}%)")
        print(f"   Normal activity: {normal_count:,} ({normal_count/total*100:5.1f}%)")
        print(f"   Suspicious events: {suspicious_count:,} ({suspicious_count/total*100:5.1f}%)")
        print(f"   High severity (≥7): {high_severity:,} ({high_severity/total*100:5.1f}%)")
        print(f"\n   Expected detected threats: ~{threat_count + int(suspicious_count*0.3):,}")


def main():
    manager = DatasetManager()
    
    print("\n🔐 Security Dataset Manager\n")
    
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "list":
            manager.list_datasets()
        
        elif command == "analyze" and len(sys.argv) > 2:
            manager.analyze_dataset(sys.argv[2])
        
        elif command == "compare" and len(sys.argv) > 3:
            manager.compare_datasets(*sys.argv[2:])
        
        elif command == "estimate" and len(sys.argv) > 2:
            manager.estimate_threat_detection(sys.argv[2])
        
        elif command == "regenerate":
            manager.regenerate_all()
        
        else:
            print("Usage:")
            print("  python dataset_manager.py list                           # List all datasets")
            print("  python dataset_manager.py analyze <filename>             # Analyze a dataset")
            print("  python dataset_manager.py compare <file1> <file2> ...   # Compare datasets")
            print("  python dataset_manager.py estimate <filename>            # Estimate threat detection")
            print("  python dataset_manager.py regenerate                     # Regenerate all datasets\n")
    
    else:
        # Default: show all datasets
        manager.list_datasets()


if __name__ == "__main__":
    main()
