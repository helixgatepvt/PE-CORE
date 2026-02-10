create table decision_snapshots (
  snapshot_id uuid primary key default gen_random_uuid(),
  deal_id text not null,
  decision_type text not null,
  decision_pointer text not null
    check (decision_pointer in ('PROCEED','PROCEED_WITH_CONDITIONS','DO_NOT_PROCEED')),
  assumptions_vector jsonb not null,
  risk_vector jsonb not null,
  fragility_profile jsonb,
  cross_sphere_exposure jsonb,
  unresolved_conditions jsonb,
  accepted_risks jsonb,
  engine_version_hash text not null,
  created_at timestamp with time zone default now()
);

