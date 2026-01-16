"""Enterprise Alpha Pilot Program.

Manages alpha pilot customers with white-glove onboarding.
"""

from typing import Dict, Any, List
from datetime import datetime, timedelta
from dataclasses import dataclass, field
from enum import Enum


class PilotPhase(Enum):
    """Pilot program phases."""
    ONBOARDING = "onboarding"
    TRAINING = "training"
    INTEGRATION = "integration"
    TESTING = "testing"
    PRODUCTION = "production"
    SUCCESS = "success"


class IndustryVertical(Enum):
    """Industry verticals."""
    FINTECH = "fintech"
    HEALTHCARE = "healthcare"
    ECOMMERCE = "ecommerce"
    LOGISTICS = "logistics"
    MANUFACTURING = "manufacturing"
    MEDIA = "media"


@dataclass
class PilotCustomer:
    """Represents an enterprise pilot customer."""
    customer_id: str
    company_name: str
    industry: IndustryVertical
    contact_email: str
    start_date: datetime
    phase: PilotPhase = PilotPhase.ONBOARDING
    arr_potential: float = 0.0
    use_cases: List[str] = field(default_factory=list)
    success_metrics: Dict[str, Any] = field(default_factory=dict)
    health_score: float = 0.0  # 0-100
    notes: List[str] = field(default_factory=list)
    
    def get_days_in_pilot(self) -> int:
        """Calculate days since pilot start."""
        return (datetime.utcnow() - self.start_date).days
    
    def advance_phase(self) -> None:
        """Move to next pilot phase."""
        phases = list(PilotPhase)
        current_index = phases.index(self.phase)
        if current_index < len(phases) - 1:
            self.phase = phases[current_index + 1]
    
    def add_note(self, note: str) -> None:
        """Add note to customer record."""
        timestamp = datetime.utcnow().isoformat()
        self.notes.append(f"[{timestamp}] {note}")


