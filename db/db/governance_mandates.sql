create table governance_mandates (
  mandate_id uuid primary key default gen_random_uuid(),
  fund_id text not null,
  mandate_name text not null,
  required_snapshot boolean not null default true,
  required_assumptions boolean not null default true,
  required_risk_acceptance boolean not null default true,
  required_dissent_record boolean not null default false,
  minimum_reviewers integer not null default 1,
  enforcement_level text not null
    check (enforcement_level in ('ADVISORY','STRICT')),
  created_at timestamp with time zone default now()
);
