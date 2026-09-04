import { Loader2, Search, X } from "lucide-react";
import { cn } from "../../lib/cn";

export function Button({
  variant = "primary",
  size = "md",
  loading = false,
  className,
  children,
  ...props
}) {
  const variants = {
    primary:
      "bg-violet-500 text-white hover:bg-violet-400 border-violet-400/20",
    secondary:
      "bg-[#151923] text-slate-200 hover:bg-[#191e28] border-[#252a35]",
    ghost:
      "bg-transparent text-slate-300 hover:bg-white/[0.04] border-transparent",
    danger:
      "bg-red-500/10 text-red-300 hover:bg-red-500/20 border-red-500/20",
  };

  const sizes = {
    sm: "px-3 py-2 text-xs",
    md: "px-4 py-2.5 text-sm",
    lg: "px-5 py-3 text-sm",
  };

  return (
    <button
      className={cn(
        "inline-flex items-center justify-center gap-2 rounded-xl border font-medium transition disabled:cursor-not-allowed disabled:opacity-50",
        variants[variant],
        sizes[size],
        className,
      )}
      disabled={loading || props.disabled}
      {...props}
    >
      {loading && <Loader2 size={15} className="animate-spin" />}
      {children}
    </button>
  );
}

export function Input({ label, error, className, ...props }) {
  return (
    <label className="block">
      {label && (
        <span className="mb-2 block text-xs font-medium text-slate-400">
          {label}
        </span>
      )}
      <input
        className={cn(
          "w-full rounded-xl border border-[#252a35] bg-[#10131a] px-3.5 py-2.5 text-sm text-slate-100 outline-none transition placeholder:text-slate-600 focus:border-violet-500/60 focus:ring-2 focus:ring-violet-500/10",
          className,
        )}
        {...props}
      />
      {error && <span className="mt-1 block text-xs text-red-400">{error}</span>}
    </label>
  );
}

export function Select({ label, options = [], className, ...props }) {
  return (
    <label className="block">
      {label && (
        <span className="mb-2 block text-xs font-medium text-slate-400">
          {label}
        </span>
      )}
      <select
        className={cn(
          "w-full rounded-xl border border-[#252a35] bg-[#10131a] px-3.5 py-2.5 text-sm text-slate-100 outline-none focus:border-violet-500/60",
          className,
        )}
        {...props}
      >
        {options.map((option) => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>
    </label>
  );
}

export function Textarea({ label, className, ...props }) {
  return (
    <label className="block">
      {label && (
        <span className="mb-2 block text-xs font-medium text-slate-400">
          {label}
        </span>
      )}
      <textarea
        className={cn(
          "min-h-24 w-full rounded-xl border border-[#252a35] bg-[#10131a] px-3.5 py-2.5 text-sm text-slate-100 outline-none focus:border-violet-500/60",
          className,
        )}
        {...props}
      />
    </label>
  );
}

export function Card({ className, children }) {
  return (
    <div
      className={cn(
        "rounded-2xl border border-[#252a35] bg-[#10131a]",
        className,
      )}
    >
      {children}
    </div>
  );
}

export function Badge({ value }) {
  const normalized = String(value || "").toLowerCase();

  let tone = "bg-slate-500/10 text-slate-300 border-slate-500/20";

  if (
    normalized.includes("active") ||
    normalized.includes("available") ||
    normalized.includes("paid") ||
    normalized.includes("completed")
  ) {
    tone = "bg-emerald-500/10 text-emerald-300 border-emerald-500/20";
  }

  if (
    normalized.includes("low") ||
    normalized.includes("reserved") ||
    normalized.includes("pending")
  ) {
    tone = "bg-amber-500/10 text-amber-300 border-amber-500/20";
  }

  if (
    normalized.includes("inactive") ||
    normalized.includes("critical") ||
    normalized.includes("failed")
  ) {
    tone = "bg-red-500/10 text-red-300 border-red-500/20";
  }

  if (normalized.includes("occupied")) {
    tone = "bg-violet-500/10 text-violet-300 border-violet-500/20";
  }

  return (
    <span
      className={cn(
        "inline-flex rounded-full border px-2.5 py-1 text-[11px] font-medium",
        tone,
      )}
    >
      {value || "â€”"}
    </span>
  );
}

export function SearchBox({ value, onChange, placeholder = "Search..." }) {
  return (
    <div className="relative">
      <Search
        size={16}
        className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-600"
      />
      <input
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder={placeholder}
        className="w-full rounded-xl border border-[#252a35] bg-[#10131a] py-2.5 pl-9 pr-3 text-sm text-slate-200 outline-none focus:border-violet-500/60"
      />
    </div>
  );
}

export function EmptyState({ title = "No records found", text }) {
  return (
    <div className="flex min-h-52 flex-col items-center justify-center p-8 text-center">
      <div className="mb-3 rounded-full border border-[#252a35] bg-[#151923] p-3">
        <Search size={18} className="text-slate-500" />
      </div>
      <h3 className="text-sm font-semibold text-slate-200">{title}</h3>
      {text && <p className="mt-1 max-w-sm text-xs text-slate-500">{text}</p>}
    </div>
  );
}

export function Skeleton({ className }) {
  return (
    <div
      className={cn(
        "animate-pulse rounded-xl bg-[#191d27]",
        className,
      )}
    />
  );
}

export function Modal({ open, title, onClose, children, wide = false }) {
  if (!open) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/65 p-4 backdrop-blur-sm">
      <div
        className={cn(
          "max-h-[90vh] w-full overflow-auto rounded-2xl border border-[#252a35] bg-[#10131a] shadow-2xl",
          wide ? "max-w-3xl" : "max-w-lg",
        )}
      >
        <div className="sticky top-0 flex items-center justify-between border-b border-[#252a35] bg-[#10131a] px-5 py-4">
          <h2 className="text-sm font-semibold text-white">{title}</h2>
          <button
            onClick={onClose}
            className="rounded-lg p-1.5 text-slate-500 hover:bg-white/[0.04] hover:text-slate-200"
          >
            <X size={17} />
          </button>
        </div>

        <div className="p-5">{children}</div>
      </div>
    </div>
  );
}
