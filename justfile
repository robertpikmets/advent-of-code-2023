# List all available recipes
default:
	just --list

# Run checks (ruff + black)
check:
	ruff days
	black --check days

# Automatically fix all formating (ruff + black)
format:
	black days
	ruff --fix days
