create table ccm_fee_records (
  fee_id uuid primary key default gen_random_uuid(),
  ccm_id uuid not null references capital_clearance_opinions(ccm_id),
  deployed_capital_amount numeric not null,
  fee_rate numeric not null default 0.02,
  calculated_fee numeric not null,
  fee_status text not null default 'RECORDED',
  created_at timestamp with time zone default now()
);