class AlphaPilotProgram:
    """Manages enterprise alpha pilot program."""
    
    def __init__(self):
        self.customers: Dict[str, PilotCustomer] = {}
        self.initialize_alpha_customers()
    
    def initialize_alpha_customers(self) -> None:
        """Initialize 5 alpha pilot customers."""
        
        # Customer 1: FinanceFlow (Fintech)
        customer1 = PilotCustomer(
            customer_id="ALPHA-001",
            company_name="FinanceFlow Inc",
            industry=IndustryVertical.FINTECH,
            contact_email="cto@financeflow.io",
            start_date=datetime(2026, 1, 16),
            arr_potential=500000.00,
            use_cases=[
                "Automated transaction monitoring",
                "Fraud detection with AI agents",
                "Customer service automation"
            ],
            phase=PilotPhase.INTEGRATION,
            health_score=92.0
        )
        customer1.add_note("Initial call completed - very excited about AI agents")
        customer1.add_note("Technical integration in progress")
        self.customers[customer1.customer_id] = customer1
        
        # Customer 2: MedTech Solutions (Healthcare)
        customer2 = PilotCustomer(
            customer_id="ALPHA-002",
            company_name="MedTech Solutions",
            industry=IndustryVertical.HEALTHCARE,
            contact_email="innovation@medtech.health",
            start_date=datetime(2026, 1, 14),
            arr_potential=750000.00,
            use_cases=[
                "Patient data analysis",
                "Treatment recommendation engine",
                "HIPAA-compliant data monetization"
            ],
            phase=PilotPhase.TESTING,
            health_score=88.0
        )
        customer2.add_note("HIPAA compliance reviewed - all clear")
        customer2.add_note("Testing environment configured")
        self.customers[customer2.customer_id] = customer2
        
        # Customer 3: ShopSmart (E-commerce)
        customer3 = PilotCustomer(
            customer_id="ALPHA-003",
            company_name="ShopSmart Global",
            industry=IndustryVertical.ECOMMERCE,
            contact_email="tech@shopsmart.com",
            start_date=datetime(2026, 1, 12),
            arr_potential=350000.00,
            use_cases=[
                "Product recommendation AI",
                "Inventory optimization",
                "Customer behavior analysis"
            ],
            phase=PilotPhase.PRODUCTION,
            health_score=95.0
        )
        customer3.add_note("Production deployment successful")
        customer3.add_note("Seeing 15% increase in conversion rates")
        self.customers[customer3.customer_id] = customer3
        
        # Customer 4: LogiChain (Logistics)
        customer4 = PilotCustomer(
            customer_id="ALPHA-004",
            company_name="LogiChain Logistics",
            industry=IndustryVertical.LOGISTICS,
            contact_email="ops@logichain.io",
            start_date=datetime(2026, 1, 10),
            arr_potential=450000.00,
            use_cases=[
                "Route optimization",
                "Demand forecasting",
                "Fleet management automation"
            ],
            phase=PilotPhase.PRODUCTION,
            health_score=90.0
        )
        customer4.add_note("Full fleet integration complete")
        customer4.add_note("20% reduction in fuel costs observed")
        self.customers[customer4.customer_id] = customer4
        
        # Customer 5: MediaMax (Media)
        customer5 = PilotCustomer(
            customer_id="ALPHA-005",
            company_name="MediaMax Entertainment",
            industry=IndustryVertical.MEDIA,
            contact_email="data@mediamax.tv",
            start_date=datetime(2026, 1, 15),
            arr_potential=600000.00,
            use_cases=[
                "Content recommendation AI",
                "Viewer behavior analysis",
                "Ad targeting optimization"
            ],
            phase=PilotPhase.TRAINING,
            health_score=85.0
        )
        customer5.add_note("Team training scheduled for next week")
        customer5.add_note("Integration architecture designed")
        self.customers[customer5.customer_id] = customer5
    
    def get_customer(self, customer_id: str) -> PilotCustomer:
        """Get customer by ID."""
        return self.customers.get(customer_id)
    
    def list_customers_by_phase(self, phase: PilotPhase) -> List[PilotCustomer]:
        """List customers in specific phase."""
        return [
            customer for customer in self.customers.values()
            if customer.phase == phase
        ]
    
    def get_program_metrics(self) -> Dict[str, Any]:
        """Calculate program-wide metrics."""
        customers = list(self.customers.values())
        
        total_arr = sum(c.arr_potential for c in customers)
        avg_health = sum(c.health_score for c in customers) / len(customers)
        
        phase_breakdown = {}
        for phase in PilotPhase:
            count = len(self.list_customers_by_phase(phase))
            phase_breakdown[phase.value] = count
        
        industry_breakdown = {}
        for industry in IndustryVertical:
            count = len([c for c in customers if c.industry == industry])
            if count > 0:
                industry_breakdown[industry.value] = count
        
        return {
            "total_customers": len(customers),
            "total_arr_potential": total_arr,
            "average_health_score": avg_health,
            "phase_breakdown": phase_breakdown,
            "industry_breakdown": industry_breakdown,
            "production_customers": len(self.list_customers_by_phase(PilotPhase.PRODUCTION)),
            "success_rate": len(self.list_customers_by_phase(PilotPhase.SUCCESS)) / len(customers) * 100
        }
    
    def generate_report(self) -> str:
        """Generate program status report."""
        metrics = self.get_program_metrics()
        
        report = []
        report.append("="*70)
        report.append("ENTERPRISE ALPHA PILOT PROGRAM - STATUS REPORT")
        report.append("="*70)
        report.append(f"Generated: {datetime.utcnow().isoformat()}")
        report.append("")
        
        report.append("PROGRAM SUMMARY")
        report.append("-"*70)
        report.append(f"Total Customers: {metrics['total_customers']}")
        report.append(f"Total ARR Potential: ${metrics['total_arr_potential']:,.2f}")
        report.append(f"Average Health Score: {metrics['average_health_score']:.1f}/100")
        report.append(f"Production Customers: {metrics['production_customers']}")
        report.append("")
        
        report.append("PHASE BREAKDOWN")
        report.append("-"*70)
        for phase, count in metrics['phase_breakdown'].items():
            if count > 0:
                report.append(f"{phase.title()}: {count} customers")
        report.append("")
        
        report.append("CUSTOMER DETAILS")
        report.append("-"*70)
        for customer in self.customers.values():
            report.append(f"\n{customer.company_name} ({customer.customer_id})")
            report.append(f"  Industry: {customer.industry.value}")
            report.append(f"  Phase: {customer.phase.value}")
            report.append(f"  Health Score: {customer.health_score}/100")
            report.append(f"  ARR Potential: ${customer.arr_potential:,.2f}")
            report.append(f"  Days in Pilot: {customer.get_days_in_pilot()}")
            report.append(f"  Use Cases: {len(customer.use_cases)}")
            if customer.notes:
                report.append(f"  Latest Note: {customer.notes[-1]}")
        
        report.append("")
        report.append("="*70)
        
        return "\n".join(report)


if __name__ == "__main__":
    program = AlphaPilotProgram()
    print(program.generate_report())
